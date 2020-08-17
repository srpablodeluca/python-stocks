from pandas_datareader import data as pdr 
import math
import pandas_datareader.data as web


def comprar(ticket,start_dt,end_dt):
    df = web.DataReader(ticket, "yahoo", start_dt, end_dt)

    df["sma"] = df["Adj Close"].rolling(window=5).mean()
    smaLo = 0
    smaHi = 0
    cont = 0

    df["Line"] = None

    for sma1 in df["sma"]:
        if math.isnan(df["sma"][cont]):
            pass
        else:
            if sma1 > df["Adj Close"][cont]:
                df.loc[:,("Line")][cont] = "Hi"
                smaHi += 1
            else:
                df.loc[:,("Line")][cont] = "Low"
                smaLo += 1
        cont += 1
    
    if smaLo > smaHi:
        return True
    else:
        return False
    
# def adj(ticket1):
#     df1 = pdr.get_data_yahoo(ticket1, period="1d")
#     ult_price = df1["Adj Close"][-1]
#     return ult_price

# def sma1(ticket1):
#     df1 = pdr.get_data_yahoo(ticket1, period="50d")
#     df1["sma"] = df1["Adj Close"].rolling(window=5).mean()
#     sma = df1["sma"][-1]
#     return sma




        
        
        
        
        