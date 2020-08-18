
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
                df.loc[:,("Line")][cont] = "Hi" #El precio cierra por debajo del sma
                smaHi += 1
            else:
                df.loc[:,("Line")][cont] = "Low" #El precio cierra por encima del sma
                smaLo += 1
        cont += 1
    
    if smaLo > smaHi: 
        if df["Adj Close"][-1] < df["sma"][-1]: 
            return "Comprar" #Si Adj Close es menor que el sma conviene comprar
        else:
            return "No comprar"
    else:
        return "No comprar" #No conviene comprar 








        
        
        
        
        