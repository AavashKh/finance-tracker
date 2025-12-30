import pandas as pd
from sqlalchemy import create_engine, text
import logging

class StockDataPipeline:
    def __init__(self, csv_path, db_url):
        self.csv_path = csv_path
        # In Dev: The Engine handles the Connection Pool
        self.engine = create_engine(db_url)
        self.data = None
        
        # Setting up logging for audit trails
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract(self):
        """Extract: Read raw data from source."""
        self.logger.info(f"Extracting data from {self.csv_path}")
        self.data = pd.read_csv(self.csv_path)
        return self

    def transform(self):
        """Transform: Apply business rules and data cleaning."""
        if self.data is None:
            raise ValueError("No data found. Run extract() first.")
        
        self.logger.info("Transforming Tickers to Uppercase and cleaning data...")
        
        # Finance Logic: Ensure symbology is standardized
        self.data['Ticker'] = self.data['Ticker'].str.strip().str.upper()
        
        # Dev Logic: Handle missing values to prevent DB NULL errors
        self.data = self.data.dropna(subset=['Ticker', 'Price'])

        mapping = {
            'Ticker': 'sSymbol',
            'Price': 'currentPrice'
        }
        self.data = self.data.rename(columns=mapping)

        self.logger.info(f"Mapped columns to : {self.data.columns.tolist()}")
        return self

    def load(self, table_name):
        # Load CSV into a staging table (Overwrite if exists)
        self.data.to_sql('temp_stocks', self.engine, if_exists='replace', index=False)
    
        # The Upsert Logic
        upsert_query = text(f"""
            INSERT INTO {table_name} (sSymbol, currentPrice)
            SELECT sSymbol, currentPrice FROM temp_stocks
            ON DUPLICATE KEY UPDATE 
            currentPrice = VALUES(currentPrice);
        """)
    
        with self.engine.begin() as conn:
            conn.execute(upsert_query)
            # Cleanup
            conn.execute(text("DROP TABLE temp_stocks;"))
        
        self.logger.info("Upsert complete: Prices updated and new tickers added.")

if __name__ == "__main__":
    DB_URL = "mysql+pymysql://root:@localhost:3306/test"
    
    pipeline = StockDataPipeline("ticker_price.csv", DB_URL)
    pipeline.extract().transform().load("STOCKS")