import yfinance as yf
import os

# Create folder
os.makedirs("data", exist_ok=True)

# NSE tickers
tickers = {
    "NIFTY_50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "ITC": "ITC.NS",
    "INFY": "INFY.NS"
}


for name, symbol in tickers.items():
    df = yf.download(symbol, period="1y", interval="1d")
    df.to_csv(f"data/{name}.csv")

print(" All data saved in 'data/' folder")
