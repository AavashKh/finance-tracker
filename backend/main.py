from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Online", "message": "CashRiver is liquid"}

@app.get("/ticker/{symbol}")
def get_ticker_info(symbol: str):
    return {"symbol": symbol.upper(), "price": 150.00, "currency": "USD"}