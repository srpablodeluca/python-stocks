import pandas_datareader
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import mplfinance as mpf
#%matplotlib inline 

# tesla = web.DataReader("TSLA", "yahoo")
# aapl = web.DataReader("AAPL", "yahoo")
# qqq = web.DataReader("qqq", "yahoo")

# tesla["Adj Close"].plot(label="Tesla", figsize=(12,8), title="Adj Close")
# aapl["Adj Close"].plot(label="Apple")
# qqq["Adj Close"].plot(label="QQQ")
# plt.legend();
# plt.show()

# tesla["ma50"] = tesla["Adj Close"].rolling(50).mean()
# tesla["ma30"] = tesla["Adj Close"].rolling(30).mean()
# tesla[["Adj Close", "ma30", "ma50"]].plot(label="Tesla",figsize=(16,8), title="Moving Average");
# plt.show()

start = datetime.datetime(2020,7,1)
end = datetime.datetime(2020,7,31) 
tesla = web.DataReader("TSLA", "yahoo", start, end)
# tesla.shape
# tesla.head(3)
# tesla.tail(3)

# mpf.plot(tesla)
mc = mpf.make_marketcolors(base_mpf_style='nightclouds',up='g',down='r',volume="grey", inherit=True)
s  = mpf.make_mpf_style(base_mpf_style='nightclouds',marketcolors=mc)

mpf.plot(tesla,type='candle', style=s, title="Tesla Julio 2020",
             ylabel="Precio u$d", ylabel_lower="Volumen", volume=True,
             mav=(3,6,9), savefig="testing.png", figsize=(16,8))
plt.show()
#mpf.plot(tesla,type='candle',mav=(3,6,9),volume=True)



