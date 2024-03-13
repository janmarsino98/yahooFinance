import pandas as pd
import yfinance as yf


company = yf.Ticker("OAK"+".AX")
info = company.info
print(info)