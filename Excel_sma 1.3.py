import yfinance as yf
from pandas_datareader import data as pdr 
import math
import pandas as pd

yf.pdr_override()

def comprar(ticket):
    df = pdr.get_data_yahoo(ticket, period="50d")

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
    
def adj(ticket1):
    df1 = pdr.get_data_yahoo(ticket1, period="1d")
    ult_price = df1["Adj Close"][-1]
    return ult_price

def sma1(ticket1):
    df1 = pdr.get_data_yahoo(ticket1, period="50d")
    df1["sma"] = df1["Adj Close"].rolling(window=5).mean()
    sma = df1["sma"][-1]
    return sma

stock = ["ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CEPU.BA", "COME.BA", 
         "CRES.BA", "CVH.BA", "EDN.BA", "GGAL.BA", "MIRG.BA",
         "PAMP.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", 
         "TXAR.BA", "VALO.BA", "YPFD.BA"]

stocks = pd.DataFrame(data = stock, columns=["Tickets"])

stocks["Acción"] = 0
stocks["Adj Close"] = 0
stocks["sma"] = 0

cont = 0


for i in stock:
    print(i)
    if comprar(i) == True:
        print("Comprar "+ str(i))
        stocks["Acción"][cont] = "Comprar"
        stocks["Adj Close"][cont] = adj(i)
        stocks["sma"][cont] = sma1(i)
        
            
    else:
        print("No comprar "+ str(i))
        stocks["Acción"][cont] = "No comprar"
        stocks["Adj Close"][cont] = adj(i)
        stocks["sma"][cont] = sma1(i)
    cont += 1
        
print(stocks)

stocks.to_excel("Stocks análisis.xlsx")
        

        
        
        
        
        
        
        