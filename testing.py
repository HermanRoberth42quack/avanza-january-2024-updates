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
import datetime
import hashlib
import pyotp
from scipy.stats import skewnorm
import numpy as np
from datetime import datetime
from datetime import date
import certifi
import talib
from avanza import Avanza,OrderType,InstrumentType
from avanza import Avanza,OrderType,InstrumentType

avanza = Avanza({
    'username': 'Herman_Roberth',
    'password': 'Sweetheart123',
    'totpSecret': 'HGR5JY7LUORXDYNM5IYAZ6A6S7PHCWVE'
})

"""
account_number=9651099
Is_Real_off= "YESS ACTUALL MONEY"  
symbolD= 'VIX' 
exchangeD='PEPPERSTONE'  
tv = TvDatafeed()

"""
symbolD= 'DE30EUR' #'GRXEUR' pip 
exchangeD= 'OANDA' #'FOREXCOM'
account_number=9651099
tv = TvDatafeed()
#vix_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=5000)
dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
#print(dax_data)
#print(vix_data)
def current_price():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_minute,n_bars=1)
    return dax_data.close.sum()


def Current_time():
    t = time.localtime()
    current_time = time.strftime("%H%M", t)
    return float(current_time)


def ADX1h():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_1_hour,n_bars=4000)
    #b=dax_data.high
   
    real = talib.ADX(dax_data.high , dax_data.low, dax_data.close, timeperiod=12)
    a=real[3999]
      
    
    
    return a

def Recalibrate():
    dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_3_minute,n_bars=120)
    diff=abs(dax_data.close[119]-dax_data.open[72])
    return diff
    

r=avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value')
#'balanceOnTradableAccounts'
#b=avanza.get_account_overview(account_number)
#avanza.get_account_overview(account_number).get('totalValue').get('positionValue').get("value")
#avanza.get_account_overview(account_number).get('accounts')[2].get('totalValue').get("totalValue").get('value')
#'currentOrders'
#number of orders in value 
#avanza.get_account_overview(account_number).get('buyingPower').get('currentOrders').get('value')
print(r)
#avanza.get_positions().get('withOrderbook')[0].get('instrument').get('orderbook').get('id')
#print(Recalibrate())