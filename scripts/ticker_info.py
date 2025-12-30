import yfinance as yf
import time
import csv

# Setup for yfinance (using a session is best practice)

tickers = ['AMZN', 'INTC', 'LLY', 'META', 'MSFT',
           'NFLX', 'NVDA', 'ORCL', 'PATH', 'PRME']

data = {} # Still good for checking data internally

# 1. Open the file ONCE outside the loop (using 'w' for initial write)
with open('ticker_price.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # 2. Write the Header Row ONCE
    writer.writerow(['Ticker', 'Price']) 

    for ticker in tickers:
        try:
            # Create the Ticker object using the session
            ticker_symbol = yf.Ticker(ticker)

            # Access the price info
            ticker_info = ticker_symbol.info
            current_price = ticker_info.get('currentPrice')
            
            # Use history() as a fallback if currentPrice isn't available
            if current_price is None:
                current_price = ticker_symbol.history(period='1d')['Close'].iloc[-1]
            
            # Store data internally (optional, but useful)
            data[ticker] = current_price
            
            # 3. Write a single ROW: a list containing the ticker and the price
            writer.writerow([ticker, current_price]) # <- FIX: Pass a list/iterable
            
            print(f"Successfully fetched and wrote data for {ticker}: ${current_price}")

        except Exception as e:
            # 4. Include error handling and a time delay for good measure
            print(f"Error fetching data for {ticker}: {e}")
            
        # 5. Always include throttling when looping over yfinance
        time.sleep(3) 

print("\nData collection complete. Check 'ticker_price.csv'.")