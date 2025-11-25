import requests
import yfinance as yf
import time
from fake_useragent import UserAgent

ua = UserAgent()

session = requests.Session()
session.headers.update({'User-Agent': ua.random})

tickers = ['LLY', 'INTC']
data = {}

for ticker in tickers:
    try:
        ticker_symbol = yf.Ticker(ticker, session=session)
        price = ticker_symbol.history(period='1d')

        data[ticker] = price
        print(f"Price for {ticker} : {data[ticker].head()}")
    
    except Exception as e:
        print(f"Error for {ticker} : {e}")

    time.sleep(3)

print(data)