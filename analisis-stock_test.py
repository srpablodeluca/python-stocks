"""
Created on Wed Aug  5 11:02:14 2020

@author: Pablo
"""
import pandas_datareader.data as web
import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt

def grafico(stock,name):
    
    mc = mpf.make_marketcolors(base_mpf_style='nightclouds',up='g',down='r',volume="grey", inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='nightclouds',marketcolors=mc)
    mpf.plot(stock,type='candle', style=s, title=(name+" 50 días"),
              ylabel="Precio $(pesos)", ylabel_lower="Volumen", volume=True,
              mav=(3,6,9), savefig=dict(fname=name), figsize=(16,8))
    
def grafico_lineal(stock1,name):
    stock_promedio = stock1[["Adj Close","Promedio"]]
    plt.plot(stock_promedio)
    plt.show()
    plt.savefig(name)


def find_stock(stock2):
    for i_stock in stock2:
        ticket1 = web.DataReader(i_stock, "yahoo", start_dt, end_dt)
        p_prom = ticket1.Close.mean()
        ticket1["Promedio"] = p_prom
        
        
        if (ticket1["Adj Close"][-1]) < p_prom:
            print(str(i_stock) +" Interesante para comprar")
            # grafico(ticket1,i_stock)
            grafico_lineal(ticket1,i_stock)
            
        else:
            pass
            #print(str(i_stock)+" No comrpar")
    

stock_BA = ["ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CEPU.BA", "COME.BA", 
         "CRES.BA", "CVH.BA", "EDN.BA", "GGAL.BA", "MIRG.BA",
         "PAMP.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", 
         "TXAR.BA", "VALO.BA", "YPFD.BA"]

stock_cedears = ['MMM','ANF','ADGO','ADBE','AMD','AEG','AEM','BABA',
                  'ACH','AMZN','ABEV','AMX','AXP','AIG','AMGN',
                  'ADI','AAPL','AMAT','ARCO','ADP','AVY','CAR','BIDU',
                  'BBD','BSBR','BCS','BAYN.DE','BBVA',
                  'BIIB','BRFS','BMY','CVX','LFC','CHL','CHA',
                  'CEO','SBS','ELP',
                  'SID','GLW','DESP','DTEA','EBAY',
                  'LLY','ERJ','XOM','FSLR','FMX','FMCC','FCX','GRMN',
                  'GGB','GILD','GFI','PAC','ASR','HOG','HMY',
                  'HDB','HON','HWM','IBN','INFY','ING','INTC','IBM',
                  'IFF','ITUB','JPM','JNJ','JCI','JOYY','KMB','KGC',
                  'PHG','KEP','ERIC','LYG','LMT','MMC','MCD','MDT','MELI','MRK',
                  'MUFG','MFG','MBT','MSI','NGG','NTCO','NTES','NFLX',
                  'NEM','NKE','NVS','NVDA','ORCL',
                  'ORAN','PCAR','PYPL','PBR','PFE',
                  'QCOM','ROST','CRM','SAP','SNAP','SNE','SBUX',
                  'SUZ','SYY','TSM','TGT','VIV','TEN','TSLA',
                  'HSY','DIS','TMO','TSU','TOT','TRIP','TWTR','USB',
                  'UGP','URBN','VALE','VEDL','WMT','WFC',
                  'WBK','AUY','YELP', "GOOGL","GLNT.BA", "ABT","AZN","BA",
                  "BHP","BIIB","BNG.BA","BP","C", "CAT","CSCO","CX",
                  "FB","GE","GOLD","GSK","KO","LVS","MSFT","PEP","PG",
                  "PTR","RIO","T","TM","TXN","TX","UN","V","VIST",
                  "VOD","VZ","X","XROX.BA"] 




start_dt = datetime.datetime(2020,6,11)
end_dt = datetime.datetime.today()

print("CEDEARS")
find_stock(stock_cedears)






    
    
    




