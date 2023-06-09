import pandas_datareader as data
import datetime as dt

from datetime import datetime
import yfinance as yf
import pandas_datareader.data as pdr
import pandas as pd


start = dt.datetime(2022, 4, 1)
end = dt.datetime(2022, 5, 30)
data = data.get_data_yahoo('AAPL', start, end)
print(data)

yf.pdr_override()

start = datetime.strptime('2022-04-01', '%Y-%m-%d')
end = datetime.strptime('2022-05-01', '%Y-%m-%d')

aaplprices = pdr.get_data_yahoo("AAPL", start, end)

del aaplprices['Volume']
aaplprices.head()

aaplprices.values.tolist()

aaplprices.plot()
