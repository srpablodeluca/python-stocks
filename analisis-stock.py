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


def find_stock(stock):
    for i_stock in stock:
        ticket1 = web.DataReader(i_stock, "yahoo", start_dt, end_dt)
        p_prom = ticket1.Close.mean()
        
        if (ticket1["Adj Close"][-1]) < p_prom:
            print(str(i_stock) +" Interesante para comprar")
            #grafico(i_stock)
            
        else:
            pass
            #print(str(i_stock)+" No comrpar, ponele")
    

stock_BA = ["ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CEPU.BA", "COME.BA", 
         "CRES.BA", "CVH.BA", "EDN.BA", "GGAL.BA", "MIRG.BA",
         "PAMP.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", 
         "TXAR.BA", "VALO.BA", "YPFD.BA"]

stock_cedears = ['MMM','ANF','ADGO','ADBE','AMD','AEG','AEM','BABA',
                  'ACH','AMZN','ABEV','AMX','AXP','AIG','AMGN',
                  'ADI','AAPL','AMAT','ARCO','ADP','AVY','CAR','BIDU',
                  'BBD','BSBR','BCS','BAYN','BBVA',
                  'BIIB','BRFS','BMY','CVX','LFC','CHL','CHA',
                  'CEO','CDE','SBS','ELP',
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
                  'WBK','AUY','YELP', "GOOGL"] 




start_dt = datetime.datetime(2020,6,11)
end_dt = datetime.datetime.today()

tkr = ["BBD"]

find_stock(stock_cedears)





    
    
    




