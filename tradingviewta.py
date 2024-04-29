# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:19:54 2024

@author: herma
"""
import time
import numpy as np
import pandas as pd
from maintv import TvDatafeed,Interval
import seis
from seis import Seis

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
from maintv import Interval
from tvlive import TvDatafeedLive

#username = 'Herman_Roberth'
#password = 'Ledzeppelinpinkfloyd123'
path_to_data= r"C:\Users\herma\Desktop\Dax_data\dax_data_3min.xlsx"
data = pd.read_excel(path_to_data)
df3 = pd.DataFrame(data, columns = ['timestamp', 'open', 'high', 'low', 'close'])

#tv = TvDatafeed()
#dax_data=tv.get_hist(interval=Interval.in_3_minute,n_bars=5)
#print(dax_data)
from tradingview_ta import TA_Handler, Interval, Exchange

dax = TA_Handler(
    symbol="DE30EUR",
    screener="cfd",
    exchange="OANDA",
    interval=Interval.INTERVAL_1_MINUTE,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)

def get_indicators():
    return dax.get_indicators(["open","high","low","close"])

columns = ['timestamp', 'open', 'high', 'low', 'close']
df = pd.DataFrame(columns=columns)
df2= df3
# Continuously update the DataFrame
current_minute = pd.Timestamp.now().replace(second=0, microsecond=0)
current_row_index = 0
current_row1_index = len(df3.open)-1
# Continuously update the DataFrame
#dax_data=tv.get_hist("DE30EUR",'OANDA',interval=Interval.in_3_minute,n_bars=400)
#dax_data.to_excel(path_to_data, index=False)

while True:
    #if datetime.now().second<59 :
    
        current_data = get_indicators()
        new_minute = pd.Timestamp.now().replace(second=0, microsecond=0)
        if new_minute.minute // 3 != current_minute.minute // 3:
            df2.loc[current_row1_index,"close"]=df.loc[current_row_index,"close"]
            df2.loc[current_row1_index -1,"close"]=df2.loc[current_row1_index,"open"]
            current_row1_index =current_row1_index + 1
            df2.loc[current_row1_index, 'timestamp'] = new_minute
            df2.loc[current_row1_index, ['open', 'high', 'low', 'close']] = [current_data['open'], current_data['high'], current_data['low'],current_data['close'] ]
            #print(df)
            #print(df2)
            df.drop(df.index[0:3], inplace=True)
            current_row_index = -1
            
            df2.to_excel(path_to_data, index=False)
        if new_minute != current_minute:
            current_row_index =current_row_index + 1
            df.loc[current_row_index, 'timestamp'] = new_minute
            current_minute = new_minute
            
        df.loc[current_row_index, ['open', 'high', 'low', 'close']] = [current_data['open'], current_data['high'], current_data['low'], current_data['close']]
        df2.loc[current_row1_index, ['open', 'high', 'low', 'close']] = [df.loc[0,"open"], df["high"].max(),df["low"].min(), df.loc[current_row_index,'close']]
        df2.to_excel(path_to_data, index=False)
        
    


  
