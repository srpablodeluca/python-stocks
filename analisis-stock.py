"""
Created on Wed Aug  5 11:02:14 2020

@author: Pablo
"""
import pandas_datareader.data as web
import datetime
import mplfinance as mpf

def grafico(stock):
    
    mc = mpf.make_marketcolors(base_mpf_style='nightclouds',up='g',down='r',volume="grey", inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='nightclouds',marketcolors=mc)
    mpf.plot(stock,type='candle', style=s, title=" 50 días",
              ylabel="Precio $(pesos)", ylabel_lower="Volumen", volume=True,
              mav=(3,6,9), savefig="stock.png", figsize=(16,8))



stock = ["ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CEPU.BA", "COME.BA", 
         "CRES.BA", "CVH.BA", "EDN.BA", "GGAL.BA", "MIRG.BA",
         "PAMP.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", 
         "TXAR.BA", "VALO.BA", "YPFD.BA"]

start_dt = datetime.datetime(2020,6,11)
end_dt = datetime.datetime.today()


for ticket in stock:
    
    ticket1 = web.DataReader(ticket, "yahoo", start_dt, end_dt)
    # p_max = ticket1.Close.max()
    # p_min = ticket1.Close.min()
    p_prom = ticket1.Close.mean()
    # p_prom2 = (p_max + p_min)/2
    if (ticket1["Adj Close"][-1]) < p_prom:
        print(str(ticket) +" Interesante para comprar")
        grafico(ticket)
    else:
        print(str(ticket)+" No comrpar, ponele")
    
    
    




