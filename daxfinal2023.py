# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:19:45 2022

@author: herma
"""


import time
import numpy as np
import pandas as pd
from maintv import TvDatafeed,Interval

import sympy
import math
from datetime import datetime
from sympy import solve, Symbol, nsolve,pi
import time
import talib
from avanza import Avanza,OrderType,InstrumentType
from avanza import Avanza,OrderType,InstrumentType
import datetime
import hashlib
import pyotp
from scipy.stats import skewnorm
import numpy as np
from datetime import datetime
from datetime import date
import warnings

warnings.simplefilter(action="ignore",category= FutureWarning)
#import matplotlib.pyplot as plt

#totp = pyotp.TOTP("HGR5JY7LUORXDYNM5IYAZ6A6S7PHCWVE", digest=hashlib.sha1)
#print(totp.now())


avanza = Avanza({
    'username': 'Herman_Roberth',
    'password': 'Sweetheart123',
    'totpSecret': 'HGR5JY7LUORXDYNM5IYAZ6A6S7PHCWVE'
})



tv = TvDatafeed()
account_number=9651099
path_to_data=r'C:\Users\herma\Desktop\collected data try 123 (1).xlsx'

datee='2024-01-14'
Is_Real_off= "YESS ACTUALL MONEY"   

symbolD= 'DE30EUR' #'GRXEUR' 
exchangeD= 'OANDA' #'FOREXCOM'

#######VIX
symbolDVIX= 'VIX' 
exchangeDVIX='PEPPERSTONE' 

symbolDAXVIX= 'FVS1!' 
exchangeDAXVIX='EUREX' 

#dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
# DAX EVERYTHING
#print(dax_data)
def ADXExtream42():

    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
    #df = data.copy()
    #alpha = 1/12
    
    df = dax_data
    alpha = 1/42

    # TR
    df['H-L'] = df['high'] - df['low']
    df['H-C'] = np.abs(df['high'] - df['close'].shift(1))
    df['L-C'] = np.abs(df['low'] - df['close'].shift(1))
    df['TR'] = df[['H-L', 'H-C', 'L-C']].max(axis=1)
    del df['H-L'], df['H-C'], df['L-C']

    # ATR
    df['ATR'] = df['TR'].ewm(alpha=alpha, adjust=False).mean()

    # +-DX
    df['H-pH'] = df['high'] - df['high'].shift(1)
    df['pL-L'] = df['low'].shift(1) - df['low']
    df['+DX'] = np.where(
        (df['H-pH'] > df['pL-L']) & (df['H-pH']>0),
        df['H-pH'],
        0.0
    )
    df['-DX'] = np.where(
        (df['H-pH'] < df['pL-L']) & (df['pL-L']>0),
        df['pL-L'],
        0.0
    )
    del df['H-pH'], df['pL-L']

    # +- DMI
    df['S+DM'] = df['+DX'].ewm(alpha=alpha, adjust=False).mean()
    df['S-DM'] = df['-DX'].ewm(alpha=alpha, adjust=False).mean()
    df['+DMI'] = (df['S+DM']/df['ATR'])*100
    df['-DMI'] = (df['S-DM']/df['ATR'])*100
    del df['S+DM'], df['S-DM']

    # ADX
    df['DX'] = (np.abs(df['+DMI'] - df['-DMI'])/(df['+DMI'] + df['-DMI']))*100
    df['ADX'] = df['DX'].ewm(alpha=alpha, adjust=False).mean()
    return (df["ADX"])
#print(ADXExtream42())
def ADX47():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
    try:
        real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=42)
        a=real[4999]
    except:
        #time.sleep(5)
        pass
    
    return a
#print(ADX47())
def ADXdif():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
    try:
        real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=42)
        a=(real[4999]- real[4998])*50
    except:
        #time.sleep(5)
        pass
    
    return a
#print(ADXdif())
def macd():    
    
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=70)
        
    exp1 = dax_data.close.ewm(span=12, adjust=False).mean()
    exp2 = dax_data.close.ewm(span=26, adjust=False).mean()    
    macd = exp1-exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()    
    tot=(macd+exp3).tail(1)    
    df=pd.concat([tot],axis=1)
    Tot=np.max(df,axis=1).sum()
    
    return Tot


def CCI70():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=1)
    dax_data40=tv.get_hist(symbol=symbolD,exchange= exchangeD,interval=Interval.in_3_minute,n_bars=40)
    dax_data70=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=70)
    
  
    y40=((dax_data40.high+ dax_data40.low+dax_data40.close)/3).mean()    
    z70=((dax_data70.high+ dax_data70.low+dax_data70.close)/3).mean()    
    hlc370=(dax_data70.high+ dax_data70.low+dax_data70.close)/3   
    hlc3=(dax_data.high+ dax_data.low+dax_data.close)/3
    cci=(((hlc3)-y40))/(np.abs(((hlc370)-z70)).mean()*0.015)
    df=pd.concat([cci],axis=1)
    cur=np.max(df,axis=1).sum()
    #[0] -cci
    #[1] -cci ma
    
    return cur
#print(CCI70())
def ADXExtrean1hour():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=5000)
    #df = data.copy()
    #alpha = 1/12
    
    df = dax_data
    alpha = 1/12

    # TR
    df['H-L'] = df['high'] - df['low']
    df['H-C'] = np.abs(df['high'] - df['close'].shift(1))
    df['L-C'] = np.abs(df['low'] - df['close'].shift(1))
    df['TR'] = df[['H-L', 'H-C', 'L-C']].max(axis=1)
    del df['H-L'], df['H-C'], df['L-C']

    # ATR
    df['ATR'] = df['TR'].ewm(alpha=alpha, adjust=False).mean()

    # +-DX
    df['H-pH'] = df['high'] - df['high'].shift(1)
    df['pL-L'] = df['low'].shift(1) - df['low']
    df['+DX'] = np.where(
        (df['H-pH'] > df['pL-L']) & (df['H-pH']>0),
        df['H-pH'],
        0.0
    )
    df['-DX'] = np.where(
        (df['H-pH'] < df['pL-L']) & (df['pL-L']>0),
        df['pL-L'],
        0.0
    )
    del df['H-pH'], df['pL-L']

    # +- DMI
    df['S+DM'] = df['+DX'].ewm(alpha=alpha, adjust=False).mean()
    df['S-DM'] = df['-DX'].ewm(alpha=alpha, adjust=False).mean()
    df['+DMI'] = (df['S+DM']/df['ATR'])*100
    df['-DMI'] = (df['S-DM']/df['ATR'])*100
    del df['S+DM'], df['S-DM']

    # ADX
    df['DX'] = (np.abs(df['+DMI'] - df['-DMI'])/(df['+DMI'] + df['-DMI']))*100
    df['ADX'] = df['DX'].ewm(alpha=alpha, adjust=False).mean()
    return (df["ADX"])
#print(ADX()[4999])
def ADX1h():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=4000)
    #b=dax_data.high
    try:
        real = talib.ADX(dax_data.high , dax_data.low, dax_data.close, timeperiod=12)
        a=real[3999]
    except:
        time.sleep(2)
        a=ADXExtrean1hour()   
    
    
    return a
#print(ADX1h())
def ADXLongtrend():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_4_hour,n_bars=1000)

    real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=50)
    a=real[999]
    b=talib.WMA(real,timeperiod=25)[999]
    c=a-b
    
    q=real-real.shift(1)
    d=q[999]
    
    
    wma=talib.WMA(q, timeperiod=30)[999]
    diff=d-wma
    
    
    
    return c,d,diff

#print(ADXLongtrend())


def ADX1hSMA():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=4000)

    real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=12)
    a=real[3999]
    b=talib.WMA(real,timeperiod=12)[3999]
    c=a-b
    #d=real[3999]-real[3998]
    
    
    
    q=real-real.shift(1)
    d=q[3999]
    
    
    wma=talib.WMA(q, timeperiod=12)[3999]
    diff=d-wma
   
   
    return c,d,diff
#dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=4000)
#print(dax_data)
#print(ADX1hSMA())

def current_price():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
    return dax_data.close.sum()
#print(current_price())
def sl5mindax():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_5_minute,n_bars=20)
    dax_data37=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_5_minute,n_bars=5000)
    dax_datacp=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
    ATR=talib.ATR(dax_data37.high,dax_data37.low,dax_data37.close,timeperiod=20)[4999]
    y1=dax_data.close.sum()/20
    #WMA
    dax_data_adx=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=5000)    
    
    
    try:
        adx=talib.ADX(dax_data_adx.high,dax_data_adx.low,dax_data_adx.close,timeperiod=12)        
    except:
        #time.sleep(5)
        pass
    where=(adx[4999]-adx[4998])
    if where >=0.2:
        per=40
    else:
        per=42
    
    real = talib.WMA(dax_data37.close, timeperiod=per)
    wma=real[4999]
    #Curent price
    cp=dax_datacp.close.sum()
    # Long
    alpha_long = abs((cp-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data.close.std()  #### ATR
    p_long = 0.0001
    q_long = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data.close.std()
    p_short = 1-0.0001
    q_short = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)    
    return cp-q_long,q_short-cp,(wma-q_long),(q_short-wma),(wma-q_long)*(q_short-wma)

def sl15mindax():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_15_minute,n_bars=20)
    dax_data37=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_15_minute,n_bars=5000)
    dax_datacp=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
    ATR=talib.ATR(dax_data37.high,dax_data37.low,dax_data37.close,timeperiod=20)[4999]
    y1=dax_data.close.sum()/20
    #WMA
    dax_data_adx=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=5000)    
    try:
        adx=talib.ADX(dax_data_adx.high,dax_data_adx.low,dax_data_adx.close,timeperiod=12)    
    except:
        #time.sleep(5)
        pass
    where=(adx[4999]-adx[4998])
    if where >=0.2:
        per=40
    else:
        per=42
    
    real = talib.WMA(dax_data37.close, timeperiod=per)
    wma=real[4999]
    #Curent price
    cp=dax_datacp.close.sum()
    # Long
    alpha_long = abs((cp-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data.close.std()  #### ATR
    p_long = 0.001
    q_long = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data.close.std()
    p_short = 1-0.001
    q_short = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)    
    return cp-q_long,q_short-cp,(wma-q_long),(q_short-wma),(wma-q_long)*(q_short-wma)


def sl30mindax():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_30_minute,n_bars=20)
    dax_data37=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_30_minute,n_bars=5000)
    dax_datacp=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
    ATR=talib.ATR(dax_data37.high,dax_data37.low,dax_data37.close,timeperiod=20)[4999]
    y1=dax_data.close.sum()/20    
    #WMA
    dax_data_adx=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=5000)    
    #adx=talib.ADX(dax_data_adx.high,dax_data_adx.low,dax_data_adx.close,timeperiod=12)    
    try:
        adx=talib.ADX(dax_data_adx.high,dax_data_adx.low,dax_data_adx.close,timeperiod=12)    
    except:
        #time.sleep(5)
        pass
    where=(adx[4999]-adx[4998])
    if where >=0.2:
        per=40
    else:
        per=42    
    real = talib.WMA(dax_data37.close, timeperiod=per)
    wma=real[4999]
    #Curent price
    cp=dax_datacp.close.sum()
    # Long
    alpha_long = abs((cp-y1)/ATR)
    mu_long = y1
    sigma_long = dax_data.close.std()
    p_long = 0.001
    q_long = skewnorm.ppf(p_long, alpha_long, loc=mu_long, scale=sigma_long)
    
    #short    
    alpha_short = -abs((cp-y1)/ATR)
    mu_short = y1
    sigma_short= dax_data.close.std() #### ATR
    p_short = 1-0.001
    q_short = skewnorm.ppf(p_short, alpha_short, loc=mu_short, scale=sigma_short)
    return cp-q_long,q_short-cp,(wma-q_long),(q_short-wma),(wma-q_long)*(q_short-wma)

def Exception_exit():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_5_minute,n_bars=5000)
   
    a=talib.STDDEV(dax_data.close, timeperiod=50)
    c=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=50)
    #c=b.ema(alpha=1/22).mean()[4999]
    
    #c=talib.WMA(b,timeperiod=22)[4999]
    h=a/c
    
    h=(a/c)
    d=talib.WMA(h,timeperiod=25)[4999]
    
    return h[4999]-d

def True_Ratio():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_15_minute,n_bars=5000)
   
    #d=talib.EMA(dax_data.high,timeperiod=22)
    #e=talib.EMA(dax_data.low,timeperiod=22)
    #f=talib.EMA(dax_data.close,timeperiod=22)
    #talib.ATR(high, low, close)
    
    
    a=talib.STDDEV(dax_data.close, timeperiod=22)[4999]
    b=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    #c=b.ema(alpha=1/22).mean()[4999]
    
    c=talib.WMA(b,timeperiod=22)[4999] 
    h=a/c
    
    return h

def Exception_entry():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
    a=talib.STDDEV(dax_data.close, timeperiod=50)[4999]
    b=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    #c=b.ema(alpha=1/22).mean()[4999]
    
    c=talib.WMA(b,timeperiod=50)[4999] 
    h=a/c
    
    return h

#print(Exception_entry())
def rma():
    
   
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_15_minute,n_bars=5000)
   
    d=talib.EMA(dax_data.high,timeperiod=22)
    e=talib.EMA(dax_data.low,timeperiod=22)
    f=talib.EMA(dax_data.close,timeperiod=22)
    #talib.ATR(high, low, close)
    
    
    a=talib.STDDEV(dax_data.close, timeperiod=22)[4999]
    b=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=1)
    
    c=talib.SMA(b,timeperiod=22)[4999]
    h=a/c
    return h
#print(rma())

#################################


def DI():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_5_minute,n_bars=5000)
    Minus= talib.MINUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    Plus= talib.PLUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    a=(Minus[4999]+Plus[4999])
    b=a.sum()/2
    try:
        adx = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=32)
    except:
        time.sleep(5)
        pass
    sma=talib.SMA(adx,timeperiod=75)[4999]
    wma=talib.WMA(adx,timeperiod=75)[4999]
    smalow=talib.SMA(adx,timeperiod=10)[4999]
    wmalow=talib.WMA(adx,timeperiod=10)[4999]
    #[0] _DI average
    #[1] - SMA adx average
    #[2] - WMA adx average
    return b,sma,wma,smalow,wmalow


def DILow():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_5_minute,n_bars=5000)
    Minus= talib.MINUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    Plus= talib.PLUS_DI(dax_data.high, dax_data.low,dax_data.close,timeperiod=32)
    a=(Minus[4999]+Plus[4999])
    b=a.sum()/2
    
    try:
        adx = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=32)
    except:
        time.sleep(5)
        pass
    smalow=talib.SMA(adx,timeperiod=38)[4999]
    wmalow=talib.WMA(adx,timeperiod=38)[4999]
    
    #[0] _DI average
    #[1] - SMA adx average
    #[2] - WMA adx average
    return b,smalow,wmalow



#print(ADX1hSMA())

def Surge():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=4000)
    b=dax_data.high
    real=talib.ATR(b, dax_data.low, dax_data.close,timeperiod=14)
    
    a=real[3999]
    return a
def surge_protection():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=5000)
    b=dax_data.high
    atr=talib.ATR(b, dax_data.low, dax_data.close,timeperiod=14)
    stdev=talib.STDDEV(dax_data.close, timeperiod=14)
    surge=((stdev[4999]/atr[4999])-(stdev[4998]/atr[4998]))*10/(stdev[4998]/atr[4998])
    
    sma_atr=talib.SMA(atr,timeperiod=6)
    sma_stdev=talib.SMA(stdev,timeperiod=6)
    #ll=(sma_stdev[-1]/sma_atr[1])
    surge_sma=((sma_stdev[-1]/sma_atr[-1])-(sma_stdev[-2]/sma_atr[-2]))*10/(sma_stdev[-2]/sma_atr[-2])

   
    return surge, surge_sma
#print(surge_protection())
#print(surge_protection()[0]<=1.0 and surge_protection()[1]<=1.0)
#print(ADX1h())
#print(Surge())


def ATR15min():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_15_minute,n_bars=5000)
    a=talib.ATR(dax_data.high, dax_data.low, dax_data.close,timeperiod=20)[4999]
    return a
#print(ATR15min())

#######vix

#print(sl15mindax())
#######CHeck AVANZA:get Poistions
def orderbookidTrue():
    x=avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get('value')
    if int(x)>20:
            k=avanza.get_positions().get('withOrderbook')[0].get('instrument').get('orderbook').get('id')
            return int(k)
            
    else:
        return 0
    
        
#print(orderbookidTrue())
#orderbookidTrue()
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
#print(Long_Order_id())
def Long_Order_check():
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
    
    for a in range(0,2):
        if 0.8>l[a][1]:
            return(1)
        else:
            return(0)
        
def Short_Order_check1():
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
    for a in range(0,2):
        if  0.8>l[a][1]:
            return(1)
        else:
            return (0)

#print(Long_Order_id())
"""
def direction():
    try:
        cp = avanza.get_warrant_info(str(df["Orderbookid"][len(df)-1])).get('keyIndicators').get("direction")
    except:
        cp="no"
    return str(cp)
"""
#if current_positions<10 and ADX1hSMA()>=-0.5 and numb_o_ord==0 and Exception_entry()>=1.80 and 9.8<= ADXdif()<28 and  ADX47()<28 and True_Ratio()>=0.60  and (DI()[0]-2 >DI()[1]) and (DI()[0]-2 >DI()[2]):
    


#print(ADX1hSMA(),CCI70(), Exception_entry(),ADXdif(),ADX47(), True_Ratio(),DI()[0]-2,DI()[1]-2)
def Long_buy():
    
    l=1.0
    Long_buyl= avanza.get_warrant_info (str((Long_Order_id()))).get("quote").get("sell") + 0.02
    ll= (avanza.get_account_overview(account_number).get('accounts')[2].get('totalValue').get("totalValue").get('value')*l)/Long_buyl
    kl=math.floor(ll)
    
# Longbuy
#avanza.get_account_overview(account_number).get('buyingPower')
    b=np.format_float_positional(Long_buyl, precision=3, unique=False, fractional=False, trim='k')    
    #result= avanza.place_order(str(account_number),str(Long_Order_id()),OrderType.BUY,b,date.fromisoformat(datee),kl)
    
    print("Real long buy",kl,Long_buyl,b)
#Long_buy()

def Short_buy():
    
    l=1.0
    #Short_buyl= avanza.get_warrant_info (str((Short_Order_id()))).get("quote").get("sell") + 0.02 
    #rl= (avanza.get_account_overview(account_number).get('accounts')[2].get('totalValue').get("totalValue").get('value')*l)/Short_buyl
    #zl= math.floor(rl)  
    #shortbuy rounding
    #b=np.format_float_positional(Short_buyl, precision=3, unique=False, fractional=False, trim='k')
    
    #result= avanza.place_order(str(account_number),str(Short_Order_id()),OrderType.BUY,b,date.fromisoformat(datee),zl)
   
    
    #print("Real short buy",zl,Short_buyl,b)
    print("here",datetime.now())
#Short_buy()
def Long_sell():
    
    Long_sell= avanza.get_warrant_info (str(orderbookidTrue())).get("quote").get("buy") -0.02
    dax_long=avanza.get_positions().get('withOrderbook')[0].get('volume').get('value')
    #long sell rounding 
    b=np.format_float_positional(Long_sell, precision=3, unique=False, fractional=False, trim='k')
    
    #result1= avanza.place_order(str(account_number),str(orderbookidTrue()),OrderType.SELL,b,date.fromisoformat(datee),float(dax_long))
    print("Reeal long sell",dax_long,b)
    
def Short_sell():
    Short_sell= avanza.get_warrant_info(str(orderbookidTrue())).get("quote").get("buy") -0.02
    dax_short=avanza.get_positions().get('withOrderbook')[0].get('volume').get('value')
    #short sell
    #avanza.get_positions().get("instrumentPositions")[0].get("positions")[0].get("volume")
    
    b=np.format_float_positional(Short_sell, precision=3, unique=False, fractional=False, trim='k')
    #result= avanza.place_order(str(account_number),str(orderbookidTrue()),OrderType.SELL,b,date.fromisoformat(datee),dax_short)
    print(" Real short sell",dax_short,b)

#Short_buy()
#Long_sell()
#Long_buy()
#Short_sell()

#current_possition=avanza.get_account_overview("9651099").get('totalPositionsValue')
#numb_o_ord=avanza.get_account_overview("9651099").get('numberOfOrders')

#1 time run
#print(current_possition,ADX1hSMA(), numb_o_ord,Exception_entry(), ADXdif(),ADX47(),True_Ratio(),DI()[0],DI()[1],DI()[2]) 
#print(CCI70())




data = pd.read_excel(path_to_data)
df = pd.DataFrame(data, columns=['Trade Number', 'Filled', 'Section', 'Cases', 'Happens Modified 1', 'Happens norm','Happens Modified 2', 'Direction', 'Entry tradingview', 'Entry avanza', 'exit Tradingview', 'Exit avanza', 'Close time', 'Orderbookid', 'Tradingview Sum', 'avanza diff', 'Percent ', 'Win/Loss', 'Sortino average(15)', 'Sortino Drawdown', 'Sortino stdev of drawdown(15)', 'Sortino', 'Sortino (5 Delay)', 'Sortino Difference', 'Previous 5 average sortino dif', 'Fast move(15)', 'Fast move(15) diff 3', 'Fast move 15 diff for 2', 'Fast move(7)', 'Fast move (5 Delay)', 'Fast Difference', 'Test run Modified', 'Drawdown', 'Transfer', 'Test run norm', 'Drawdown norm', 'Test Run Modified 2'])
#pd.reset_option("all")
df.fillna(0,inplace=True)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#pd.get_option('display.max_rows', None)



#data_vix = pd.read_excel(path_to_VIXdata)
#df_VIX = pd.DataFrame(data_vix,columns=['Trade Number', 'Vix Open', 'Vix Close', 'From snp','From dax', 'Time open', 'Time close',"SL 5min","SL 15min"])
#df.loc[(len(df)),['Trade Number']] =df.loc[(len(df)-1),['Trade Number']]+1
#df.loc[(len(df)-1),['Section']] = 1

#def numb_o_ord():
   # noo=avanza.get_account_overview("9651099").get('numberOfOrders')
   # return int(noo)
#####
#def current_positions():
    #cp = float(avanza.get_account_overview("9651099").get('totalPositionsValue'))
    #return float(cp)

    
#def VIX_entry():
    

def Trade_number():
    
    df.loc[(len(df)),['Trade Number']] =df.loc[(len(df)-1),['Trade Number']] +1
    df.fillna(0,inplace=True)
    
    
def direction():
    try:
        cp = df.loc[(len(df)-1)]["Direction"]
    except:
        cp="no"
    return str(cp)
def Recalibrate():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=120)
    diff=abs(dax_data.close[119]-dax_data.open[72])
    return diff


            

def DataFrame_long_entry_process():
   if df.loc[(len(df)-1)]["Filled"]==int(1) :
       Trade_number() 
       print("long tech",datetime.now())
       adx_sma = ADX1hSMA()
       section_value = None
       if adx_sma[0] >= -0.4:
           if adx_sma[1] >= 0:
               section_value = 1 if adx_sma[2] >= 0 else 1.2
           else:
               section_value = 1.3
       else:
           if adx_sma[1] >= 0:
               section_value = 2.1 if adx_sma[2] >= 0 else 2.2
           else:
               section_value = 2.3 if adx_sma[2] >= 0 else 3

       df.iat[-1, df.columns.get_loc("Section")] = section_value
      
           
       if df.loc[(len(df)-2)]["Sortino Difference"]> 0.0:
           df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
           df.loc[(len(df)-1),["Happens norm"]]=int(1)
           
           
           if ADXLongtrend()[0]>0 and ADXLongtrend()[2]>0:
               df.loc[(len(df)-1),["Cases"]]=6
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Long_buy()
           elif ADXLongtrend()[0]>0 and ADXLongtrend()[1]>0:
               df.loc[(len(df)-1),["Cases"]] =3
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Long_buy()
               
           elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]>0 and ADXLongtrend()[2]>0:
               df.loc[(len(df)-1),["Cases"]] =5
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Long_buy()
           
           elif ADXLongtrend()[0]>0 or ADXLongtrend()[1]>0:
               df.loc[(len(df)-1),["Cases"]] =2
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Long_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               
           elif  ADXLongtrend()[0]<0 and ADXLongtrend()[2]>0 and ADXLongtrend()[1]<0:
               df.loc[(len(df)-1),["Cases"]]=4
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Long_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
           elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]<0:
               df.loc[(len(df)-1),["Cases"]] =1
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Long_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
          
           
              
       
       
       
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]>0 and ADXLongtrend()[2]>0:
           df.loc[(len(df)-1),["Cases"]]=6
           df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
           df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
           Long_buy()
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]>0 and ADXLongtrend()[1]>0 :
           df.loc[(len(df)-1),["Cases"]] =3
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               Long_buy()
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]<0 and ADXLongtrend()[1]>0 and ADXLongtrend()[2]>0:
           df.loc[(len(df)-1),["Cases"]] =5
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               Long_buy()
               
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]>0 or ADXLongtrend()[1]>0 :
            df.loc[(len(df)-1),["Cases"]] =2
            if df.loc[(len(df)-1)]["Section"]< 2.2:
                if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
                    df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
                    df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                    Long_buy()
            elif df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                Long_buy()
        
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]<0 and ADXLongtrend()[2]>0 and ADXLongtrend()[1]<0:
           df.loc[(len(df)-1),["Cases"]]=4
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               Long_buy()
           
            
       elif df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]<0 and ADXLongtrend()[1]<0:
           df.loc[(len(df)-1),["Cases"]] =1
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               Long_buy()
       
           
       if df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and  df.loc[(len(df)-2)]["Fast Difference"]> float(0.0) :
           #and df.loc[(len(df)-1)]["Section"]==1
            df.loc[(len(df)-1),["Happens norm"]]=int(1)
          
           
      
           
         
       df.loc[(len(df)-1),["Direction"]]="Lång"
       
       df.loc[(len(df)-1),["Entry tradingview"]]= float(current_price())
            #avanza price
       df.loc[(len(df)-1),["Entry avanza"]]=float(avanza.get_warrant_info (str((Long_Order_id()))).get("quote").get("sell"))
       df.loc[(len(df)-1),["Orderbookid"]]= int(Long_Order_id())
       
       #df.to_excel(path_to_data)

#DataFrame_long_entry_process()        
"""
       if adx_sma[0] >= -0.4:
           if adx_sma[1] >= 0:
               if adx_sma[2] >= 0:
                   df.loc[(len(df)-1), ["Section"]] = 1
               else:
                    df.loc[(len(df)-1), ["Section"]] = 1.2
           else:
                if adx_sma[2] < 0:
                    df.loc[(len(df)-1), ["Section"]] = 1.3
       else:
            if adx_sma[1] >= 0:
                if adx_sma[2] >= 0:
                    df.loc[(len(df)-1), ["Section"]] = 2.1
                else:
                    df.loc[(len(df)-1), ["Section"]] = 2.2
            else:
                if adx_sma[2] >= 0:
                    df.loc[(len(df)-1), ["Section"]] = 2.3
                else:
                    df.loc[(len(df)-1), ["Section"]] = 3
"""
def DataFrame_Short_entry_process():
   if df.loc[(len(df)-1)]["Filled"]==int(1) :
       Trade_number()
       print("short tech",datetime.now())
       adx_sma = ADX1hSMA()
       section_value = None

       if adx_sma[0] >= -0.4:
           if adx_sma[1] >= 0:
               section_value = 1 if adx_sma[2] >= 0 else 1.2
           else:
               section_value = 1.3
       else:
           if adx_sma[1] >= 0:
               section_value = 2.1 if adx_sma[2] >= 0 else 2.2
           else:
               section_value = 2.3 if adx_sma[2] >= 0 else 3

       df.iat[-1, df.columns.get_loc("Section")] = section_value


       
       print(datetime.now())
        # Happen yes or no
        
       if df.loc[(len(df)-2)]["Sortino Difference"]> 0.0:
           df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
           df.loc[(len(df)-1),["Happens norm"]]=int(1)
           
           
           if ADXLongtrend()[0]>0 and ADXLongtrend()[2]>0:
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               df.loc[(len(df)-1),["Cases"]]=6
               Short_buy()
           elif ADXLongtrend()[0]>0 and ADXLongtrend()[1]>0:
               df.loc[(len(df)-1),["Cases"]] =3
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()
               
           elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]>0 and ADXLongtrend()[2]>0:
               df.loc[(len(df)-1),["Cases"]] =5
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()

    
           elif ADXLongtrend()[0]>0 or ADXLongtrend()[1]>0:
               df.loc[(len(df)-1),["Cases"]] =2
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Short_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
                   
               
           elif  ADXLongtrend()[0]<0 and ADXLongtrend()[2]>0 and ADXLongtrend()[1]<0:
               df.loc[(len(df)-1),["Cases"]]=4
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Short_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
               #df.loc[(len(df)-1),["Happens Modified 2"]]=int()
           elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]<0:
               df.loc[(len(df)-1),["Cases"]] =1
               if df.loc[(len(df)-1)]["Section"]< 2.2:
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                   Short_buy()
               else: 
                   df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
          
           
      
       elif ADXLongtrend()[0]>0 and ADXLongtrend()[2]>0:
           df.loc[(len(df)-1),["Cases"]]=6
           df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
           df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
           Short_buy()
       elif ADXLongtrend()[0]>0 and ADXLongtrend()[1]>0 :
           df.loc[(len(df)-1),["Cases"]] =3
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()
       elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]>0 and ADXLongtrend()[2]>0:
           df.loc[(len(df)-1),["Cases"]] =5
           if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
               df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()
               
       elif ADXLongtrend()[0]>0 or ADXLongtrend()[1]>0 :
            df.loc[(len(df)-1),["Cases"]] =2
            if df.loc[(len(df)-1)]["Section"]< 2.2:
                if  df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']: 
                    df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
                    df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                    Short_buy()
            elif df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
                df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                Short_buy()
                
                
        
       elif  ADXLongtrend()[0]<0 and ADXLongtrend()[2]>0 and ADXLongtrend()[1]<0:
           df.loc[(len(df)-1),["Cases"]]=4
           if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()
           
            
       elif ADXLongtrend()[0]<0 and ADXLongtrend()[1]<0:
           df.loc[(len(df)-1),["Cases"]] =1
           if df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
               df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
               Short_buy()
      
           
       if  df.loc[(len(df)-2)]["Fast Difference"]> float(0.0) :
           #and df.loc[(len(df)-1)]["Section"]==1 
           df.loc[(len(df)-1),["Happens norm"]]=int(1)
          
       
        
       
       df.loc[(len(df)-1),["Direction"]]= "Kort"
       df.loc[(len(df)-1),["Entry tradingview"]]= float(current_price())
    #avanza price
      # df.loc[(len(df)-1),["Entry avanza"]]= avanza.get_warrant_info (str((Short_Order_id()))).get("quote").get("sell")
       #df.loc[(len(df)-1),["Orderbookid"]]= int(Short_Order_id())
    
        #str(avanza.get_warrant_info(str(Short_Order_id())).get("keyIndicators").get("direction"))
                   
       df.to_excel(path_to_data)
        
def DataFrame_Short_entry_process1():
   if df.loc[(len(df)-1)]["Filled"]==int(1) :
       Trade_number()
       print("short tech",datetime.now())
       adx_sma = ADX1hSMA()
       section_value = None

       if adx_sma[0] >= -0.4:
           if adx_sma[1] >= 0:
               section_value = 1 if adx_sma[2] >= 0 else 1.2
           else:
               section_value = 1.3
       else:
           if adx_sma[1] >= 0:
               section_value = 2.1 if adx_sma[2] >= 0 else 2.2
           else:
               section_value = 2.3 if adx_sma[2] >= 0 else 3

       df.iat[-1, df.columns.get_loc("Section")] = section_value


       
      
        
       adx_longtrend = ADXLongtrend()

       if df.iloc[len(df) - 2]["Sortino Difference"] > 0.0:
            df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
            df.iloc[len(df) - 1, df.columns.get_loc("Happens norm")] = 1
        
            if adx_longtrend[0] > 0:
                if adx_longtrend[2] > 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 6
                    Short_buy()
                elif adx_longtrend[1] > 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
                elif adx_longtrend[2] < 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
            elif adx_longtrend[0] < 0:
                if adx_longtrend[1] > 0 and adx_longtrend[2] > 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
                elif adx_longtrend[1] > 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
                elif adx_longtrend[2] > 0 and adx_longtrend[1] < 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
                elif adx_longtrend[1] < 0:
                    df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
        
            if adx_longtrend[0] > 0 or adx_longtrend[1] > 0:
                df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 2
                if df.iloc[len(df) - 1]["Section"] < 2.2:
                    if (
                        df.iloc[len(df) - 2]["Fast move(15)"]
                        >= df.iloc[len(df) - 2]["Fast move(15) diff 3"]
                        and df.iloc[len(df) - 2]["Fast move(7)"] > df.iloc[len(df) - 2]["Fast move(15)"]
                        and df.iloc[len(df) - 2]["Fast move (5 Delay)"] > df.iloc[len(df) - 2]["Fast move(15)"]
                    ):
                        df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                        Short_buy()
                elif (
                    df.iloc[len(df) - 2]["Fast move(15)"]
                    >= df.iloc[len(df) - 2]["Fast move(15) diff 3"]
                    and df.iloc[len(df) - 2]["Fast move(7)"] > df.iloc[len(df) - 2]["Fast move(15)"]
                    and df.iloc[len(df) - 2]["Fast move (5 Delay)"] > df.iloc[len(df) - 2]["Fast move(15)"]
                ):
                    df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                    Short_buy()
        
            if df.iloc[len(df) - 2]["Fast Difference"] > 0.0:
                df.iloc[len(df) - 1, df.columns.get_loc("Happens norm")] = 1
          
       
        
       
       df.loc[(len(df)-1),["Direction"]]= "Kort"
       current_price_value = float(current_price())
       short_order_id_value = Short_Order_id()
       last_row_index = len(df) - 1
        
       df.iloc[last_row_index, df.columns.get_loc("Direction")] = "Kort"
       df.iloc[last_row_index, df.columns.get_loc("Entry tradingview")] = current_price_value
        
       avanza_info = avanza.get_warrant_info(str(short_order_id_value))
       df.iloc[last_row_index, df.columns.get_loc("Entry avanza")] = avanza_info.get("quote").get("sell")
        
       df.iloc[last_row_index, df.columns.get_loc("Orderbookid")] = int(short_order_id_value)
       df.to_excel(path_to_data)

def DataFrame_Exit_process():
        
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
            df.loc[(len(df)-1),['exit Tradingview']]= current_price()
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
               df.loc[(len(df)-1),[ 'Test run Modified 2']]= float(df.loc[(len(df)-1),['Percent ']]-0.008)*float(df.loc[(len(df)-2),['Test run Modified 2']])
            else:
               df.loc[(len(df)-1),['Test run Modified 2']]=df.loc[(len(df)-2),['Test run Modified 2']]
           
            df['Drawdown Modified 2'] = (df['Test run Modified 2'] - df['Test run Modified 2'].cummax())/df['Test run Modified 2'].cummax()
           
            
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
                
            
        ##############
        #to excell
            df.loc[(len(df)-1),['Close time']]= datetime.now()
            print("exit complete")
            df.to_excel(path_to_data)
  
def Current_time():
    t = time.localtime()
    current_time = time.strftime("%H%M", t)
    return float(current_time)


def Long_add_to_watchlist():
    string=("B Longdax sg"," tlng dax vt","tlng dax vt")
    #" T long dax nordnet",
    Long_watchlist_id='10045250'
    cu=int()
    
    for b in range(0,2):
        q=avanza.search_for_warrant(string[b]).get('hits')[0].get('topHits')
        for i in range(0,len(q)):
            r=avanza.search_for_warrant(string[b]).get('hits')[0].get('topHits')[i].get('id')
            #s= avanza.get_warrant_info (str(r)).get("quote").get("sell")
           
            try: 
                s= avanza.get_warrant_info (str(r)).get("quote").get("sell")
            except:
                print(s)
            if s == None:
                cu=0.1
            else:
                try:
                    cu=avanza.get_warrant_info (str(r)).get("quote").get("sell")
                except:
                    print(cu)
            if cu>1.4 and cu<4.5:
                #a.append((r,cu))
                avanza.add_to_watchlist(str(r), Long_watchlist_id)

def Short_add_to_watchlist():
    string=("tsrt dax vt"," B shrtdax sg")
    #" T shrt dax nordnet",
    Short_watchlist_id='10045251'
    cu=int()
    
    for b in range(0,2):
        q=avanza.search_for_warrant(string[b]).get('hits')[0].get('topHits')
        for i in range(0,len(q)):
            r=avanza.search_for_warrant(string[b]).get('hits')[0].get('topHits')[i].get('id')
            try: 
                s= avanza.get_warrant_info (str(r)).get("quote").get("sell")
            except:
                print(s)
            if s == None:
                cu=0.1
            else:
                try:
                    cu=avanza.get_warrant_info (str(r)).get("quote").get("sell")
                except:
                    print(cu)
            if cu>1.4 and cu<4.5:
                #a.append((r,cu))
                avanza.add_to_watchlist(str(r), Short_watchlist_id)


def Long_Remove_watchlist():
    r=avanza.get_watchlists()[0].get('orderbooks')
    i=len(r)
    l=[]
    cu=int()
    for j in range(4,-1,-1):
        for k in range (0, i-j):
            z=avanza.get_watchlists()[0].get('orderbooks')[k]
            s= avanza.get_warrant_info (str(z)).get("quote").get("sell")
            #if type(s)== "NoneType ":
                #cu=0.1
            #print(z)
            #print(s)
            
            #print(type(s))
            if s == None:
                avanza.remove_from_watchlist(z, '10045250')
            elif s<1.2 or s>5.6:
                avanza.remove_from_watchlist(z, '10045250')
        
#print(avanza.get_watchlists()[0].get('orderbooks'))
def Short_Remove_watchlist():
    
    r=avanza.get_watchlists()[2].get('orderbooks')
    i=len(r)
    l=[]
    cu=int()
    for j in range (4,-1-1):
        for k in range (0, i-j):
            z=avanza.get_watchlists()[2].get('orderbooks')[k]
            
            s= avanza.get_warrant_info (str(z)).get("quote").get("sell")
            #if type(s)== "NoneType ":
                #cu=0.1
            #print(z)
            #print(s)
            
            #print(type(s))
            if s == None:
                avanza.remove_from_watchlist(z, '10045251')
            elif s<1.2 or s>5.6:
                avanza.remove_from_watchlist(z, "10045251")
#Dataframe
#DataFrame_long_entry_process()
#DataFrame_Exit_process()
#df.drop(index=df.index[-1], axis=0, inplace=True) 
#df.to_excel(path_to_data)
#Long_add_to_watchlist()
#Short_add_to_watchlist()
#DataFrame_Short_entry_process1()
#df.loc[(len(df)-1),["Entry tradingview"]]= 15784
#df.loc[(len(df)-1),["Exit avanza"]]= 3.3
#df.loc[(len(df)-1),["Orderbookid"]]= 1626167
#df.to_excel(path_to_data)
#DataFrame_Short_entry_process()

#print(df)
def distance():
    
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_4_hour,n_bars=100)
    a=abs(dax_data.close[99]-dax_data.close[98])
    return a

#Current_time()>801.0 or Current_time()>816.0 or Current_time()>910.0 or
#print(sl15mindax()[0])

#Long_add_to_watchlist()
#Short_add_to_watchlist()
#print(Long_Order_check())
#Long_add_to_watchlist()
#Short_add_to_watchlist()
#Long_Remove_watchlist()
#Short_Remove_watchlist()
print(datetime.now())
DataFrame_long_entry_process()
print(datetime.now())
"""
print(df)


while True:
    try:
        while True:
           
            account_number=9651099
            numb_o_ord=avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value')
            current_positions = avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get("value")
            condition=82
            if  df.loc[(len(df)-1)]["Filled"]==int(1) and 802.0<=Current_time()<2158.0 and surge_protection()[0]<=1.0 and surge_protection()[1]<=1.0:
                
                if current_positions<10  and ADX1hSMA()<=-0.5 and surge_protection()[0]<=1.0 and surge_protection()[1]<=1.0 and 10>=numb_o_ord>=-10 and Exception_entry()>=1.8 and 9.8<= ADXdif()<28 and  ADX47()<28 and True_Ratio()>=0.0  and (DI()[0]-2 >DI()[1]) and (DI()[0]-2 >DI()[2]):
                    #print("may")
                    Long_orderbookId1= Long_Order_id()           
                    Short_orderbookId1= Short_Order_id()
                    #print(CCI70())
                    
                    if 10<=CCI70()<=300 :
                    #long entry
                        DataFrame_long_entry_process()
                        
                    elif -10>=CCI70()>=-300 :
                    #short entry
                        #print("ok")
                        DataFrame_Short_entry_process()
                    
                        
                    
                elif current_positions<10 and surge_protection()[0]<=1.0 and surge_protection()[1]<=1.0 and Surge()<=20.000 and ADX1hSMA()>=-0.5 and 10>=numb_o_ord>=-10:
                    Long_orderbookId1= Long_Order_id()           
                    Short_orderbookId1= Short_Order_id()
                    if ADX1h()<21:
                        if 10<= ADXdif()<28 and ADX47()<28 and True_Ratio()>0.20 :                  
                            if 150<= CCI70()<=310 and sl15mindax()[2]>0.00 and sl15mindax()[0]<=condition :
                                DataFrame_long_entry_process()
                                
                            elif -150>= CCI70()>=-310 and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition:
                                DataFrame_Short_entry_process()
                    
                    #test thiss
                    elif 21<=ADX1h() <32 :              
                        if 10<= ADXdif()<=28 and  ADX47()<=28.00 and True_Ratio()>=0.20 and (DI()[1]>=12) and (DI()[2]>=12 ) and (DI()[0]-2 >DI()[1]) and (DI()[0]-2 >DI()[2]):
                            if 10<=CCI70()<=300 and sl15mindax()[2]>0.00 and sl15mindax()[0]<=condition:
                               DataFrame_long_entry_process()
                            elif -10>=CCI70()>=-300 and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition:
                               DataFrame_Short_entry_process() 
                               #print("yup short")
                        
                        if 1<= ADXdif()<=28  and 20.000<=ADX47()<=28.00 and True_Ratio()>=0.2 and (DI()[1]>=12) and (DI()[2]>=12 ) and (DI()[0]-2 >DI()[1]) and (DI()[0]-2 >DI()[2]) :
                            if sl15mindax()[2]>0.00 and 10<=CCI70()<=300 and sl15mindax()[0]<=condition:
                                DataFrame_long_entry_process()
                            elif -10>= CCI70()>=-300 and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition:
                                DataFrame_Short_entry_process()
                                #print("yup short")
                            
                        
                            
                        if True_Ratio()>=1.5:
                            if 1<= ADXdif()  and 20.00<=ADX47() :
                                if 10<=CCI70() and  sl15mindax()[2]>0.00 and sl15mindax()[0]<=condition:
                                    DataFrame_long_entry_process()
                                elif -10>=CCI70() and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition:
                                    DataFrame_Short_entry_process()
                            
                    elif ADX1h()>=32 :
                        #and DILow()[0]>=DILow()[1]
                            if 10<= ADXdif()<28  and ADX47()<=28 and True_Ratio()>=0.0 and DILow()[1]>=12 :
                                if 10<=CCI70()<=300 and sl15mindax()[2]>0.00 and sl15mindax()[0]<=condition:
                                    DataFrame_long_entry_process()
                                elif -10>=CCI70()>=-300 and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition :
                                    DataFrame_Short_entry_process()
                                
                            if 1<= ADXdif()<28 and 20<=ADX47()<=28 and True_Ratio()>=0.0  and DILow()[1]>=12 :
                                if 10<=CCI70()<=300 and sl15mindax()[2]>0.00 and sl15mindax()[0]<=condition:
                                    DataFrame_long_entry_process()
                                elif -10>=CCI70()>=300 and sl15mindax()[3]>0.00 and sl15mindax()[1]<=condition:
                                    DataFrame_Short_entry_process()
            
            #elif current_positions>10 and numb_o_ord==0:
            elif df.loc[(len(df)-1)]["Filled"]==int(0) :
                #print("here 0")
                
             
                if Current_time()>=2158.0: 
                   print("Time constraint exit")
                   DataFrame_Exit_process()
                   
                
                if Exception_exit()<=0:
                   
                    if direction()=="Lång":
                        #print("here 1")
                        if ADX1h()<48 :
                            if sl5mindax()[0]<0.0:
                                DataFrame_Exit_process()
                            elif sl5mindax()[2]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 5 Min")
                            #LONG SELL
                            
                            
                        elif 48<=ADX1h() :
                            if sl15mindax()[0]<0.00:
                                DataFrame_Exit_process()
                            elif sl15mindax()[2]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 15 Min")
                                
                    elif direction()=="Kort":
                      
                        if ADX1h()<48  :
                            if sl5mindax()[1]<0.00:
                                DataFrame_Exit_process()
                            elif sl5mindax()[3]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 5 Min")
                                
                            
                            #SHORT SELL
                        
                            
                        elif 48<=ADX1h() :
                            if sl15mindax()[1]<0.00:
                                DataFrame_Exit_process()
                            elif sl15mindax()[3]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 15 Min")
                           
                
                if True_Ratio()< 1.0 :
                    
                    if direction()=="Lång":
                        #print("here 3")
                        if  sl5mindax()[0]<0.00 :
                            DataFrame_Exit_process()
                        elif  sl5mindax()[2]<0.00 :
                            DataFrame_Exit_process()
                            print("WMA 5 Min")
                        
                    elif direction()=="Kort" :
                        #print("here s")
                        if  sl5mindax()[1]<0.00 :
                            DataFrame_Exit_process()
                        elif sl5mindax()[3]<0.00:
                            DataFrame_Exit_process()
                            print("WMA 5 Min")
                            
                
                if True_Ratio()>=1.0 :
                    if direction()=="Lång" : #orderbookidTrue()==Long_orderbookId1 :
                        #print("here 4")
                        if ADX1h()<18:
                            if  sl5mindax()[0]<0.00 :
                                DataFrame_Exit_process()
                            elif  sl5mindax()[2]<0.00 :
                                DataFrame_Exit_process()
                                print("WMA 5 Min")
                            #DataFrame_Exit_process()
                        if 18 <= ADX1h()<48 :
                            if sl15mindax()[0]<0.00:
                                DataFrame_Exit_process()
                            elif sl15mindax()[2]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 15 Min")
                            
                            
                        elif ADX1h()>=48 :
                            if sl30mindax()[0]<0.00:
                                DataFrame_Exit_process()
                            elif sl30mindax()[2]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 30 Min")
                            
                
                            
                    elif direction()=="Kort":
                        #print("kort")
                        if ADX1h()<18 :
                            if  sl5mindax()[1]<0.00 :
                                DataFrame_Exit_process()
                            elif sl5mindax()[3]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 5 Min")
                            
                            
                        if 18<=ADX1h()<48 :
                            if sl15mindax()[1]<0.00:
                                DataFrame_Exit_process()
                            elif sl15mindax()[3]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 15 Min")
                           
                            
                        elif ADX1h()>=48 :
                            if sl30mindax()[1]<0.00:
                                DataFrame_Exit_process()
                            elif sl30mindax()[3]<0.00:
                                DataFrame_Exit_process()
                                print("WMA 30 Min")
                            
            if Recalibrate()>90:
                 #print("here")
                 if surge_protection()[0]>=1.0 or surge_protection()[1]>=1.0:
                     #print("here2")
                     if Long_Order_check()>0 or Short_Order_check()>0:
                         #print("here 3")
                         Long_add_to_watchlist()
                         Short_add_to_watchlist()
                         Long_Remove_watchlist()
                         Short_Remove_watchlist()
                         
                
               
                
                               
                
                         
            time.sleep(3)
            #print("hi")
    except Exception as e:
        # If an error occurs, log the error and sleep for a bit
        print(f"Error: {e}",datetime.now())
        time.sleep(3)
        
"""