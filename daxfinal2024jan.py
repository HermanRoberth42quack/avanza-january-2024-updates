# -*- coding: utf-8 -*-



import time
import numpy as np
import pandas as pd
from maintv import TvDatafeed,Interval


#import sympy
import datetime
import math

from datetime import datetime
#from sympy import solve, Symbol, nsolve,pi
#import time
import talib
from avanza import Avanza,OrderType,InstrumentType
from avanza import Avanza,OrderType,InstrumentType
#import datetime
#import hashlib
#import pyotp
from scipy.stats import skewnorm
#import numpy as np

from datetime import date
import warnings

#from tvlive import TvDatafeedLive

#username = 'Herman_Roberth'
#password = 'Ledzeppelinpinkfloyd123'


tv = TvDatafeed()

warnings.simplefilter(action="ignore",category= FutureWarning)
#import matplotlib.pyplot as plt

#totp = pyotp.TOTP("HGR5JY7LUORXDYNM5IYAZ6A6S7PHCWVE", digest=hashlib.sha1)
#print(totp.now())


avanza = Avanza({
    'username': 'Herman_Roberth',
    'password': 'Sweetheart123',
    'totpSecret': 'HGR5JY7LUORXDYNM5IYAZ6A6S7PHCWVE'
})


username = 'Herman_Roberth'
password = 'Ledzeppelinpinkfloyd123'

#tv = TvDatafeed(username, password)

account_number=9651099
path_to_data=r'C:\Users\herma\Desktop\collected data try 1236.xlsx'


datee= "2024-05-03"
Is_Real_off= "YESS ACTUALL MONEY"   


#####reading data
def dax_data_5min():
    path_to_data=  r"C:\Users\herma\Desktop\Dax_data\5min.xlsx"
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    return df
def dax_data_15min():
    path_to_data=  r"C:\Users\herma\Desktop\Dax_data\15min.xlsx"
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    return df
def dax_data_30min():
    path_to_data=  r"C:\Users\herma\Desktop\Dax_data\30min.xlsx"
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    return df
def dax_data_1hour():
    path_to_data=  r"C:\Users\herma\Desktop\Dax_data\1hour.xlsx"
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    return df
def dax_data_4hours():
    path_to_data=  r"C:\Users\herma\Desktop\Dax_data\4hours.xlsx"
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    
    return df
def ALL3minfunctions():
    dax_data=tv.get_hist('DE30EUR','OANDA',interval=Interval.in_3_minute,n_bars=400)
    real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=42)
    adx47=real[-1]
    adxdif=((real[-1]-real[-2])/real[-2])*500
    
    dax_data1=dax_data.tail(1)
    dax_data40=dax_data.tail(40)
    dax_data70=dax_data.tail(70)
    y40=((dax_data40.high+ dax_data40.low+dax_data40.close)/3).mean()    
    z70=((dax_data70.high+ dax_data70.low+dax_data70.close)/3).mean()    
    hlc370=(dax_data70.high+ dax_data70.low+dax_data70.close)/3   
    hlc3=(dax_data1.high+ dax_data1.low+dax_data1.close)/3
    cci=(((hlc3)-y40))/(np.abs(((hlc370)-z70)).mean()*0.015)
    df=pd.concat([cci],axis=1)
    cur=np.max(df,axis=1).sum()
    
    current_price=dax_data.close[-1]
    
    surge_1=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=14)
    surge=surge_1[-1]
    
    stdev=talib.STDDEV(dax_data.close, timeperiod=14)
    surge_protection=((stdev[-1]/surge_1[-1])-(stdev[-2]/surge_1[-2]))*10/(stdev[-2]/surge_1[-2])
    sma_atr=talib.SMA(surge_1,timeperiod=6)
    sma_stdev=talib.SMA(stdev,timeperiod=6)
    surge_sma=((sma_stdev[-1]/sma_atr[-1])-(sma_stdev[-2]/sma_atr[-2]))*10/(sma_stdev[-2]/sma_atr[-2])
    
    EE=talib.STDDEV(dax_data.close, timeperiod=50)[-1]
    EEB=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    EEC=talib.WMA(EEB,timeperiod=50)[-1]
    Exception_entry=EE/EEC
    
    Recalibrate=abs(dax_data.close[-1]-dax_data.open[-48])
    
    return adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate
#print(dax_data)


def All5minfunctions(): 
    #dax_data=tv.get_hist(interval=Interval.in_5_minute,n_bars=500)
    dax_data=dax_data_5min()
    EESTDEV=talib.STDDEV(dax_data.close, timeperiod=50)
    EEATR=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=50)
    Vol_ratio=(EESTDEV/EEATR)
    
    d=talib.WMA(Vol_ratio,timeperiod=25).iloc[-1]
    
    Exception_exit=Vol_ratio.iloc[-1]-d
    
    Minus= talib.MINUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    Plus= talib.PLUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    a=(Minus.iloc[-1]+Plus.iloc[-1])
    avg=a.sum()/2
    adx = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=32)
    
    sma=talib.SMA(adx,timeperiod=74).iloc[-1]
    wma=talib.SMA(adx,timeperiod=74).iloc[-1]
    smalow=talib.SMA(adx,timeperiod=32).iloc[-1]
    wmalow=talib.SMA(adx,timeperiod=32).iloc[-1]
    
    smalow2=talib.SMA(adx,timeperiod=32).iloc[-1]
    wmalow2=talib.SMA(adx,timeperiod=32).iloc[-1]
    current_price_5min=dax_data.close.iloc[-1]
    
    return Exception_exit, avg, sma, wma,smalow,wmalow,smalow2,wmalow2,current_price_5min

####### 15 min
def All15minfunctions():
    dax_data=dax_data_15min()
   
    stdev=talib.STDDEV(dax_data.close, timeperiod=22).iloc[-1]
    atr=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    atrwma=talib.WMA(atr,timeperiod=22).iloc[-1] 
    True_Ratio=stdev/atrwma
    
    ATR15min=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=20).iloc[-1]
   
    a=talib.STDDEV(dax_data.close, timeperiod=22).iloc[-1]
    b=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    c=talib.SMA(b,timeperiod=22).iloc[-1]
    rma=a/c
    return True_Ratio, ATR15min,rma


######### 1 Hour

def All1hourfunctions():
    dax_data=dax_data_1hour()

    real = talib.ADX(dax_data.high , dax_data.low, dax_data.close, timeperiod=12)
    adx1h=real.iloc[-1]
    
    adx1hwma=talib.WMA(real,timeperiod=12).iloc[-1]
    diffadxwma=adx1h- adx1hwma
    
    q=real-real.shift(1)
    diffprev=q.iloc[-1]
    
    
    diffprevwma=talib.WMA(q, timeperiod=12).iloc[-1]
    changeprevwma=diffprev-diffprevwma
   
   
    return adx1h,diffadxwma,diffprev,changeprevwma
    

#print(ADX1h())
###### 4 hours
def All4hourfunctions():
    dax_data=dax_data_4hours()

    real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=50)
    adx=real.iloc[-1]
    adxwma=talib.WMA(real,timeperiod=25).iloc[-1]
    Dist_adx_wma=adx-adxwma
    q=real-real.shift(1)
    Diff_previous=q.iloc[-1]
    wma=talib.WMA(q, timeperiod=30).iloc[-1]
    diff_previous_wma=Diff_previous-wma
    
    distance=abs(dax_data.close.iloc[-1]-dax_data.close.iloc[-2])
    return Dist_adx_wma,Diff_previous,diff_previous_wma,distance

#print(All1hourfunctions())
######### SLS
##calling the functions
##adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate=ALL3minfunctions()
#Exception_exit, avg, sma, wma,smalow,wmalow,smalow2,wmalow2= All5minfunctions()
#True_Ratio, ATR15min,rma=All15minfunctions()
#adx1h,diffadxwma,diffprev,changeprevwma = All1hourfunctions()
#Dist_adx_wma,Diff_previous,diff_previous_wma,distance=All4hourfunctions()

def sl5mindax(diffadxwma):
    #dax_data=dax_data_5min()
    #dax_data=tv.get_hist(symbol='DE30EUR',exchange='OANDA',interval=Interval.in_5_minute,n_bars=500)
    dax_data=dax_data_5min()
    dax_datacp=dax_data.close.iloc[-1]
    dax_data1=dax_data.tail(20)
    ATR=talib.ATR(dax_data.high,dax_data.low,dax_data.close,timeperiod=20).iloc[-1]
    y1=dax_data1.close.sum()/20
    where=diffadxwma
    if where >=0.2:
        per=40
    else:
        per=42
    real = talib.WMA(dax_data.close, timeperiod=per)
    wma=real.iloc[-1]
    cp=dax_datacp
    # Long
    alpha_long = abs((cp-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data1.close.std()  #### ATR
    p_long = 0.0001
    q_long = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data1.close.std()
    p_short = 1-0.0001
    q_short = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)    
    return cp-q_long,q_short-cp,(wma-q_long),(q_short-wma),(wma-q_long)*(q_short-wma)
#Long_exit_5min, Short_exit_5min, Long_WMA_exit_5min, Short_WMA_exit_5min, Multiply_5min = sl5mindax(diffadxwma)
#print(result1, result2, result3, result4, result5)


#print(sl5mindax())
def sl15mindax(diffadxwma):
    dax_data=dax_data_15min()
    dax_datacp=dax_data.close.iloc[-1]
    dax_data1=dax_data.tail(20)
    ATR=talib.ATR(dax_data.high,dax_data.low,dax_data.close,timeperiod=20).iloc[-1]
    y1=dax_data1.close.sum()/20
    where=diffadxwma 
    if where >=0.2:
        per=40
    else:
        per=42
    real = talib.WMA(dax_data.close, timeperiod=per)
    wma2=real.iloc[-1]
    cp2=dax_datacp
    # Long
    alpha_long = abs((cp2-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data.close.std()  #### ATR
    p_long = 0.001
    q_long2 = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp2-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data1.close.std()
    p_short = 1-0.001
    q_short2 = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)    
    return cp2-q_long2,q_short2-cp2,(wma2-q_long2),(q_short2-wma2),(wma2-q_long2)*(q_short2-wma2)
#Long_exit_15min, Short_exit_15min, Long_WMA_exit_15min, Short_WMA_exit_15min, Multiply_15min = sl15mindax(diffadxwma)
#(cp-q_long),(q_short-cp),(wma-q_long),(q_short-wma),(wma-q_long)*(q_short-wma)=sl5mindax()
def sl30mindax(diffadxwma):
    dax_data=dax_data_30min()
    dax_datacp=dax_data.close.iloc[-1]
    dax_data1=dax_data.tail(20)
    ATR=talib.ATR(dax_data.high,dax_data.low,dax_data.close,timeperiod=20).iloc[-1]
    y1=dax_data1.close.sum()/20
    where=diffadxwma 
    if where >=0.2:
        per=40
    else:
        per=42
    real = talib.WMA(dax_data.close, timeperiod=per)
    wma3=real.iloc[-1]
    cp3=dax_datacp
    # Long
    alpha_long = abs((cp3-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data.close.std()
    p_long = 0.001
    q_long3 = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp3-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data.close.std() #### ATR
    p_short = 1-0.001
    q_short3 = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)
    return cp3-q_long3,q_short3-cp3,(wma3-q_long3),(q_short3-wma3),(wma3-q_long3)*(q_short3-wma3)


def orderbookidTrue():
    total_value = avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get('value')
    return int(avanza.get_positions().get('withOrderbook')[0].get('instrument').get('orderbook').get('id')) if int(total_value) > 20 else 0


def Short_Order_id():
    
    r=avanza.get_watchlists()[2].get('orderbooks')
    i=len(r)
    l=[]
    cu=int()
    #print(r)
    for k in range (0, i):
        z=r=avanza.get_watchlists()[2].get('orderbooks')[k]
        s= avanza.get_warrant_info (str(z)).get("quote").get("sell")
        if s==None:
            cu=0.1
        else:
            cu=avanza.get_warrant_info (str(z)).get("quote").get("sell")                
        l.append((z,cu))       
        l.sort(key=lambda a: a[1]) 
        #print(l)
        #print(r)
    for a in range(0,i):
        if 2.65<l[a][1]:
            return(l[a][0]) 
#print(Short_Order_id())  

def Long_Order_id():
    r=avanza.get_watchlists()[0].get('orderbooks')
    i=len(r)
    l=[]
    cu=int()
    for k in range (0, i):
        z=r=avanza.get_watchlists()[0].get('orderbooks')[k]
        s= avanza.get_warrant_info (str(z)).get("quote").get("sell")
        #if type(s)== "NoneType ":
            #cu=0.1
        #print(z)
        #print(s)
        
        #print(type(s))
        if s == None:
            cu=0.1
        else:
            cu=avanza.get_warrant_info (str(z)).get("quote").get("sell")
        l.append((z,cu))
        l.sort(key=lambda a: a[1])        
    
    for a in range(0,i):
        if 2.65<l[a][1]:
            return(l[a][0]) 



def Long_Order_check():
    r = avanza.get_watchlists()[0].get('orderbooks')
    l = []
    
    for z in r:
        warrant_info = avanza.get_warrant_info(str(z)).get("quote").get("sell")
        cu = 0.1 if warrant_info is None else warrant_info
        l.append((z, cu))
    
    l.sort(key=lambda a: a[1])
    
    for a in range(2):
        if 0.8 > l[a][1]:
            return 1
        else:
            return 0

def Short_Order_check():
    r = avanza.get_watchlists()[2].get('orderbooks')
    l = []
    
    for z in r:
        s = avanza.get_warrant_info(str(z)).get("quote").get("sell")
        cu = 0.1 if s is None else s
        l.append((z, cu))
    
    l.sort(key=lambda a: a[1])

    for a in range(2):
         if 0.8 > l[a][1]:
             return 1
         else:
             return 0

def Long_buy():
    print("here 1")
    l=1.0
    Long_buyl= avanza.get_warrant_info (str((Long_Order_id()))).get("quote").get("sell") + 0.02
    ll= (avanza.get_account_overview(account_number).get('accounts')[2].get('totalValue').get("totalValue").get('value')*l)/Long_buyl
    kl=math.floor(ll)
 
    b=np.format_float_positional(Long_buyl, precision=3, unique=False, fractional=False, trim='k')    
    result= avanza.place_order(str(account_number),str(Long_Order_id()),OrderType.BUY,b,date.fromisoformat(datee),kl)
    
    print("Real long buy",kl,Long_buyl,b)
    
#Long_buy()

def Short_buy():
    
    l=1.0
    Short_buyl= avanza.get_warrant_info (str((Short_Order_id()))).get("quote").get("sell") + 0.02 
    rl= (avanza.get_account_overview(account_number).get('accounts')[2].get('totalValue').get("totalValue").get('value')*l)/Short_buyl
    zl= math.floor(rl)  
    #shortbuy rounding
    b=np.format_float_positional(Short_buyl, precision=3, unique=False, fractional=False, trim='k')
    
    result= avanza.place_order(str(account_number),str(Short_Order_id()),OrderType.BUY,b,date.fromisoformat(datee),zl)

    print("Real short buy",zl,Short_buyl,b)
    #print("here",datetime.now())
#Short_buy()
def Long_sell():
    
    Long_sell= avanza.get_warrant_info (str(orderbookidTrue())).get("quote").get("buy") -0.02
    dax_long=avanza.get_positions().get('withOrderbook')[0].get('volume').get('value')
    #long sell rounding 
    b=np.format_float_positional(Long_sell, precision=3, unique=False, fractional=False, trim='k')
    
    result1= avanza.place_order(str(account_number),str(orderbookidTrue()),OrderType.SELL,b,date.fromisoformat(datee),float(dax_long))
    print("Reeal long sell",dax_long,b)
#Long_sell()
#print (avanza.get_warrant_info (str(orderbookidTrue())).get("quote").get("buy") -0.02)
#print(avanza.get_positions().get('withOrderbook')[0].get('volume').get('value'))
def Short_sell():
    #print("Short_sell")
    Short_sell= avanza.get_warrant_info(str(orderbookidTrue())).get("quote").get("buy") -0.02
    dax_short=avanza.get_positions().get('withOrderbook')[0].get('volume').get('value')
    #short sell
    
    b=np.format_float_positional(Short_sell, precision=3, unique=False, fractional=False, trim='k')
    result= avanza.place_order(str(account_number),str(orderbookidTrue()),OrderType.SELL,b,date.fromisoformat(datee),dax_short)
    print(" Real short sell",dax_short,b)
    

data = pd.read_excel(path_to_data)
df = pd.DataFrame(data, columns=['Trade Number', 'Filled', 'Section', 'Cases', 'Happens Modified 1', 'Happens norm','Happens Modified 2', 'Direction', 'Entry tradingview', 'Entry avanza', 'exit Tradingview', 'Exit avanza', 'Close time', 'Orderbookid', 'Tradingview Sum', 'avanza diff', 'Percent ', 'Win/Loss', 'Sortino average(15)','Sortino average (5)', 'Sortino Drawdown','sortino stdev of drawdown(5)', 'Sortino stdev of drawdown(15)','sortino 5', 'Sortino', 'Sortino (5 Delay)','difference betwee', 'Sortino Difference', 'Previous 5 average sortino dif', 'Fast move(15)', 'Fast move(15) diff 3', 'Fast move 15 diff for 2', 'Fast move(7)', 'Fast move (5 Delay)', 'Fast Difference', 'Test run Modified', 'Drawdown', 'Transfer', 'Test run norm', 'Drawdown norm', 'Test Run Modified 2','Drawdown Modified 2'])
#pd.reset_option("all")
df.fillna(0,inplace=True)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#pd.get_option('display.max_rows', None)

def Trade_number():
    df.loc[(len(df)),['Trade Number']] =df.loc[(len(df)-1),['Trade Number']] +1
    df.fillna(0,inplace=True)
 
def direction():
    try:
        cp = df.loc[(len(df)-1)]["Direction"]
    except:
        cp="no"
    return str(cp)

def Long_add_to_watchlist():
    strings = ["B Longdax sg", "tlng dax vt"]
    Long_watchlist_id = '10045250'
    
    for string in strings:
        try:
            q = avanza.search_for_warrant(string).get('hits')[0].get('topHits')
            for hit in q:
                warrant_id = hit.get('id')
                try:
                    sell_price = avanza.get_warrant_info(warrant_id).get("quote").get("sell")
                except Exception as e:
                    print(f"Error getting sell price for warrant {warrant_id}: {e}")
                    continue
                
                if sell_price is None:
                    cu = 0.1
                else:
                    cu = sell_price
                
                if 1.4 < cu < 4.5:
                    avanza.add_to_watchlist(str(warrant_id), Long_watchlist_id)
        except Exception as e:
            print(f"Error searching for warrant '{string}': {e}")

def Short_add_to_watchlist():
    strings = [" B shrtdax sg","tsrt dax vt"]
    Short_watchlist_id = '10045251'
    
    for string in strings:
        try:
            q = avanza.search_for_warrant(string).get('hits')[0].get('topHits')
            for hit in q:
                warrant_id = hit.get('id')
                try:
                    sell_price = avanza.get_warrant_info(warrant_id).get("quote").get("sell")
                except Exception as e:
                    print(f"Error getting sell price for warrant {warrant_id}: {e}")
                    continue
                
                if sell_price is None:
                    cu = 0.1
                else:
                    cu = sell_price
                
                if 1.4 < cu < 4.5:
                    avanza.add_to_watchlist(str(warrant_id), Short_watchlist_id)
        except Exception as e:
            print(f"Error searching for warrant '{string}': {e}")
   


def Long_Remove_watchlist():
    watchlist_id = '10045250'
    orderbooks = avanza.get_watchlists()[0].get('orderbooks')
    
    for orderbook in reversed(orderbooks[:-1]):  # Iterate in reverse order excluding the last item
        sell_price = avanza.get_warrant_info(str(orderbook)).get("quote").get("sell")
    
        if sell_price is None or sell_price < 1.2 or sell_price > 5.6:
            avanza.remove_from_watchlist(orderbook, watchlist_id)
        
#print(avanza.get_watchlists()[0].get('orderbooks'))
def Short_Remove_watchlist():
    watchlist_id = '10045251'
    orderbooks = avanza.get_watchlists()[2].get('orderbooks')
    
    for orderbook in reversed(orderbooks[:-1]):  # Iterate in reverse order excluding the last item
        sell_price = avanza.get_warrant_info(str(orderbook)).get("quote").get("sell")
    
        if sell_price is None or sell_price < 1.2 or sell_price > 5.6:
            avanza.remove_from_watchlist(orderbook, watchlist_id)


def DataFrame_long_entry_process(diffadxwma,diffprev,changeprevwma,
current_price_5min, Dist_adx_wma,Diff_previous,diff_previous_wma):
   if df.loc[(len(df)-1)]["Filled"]==int(1) :
       Trade_number() 
       print("long tech",datetime.now())
       
       
       section_value = None
       if diffadxwma >= 0:
           if diffprev >= 0:
               section_value = 1 if changeprevwma >= 0 else 1.2
           else:
               section_value = 1.3
       else:
           if diffprev >= 0:
               section_value = 2.1 if changeprevwma >= 0 else 2.2
           else:
               section_value = 2.3 if changeprevwma >= 0 else 3

       print("here2")
       #section_value=1
       df.iat[-1, df.columns.get_loc("Section")] = section_value
       #Dist_adx_wma,Diff_previous,diff_previous_wma,distance=All4hourfunctions()
       if df.iloc[len(df) - 2]["Sortino Difference"] > 0.0:
           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
           df.iloc[len(df) - 1, df.columns.get_loc("Happens norm")] = 1
           

           if Dist_adx_wma > 0:
               if diff_previous_wma > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 6
                   if df.loc[(len(df)-1)]["Section"]< 3:
                       df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                       Long_buy()
               elif Diff_previous > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                   if df.loc[(len(df)-1)]["Section"]< 3:
                       df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                       Long_buy()
               df.loc[(len(df)-1),["Cases"]] =2
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")]=1
                   Long_buy()
               
               
           elif Dist_adx_wma < 0:
               if Diff_previous > 0 and diff_previous_wma > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                   df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                   Long_buy()
               
               elif diff_previous_wma > 0 and Diff_previous < 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                   if df.loc[(len(df)-1)]["Section"]< 2.2:
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                       Long_buy()
                   else: 
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               elif Diff_previous < 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                   if df.loc[(len(df)-1)]["Section"]< 2.2:
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                       Long_buy()
                   else: 
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
                   
               
                   
       else :
          
           if Dist_adx_wma>0 and diff_previous_wma>0:
               
               df.loc[(len(df)-1),["Cases"]]=6
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               if df.loc[(len(df)-1)]["Section"]< 3:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Long_buy()
          
           elif Dist_adx_wma > 0:
                
                if Diff_previous > 0:
                    
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                    if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                        Long_buy()
                else:
                    
                    df.loc[(len(df)-1),["Cases"]] =2
                    if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                        df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                        Long_buy()
                
                
           else :
                
                if Diff_previous > 0 and diff_previous_wma > 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                    if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                        Long_buy()
                
                elif diff_previous_wma > 0 and Diff_previous < 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                    if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                        df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                        Long_buy()
                    
                elif Diff_previous < 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                    if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                        df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                        Long_buy()
                 
           if df.loc[(len(df)-2)]["Fast Difference"]> float(0.0) :
                   
                  #and df.loc[(len(df)-1)]["Section"]==1
                   df.loc[(len(df)-1),["Happens norm"]]=int(1)
                   
       
       print("here3")
       last_row_index = len(df) - 1
       df.loc[last_row_index, "Direction"] = "Lång"
       df.loc[last_row_index, "Entry tradingview"] = current_price_5min
       df.loc[last_row_index, "Entry avanza"] = float(avanza.get_warrant_info(str(Long_Order_id())).get("quote").get("sell"))
       df.loc[last_row_index, "Orderbookid"] = int(Long_Order_id())
       df.to_excel(path_to_data)
       print(df)
       #print(datetime.now())

#DataFrame_long_entry_process()        

def DataFrame_Short_entry_process(diffadxwma,diffprev,changeprevwma,
current_price_5min, Dist_adx_wma,Diff_previous,diff_previous_wma):
   if df.loc[(len(df)-1)]["Filled"]==int(1) :
       Trade_number()
       print("short tech",datetime.now())
       
       section_value = None
       if diffadxwma >= 0:
           if diffprev >= 0:
               section_value = 1 if changeprevwma >= 0 else 1.2
           else:
               section_value = 1.3
       else:
           if diffprev >= 0:
               section_value = 2.1 if changeprevwma >= 0 else 2.2
           else:
               section_value = 2.3 if changeprevwma >= 0 else 3

       df.iat[-1, df.columns.get_loc("Section")] = section_value
       #diff_previous_wma
       if df.iloc[len(df) - 2]["Sortino Difference"] > 0.0:
           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
           df.iloc[len(df) - 1, df.columns.get_loc("Happens norm")] = 1

           if Dist_adx_wma > 0:
               if  diff_previous_wma > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 6
                   if df.loc[(len(df)-1)]["Section"]< 3:
                       df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                       Short_buy()
               elif Diff_previous > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                   if df.loc[(len(df)-1)]["Section"]< 3:
                       df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                       Short_buy()
               df.loc[(len(df)-1),["Cases"]] =2
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")]=1
                   Short_buy()
               
               
           elif Dist_adx_wma < 0:
               if Diff_previous > 0 and  diff_previous_wma > 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                   df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                   Short_buy()
               
               elif  diff_previous_wma > 0 and Diff_previous < 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                   if df.loc[(len(df)-1)]["Section"]< 2.2:
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                       Short_buy()
                   else: 
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               elif Diff_previous < 0:
                   df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                   if df.loc[(len(df)-1)]["Section"]< 2.2:
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                       Short_buy()
                   else: 
                       df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
                   
               
                   
       else :
           if  Dist_adx_wma>0 and  diff_previous_wma>0:
               df.loc[(len(df)-1),["Cases"]]=6
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               if df.loc[(len(df)-1)]["Section"]< 3 :
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Short_buy()

           elif Dist_adx_wma > 0:
                   if Diff_previous > 0:
                       df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                       if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                           Short_buy()
                   else:
                       df.loc[(len(df)-1),["Cases"]] =2
                       if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                           df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                           Short_buy()          
           else:
                   if Diff_previous > 0 and  diff_previous_wma > 0:
                       df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                       if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                           Short_buy()
                   
                   elif  diff_previous_wma > 0 and Diff_previous < 0:
                       df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                       if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                           df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                           Short_buy()
                       
                   elif Diff_previous < 0:
                       df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                       if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                           df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                           df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                           Short_buy()
                 
           if df.loc[(len(df)-2)]["Fast Difference"]> float(0.0) :
                  #and df.loc[(len(df)-1)]["Section"]==1
                   df.loc[(len(df)-1),["Happens norm"]]=int(1)

       
       short_order_id_value = Short_Order_id()
       last_row_index = len(df) - 1 
       df.iloc[last_row_index, df.columns.get_loc("Direction")] = "Kort"
       df.iloc[last_row_index, df.columns.get_loc("Entry tradingview")] = current_price_5min       
       avanza_info = avanza.get_warrant_info(str(short_order_id_value))
       df.iloc[last_row_index, df.columns.get_loc("Entry avanza")] = avanza_info.get("quote").get("sell")
       df.iloc[last_row_index, df.columns.get_loc("Orderbookid")] = int(short_order_id_value)
       df.to_excel(path_to_data)
       print(df)
       #print(datetime.now())

def DataFrame_Exit_process(current_price_5min):
        
    if df.loc[(len(df)-1)]["Filled"]==int(0) :
        
        if df.loc[(len(df)-1)]["Happens Modified 2"]==int(1):
            
            if  float(avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get("value"))>=(1) and int(10)>=float(avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value'))>=int(-10) and direction() =="Lång":
                #direction() =="Lång" and current_positions()>10 and
                Long_sell()
            elif float(avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get("value"))>=(1) and int(10)>=float(avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value'))>=int(-10) and direction()=="Kort":
                #direction()=="Kort" and current_positions()>10 and
                Short_sell()
                
        
        print("Exits",datetime.now())
        
        if df.loc[(len(df)-1)]["Entry tradingview"]!= 0 and df.loc[(len(df)-1)]['exit Tradingview']== 0:
            
            df.loc[(len(df)-1),['exit Tradingview']]= current_price_5min
            
            df.loc[(len(df)-1),["Exit avanza"]] = avanza.get_warrant_info (str(int(df["Orderbookid"][(len(df)-1)]))).get("quote").get("buy")
            # data processing 
            df.loc[(len(df)-1),["avanza diff"]]= float(df.loc[(len(df)-1),["Exit avanza"]])-float(df.loc[(len(df)-1),["Entry avanza"]])
            df.loc[(len(df)-1),['Percent ']]=float(1)+float(df.loc[(len(df)-1),["avanza diff"]])/float(df.loc[(len(df)-1),["Entry avanza"]])
            #Just some differencs and acount keeping
            if df.loc[(len(df)-1)]["avanza diff"]>=0:
                df.loc[(len(df)-1),['Win/Loss']]=int(1)
            else:
                df.loc[(len(df)-1),['Win/Loss']]=int(0)
            if df.loc[(len(df)-1)]["Direction"]=="Lång":
                df.loc[(len(df)-1),["Tradingview Sum"]]=float(df.loc[(len(df)-1),["exit Tradingview"]])-float(df.loc[(len(df)-1),["Entry tradingview"]])
            else:
                df.loc[(len(df)-1),["Tradingview Sum"]]=float(df.loc[(len(df)-1),["Entry tradingview"]])-float(df.loc[(len(df)-1),["exit Tradingview"]])
            
            
            #Filled add as many as you want
            if df.loc[(len(df)-1)]["Entry tradingview"]!= 0 and df.loc[(len(df)-1)]["Tradingview Sum"]!= 0 and df.loc[(len(df)-1)]["avanza diff"]!= "no" :
                df.loc[(len(df)-1),["Filled"]]=int(1)
            else:
                df.loc[(len(df)-1),["Filled"]]=int(0)
            #trade happen
            
            #SORTINO STUff
            df["Sortino average(15)"]=df['Percent '].rolling(15,center=False).mean()
             #"Sortino average(15)"
            if df.loc[(len(df)-1)]['Percent ']<=float(1.00):
                df.loc[(len(df)-1),["Sortino Drawdown"]]= float(1)-float(df.loc[(len(df)-1),['Percent ']])
            else:
                df.loc[(len(df)-1),["Sortino Drawdown"]]= int(0)
                
            df["Sortino stdev of drawdown(15)"]=df["Sortino Drawdown"].rolling(15,center=False).std()
            a=float(df.loc[(len(df)-1),["Sortino stdev of drawdown(15)"]])
            b=float(df.loc[(len(df)-1),["Sortino average(15)"]])
           
            df.loc[(len(df)-1),["Sortino"]]=float((b-1)/a)
            df["Sortino"] = pd.to_numeric(df["Sortino"])
            df['Sortino (5 Delay)']=df["Sortino"].rolling(5,center=False).mean()
            #Sordino difference
            df.loc[(len(df)-1),["Sortino Difference"]]= df.loc[(len(df)-1)]["Sortino"]-df.loc[(len(df)-1)]['Sortino (5 Delay)']
            df['Previous 5 average sortino dif']=df["Sortino Difference"].rolling(3,center=False).mean()
            
            # moving averages
            df["Fast move(15)"]=df['Win/Loss'].rolling(14,center=False).mean()
            df["Fast move(7)"]=df['Win/Loss'].rolling(7,center=False).mean()
            df["Fast move (5 Delay)"]=df["Fast move(7)"].rolling(5,center=False).mean()
            df["Fast move(15) diff 3"]=df["Fast move(15)"].rolling(3,center=False).mean()
            df['Fast move 15 diff for 2']=df["Fast move(15)"].rolling(2,center=False).mean()
            df.loc[(len(df)-1),["Fast Difference"]]= float(df.loc[(len(df)-1),["Fast move(7)"]])-float(df.loc[(len(df)-1),["Fast move (5 Delay)"]])
           #test run and draw down modified 2
            if df.loc[(len(df)-1)]['Happens Modified 2']==int(1):
               df.loc[(len(df)-1),[ 'Test Run Modified 2']]= float(df.loc[(len(df)-1),['Percent ']]-0.008)*float(df.loc[(len(df)-2),['Test Run Modified 2']])
            else:
               df.loc[(len(df)-1),['Test Run Modified 2']]=df.loc[(len(df)-2),['Test Run Modified 2']]
           
            df['Drawdown Modified 2'] = (df['Test Run Modified 2'] - df['Test Run Modified 2'].cummax())/df['Test Run Modified 2'].cummax()
           
            
            #Test runs and drawdowns modified
            if df.loc[(len(df)-1)]['Happens Modified 1']==int(1):
                df.loc[(len(df)-1),[ 'Test run Modified']]= float(df.loc[(len(df)-1),['Percent ']]-0.008)*float(df.loc[(len(df)-2),['Test run Modified']])
            else:
                df.loc[(len(df)-1),['Test run Modified']]=df.loc[(len(df)-2),['Test run Modified']]
            
            df['Drawdown'] = (df['Test run Modified'] - df['Test run Modified'].cummax())/df['Test run Modified'].cummax()
            
            #Testrun drawdown normal
            if df.loc[(len(df)-1)]['Happens norm']==int(1):
                df.loc[(len(df)-1),[ 'Test run norm']]= float(df.loc[(len(df)-1),['Percent ']]-0.008)*float(df.loc[(len(df)-2),['Test run norm']])
            else:
                df.loc[(len(df)-1),['Test run norm']]=df.loc[(len(df)-2),['Test run norm']]
            
            df['Drawdown norm'] = (df['Test run norm'] - df['Test run norm'].cummax())/df['Test run norm'].cummax()
            # Transfer
            
            if df.loc[(len(df)-1)]["Sortino Difference"]<df.loc[(len(df)-1)]['Previous 5 average sortino dif'] and df.loc[(len(df)-1)]["Fast Difference"]>0 and df.loc[(len(df)-1)]["Fast move (5 Delay)"]>=0.6 and df.loc[(len(df)-1)]["Fast move(15)"]< df.loc[(len(df)-1)]["Fast move(7)"] :
                df.loc[(len(df)-1),['Transfer']]=int(1)
            else:
                df.loc[(len(df)-1),['Transfer']]=int(0)
                
                
            
            ####drawdown and transfer warning
            if df.loc[(len(df)-1)]['Drawdown norm']<=-0.68:
                 print("drawdown < -0.68, optimal time to put money in")
            if df.loc[(len(df)-1)]["Transfer"]==int(1):
                 print("Transfer 0.75 to different acount, keep 0.25 in play. 0.25 profit, and at drawdown warning 0.25, 0.5 of remaining into play")
 
        #to excell
            df.loc[(len(df)-1),['Close time']]= datetime.now()
            print("exit complete")
            df.to_excel(path_to_data)
            print(df)


def Current_time():
    t = time.localtime()
    current_time = time.strftime("%H%M", t)
    return float(current_time)




#df.drop(index=df.index[-1], axis=0, inplace=True) 
#df.to_excel(path_to_data)

Long_add_to_watchlist()
Short_add_to_watchlist()
Long_Remove_watchlist()
Short_Remove_watchlist()
#print(df)
#adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate=ALL3minfunctions()
#True_Ratio, ATR15min,rma=All15minfunctions()
#Dist_adx_wma,Diff_previous,diff_previous_wma,distance=All4hourfunctions()
#Exception_exit, avg, sma, wma,smalow,wmalow,smalow2,wmalow2,current_price_5min= All5minfunctions()
#adx1h,diffadxwma,diffprev,changeprevwma = All1hourfunctions()
#DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
#DataFrame_Exit_process(current_price_5min)
print(df)
#adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate=ALL3minfunctions()

while True:
    try:
        while True:
            #dax_data3=tv.get_hist(interval=Interval.in_3_minute,n_bars=200)
            account_number=9651099
            #surge_protection=surge_protection()
            numb_o_ord=avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value')
            current_positions = avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get("value")
            condition=90
            
            if  df.loc[(len(df)-1)]["Filled"]==int(1) and 802.0<=Current_time()<2158.0 :
                adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate=ALL3minfunctions()
                #print(adx47,adxdif,cur,current_price,surge, surge_protection,surge_sma,Exception_entry,Recalibrate)
                Exception_exit, avg, sma, wma,smalow,wmalow,smalow2,wmalow2,current_price_5min= All5minfunctions()
                adx1h,diffadxwma,diffprev,changeprevwma = All1hourfunctions()
                True_Ratio, ATR15min,rma=All15minfunctions()
                Dist_adx_wma,Diff_previous,diff_previous_wma,distance=All4hourfunctions()
                #print(current_positions)
                if surge_protection<=1.0 and surge_sma<=1.0:
                    
                    if current_positions<10  and diffadxwma<=-0.1 and surge_protection<=1.0 and surge_sma<=1.0 and 10>=numb_o_ord>=-10 and Exception_entry>=1.8 and 9.8<= adxdif<30 and  adx47<30 and True_Ratio >=0.0  and (avg-2 >sma) and (avg-2 >wma):
                        
                        Long_orderbookId1= Long_Order_id()           
                        Short_orderbookId1= Short_Order_id()
                        if 10<=cur<=300 :
                            DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma) 
                        elif -10>=cur>=-300 :
                            DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                    elif current_positions<10 and surge_protection<=1.0 and surge_sma<=1.0 and surge<=20.000 and diffadxwma>=-0.1 :
                        
                        Long_exit_15min, Short_exit_15min, Long_WMA_exit_15min, Short_WMA_exit_15min, Multiply_15min = sl15mindax(diffadxwma)
                        Long_orderbookId1= Long_Order_id()           
                        Short_orderbookId1= Short_Order_id()
                        if adx1h<21:
                            if 10<= adxdif<30 and adx47<30 and True_Ratio>0.00 :                  
                                
                                if 150<= cur<=310 and Long_WMA_exit_15min>0.00 and Long_exit_15min<=condition :
                                    DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                elif -150>= cur>=-310 and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition:
                                    DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                        elif 21<=adx1h <32 :              
                            if 10<= adxdif<=30 and  adx47<=30.00 and True_Ratio>=0.00 and (sma>=0) and (wma>=0 ) and (avg-2 >sma) and (avg-2 >wma):
                                
                                if 10<=cur<=300 and Long_WMA_exit_15min>0.00 and Long_exit_15min<=condition:
                                   DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                elif -10>=cur>=-300 and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition:
                                   DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma) 
                            if 1<= adxdif<=30  and 20.000<=adx47<=30.00 and True_Ratio>=0.0 and (sma>=0) and (wma>=0 ) and (avg-2 >sma) and (avg-2 >wma) :
                                if Long_WMA_exit_15min>0.00 and 10<=cur<=300 and Long_exit_15min<=condition:
                                    DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                elif -10>= cur>=-300 and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition:
                                    DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                            if True_Ratio>=1.5:
                                if 1<= adxdif  and 20.00<=adx47 :
                                    
                                    if 10<=cur and  Long_WMA_exit_15min>0.00 and Long_exit_15min<=condition:
                                        DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                    elif -10>=cur and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition:
                                        DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)                    
                        elif adx1h>=32 :
                                if 10<= adxdif<30  and adx47<=30 and True_Ratio>=0.0 and smalow2>=1:
                                    
                                    #print(Long_exit_15min)
                                    if 10<=cur<=300 and Long_WMA_exit_15min>0.00 and Long_exit_15min<=condition:
                                        
                                        DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                    elif -10>=cur>=-300 and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition :
                                        DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)    
                                if 1<= adxdif<30 and 20<=adx47<=30 and True_Ratio>=0.0  and smalow2>=1 :
                                    
                                    if 10<=cur<=300 and Long_WMA_exit_15min>0.00 and Long_exit_15min<=condition:
                                        DataFrame_long_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                                    elif -10>=cur>=300 and Short_WMA_exit_15min>0.00 and Short_exit_15min<=condition:
                                        DataFrame_Short_entry_process(diffadxwma, diffprev, changeprevwma, current_price_5min, Dist_adx_wma, Diff_previous, diff_previous_wma)
                if Recalibrate>90:
                     if surge_protection>=1.0 or surge_sma>=1.0:
                         if Long_Order_check()>0 or Short_Order_check()>0:
                             Long_add_to_watchlist()
                             Short_add_to_watchlist()
                             Long_Remove_watchlist()
                             Short_Remove_watchlist()
            elif df.loc[(len(df)-1)]["Filled"]==int(0) :
                True_Ratio, ATR15min,rma=All15minfunctions()
                
                adx1h,diffadxwma,diffprev,changeprevwma = All1hourfunctions()
                
                Exception_exit, avg, sma, wma,smalow,wmalow,smalow2,wmalow2,current_price_5min= All5minfunctions()
                Long_exit_5min, Short_exit_5min, Long_WMA_exit_5min, Short_WMA_exit_5min, Multiply_5min = sl5mindax(diffadxwma)
               
                Long_exit_15min, Short_exit_15min, Long_WMA_exit_15min, Short_WMA_exit_15min, Multiply_15min = sl15mindax(diffadxwma)
                Long_exit_30min, Short_exit_30min, Long_WMA_exit_30min, Short_WMA_exit_30min, Multiply_30min = sl30mindax(diffadxwma)
                if Current_time()>=2158.0: 
                   print("Time constraint exit")
                   DataFrame_Exit_process(current_price_5min) 
                if Exception_exit<=0:
                    if direction()=="Lång":
                        if adx1h<48 :
                            if Long_exit_5min<0.0:
                                DataFrame_Exit_process(current_price_5min)
                            elif Long_WMA_exit_5min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 5 Min")
                        elif 48<=adx1h :
                            if Long_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Long_WMA_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 15 Min")      
                    elif direction()=="Kort":
                        if adx1h<48  :
                            if Short_exit_5min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Short_WMA_exit_5min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 5 Min")
                        elif 48<=adx1h :
                            if Short_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Short_WMA_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 15 Min")  
                if True_Ratio< 1.0:    
                    if direction()=="Lång":
                        if  Long_exit_5min<0.00 :
                            DataFrame_Exit_process(current_price_5min)
                        elif  Long_WMA_exit_5min<0.00 :
                            DataFrame_Exit_process(current_price_5min)
                            print("WMA 5 Min")                       
                    elif direction()=="Kort" :
                        if  Short_exit_5min<0.00 :
                            DataFrame_Exit_process(current_price_5min)
                        elif Short_WMA_exit_5min<0.00:
                            DataFrame_Exit_process(current_price_5min)
                            print("WMA 5 Min")
                if True_Ratio>=1.0 :
                    if direction()=="Lång" : #orderbookidTrue()==Long_orderbookId1 :
                        if adx1h<18:
                            if  Long_exit_5min<0.00 :
                                DataFrame_Exit_process(current_price_5min)
                            elif  Long_WMA_exit_5min<0.00 :
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 5 Min")
                        if 18 <= adx1h<48 :
                            if Long_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Long_WMA_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 15 Min")
                        elif adx1h>=48 :
                            if Long_exit_30min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Long_WMA_exit_30min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 30 Min")   
                    elif direction()=="Kort":
                        if adx1h<18 :
                            if  Short_exit_5min<0.00 :
                                DataFrame_Exit_process(current_price_5min)
                            elif Short_WMA_exit_5min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 5 Min")         
                        if 18<=adx1h<48 :
                            if Short_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Short_WMA_exit_15min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 15 Min")  
                        elif adx1h>=48 :
                            if Short_exit_30min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                            elif Short_WMA_exit_30min<0.00:
                                DataFrame_Exit_process(current_price_5min)
                                print("WMA 30 Min")                     
            
            time.sleep(5)
            #print(surge_protection()[0])
            #print("hi",datetime.now())
    except Exception as e:
        # If an error occurs, log the error and sleep for a bit
        print(f"Error: {e}",datetime.now())
        #print(ADX1hSMA()[0])
        time.sleep(5)

