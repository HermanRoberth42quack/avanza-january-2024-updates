# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:02:22 2024

@author: herma
"""


import time
import numpy as np
import pandas as pd
#from maintv import TvDatafeed,Interval
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


#tv = TvDatafeed()
path_to_data= r'C:\Users\herma\Desktop\Dax_data\15min.xlsx'
#dax_data=tv.get_hist("DE30EUR",'OANDA',interval=Interval.in_15_minute,n_bars=400)
#dax_data.to_excel(path_to_data, index=False)
#dax_data=tv.get_hist(interval=Interval.in_3_minute,n_bars=5)
#print(dax_data)
from tradingview_ta import TA_Handler, Interval, Exchange

dax = TA_Handler(
    symbol="DE30EUR",
    screener="cfd",
    exchange="OANDA",
    interval=Interval.INTERVAL_15_MINUTES,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
#print(dax.get_indicators(["open","low","high","close"]))
#datetime.now()

def get_indicators():
    return dax.get_indicators(["open","high","low","close"])




data = pd.read_excel(path_to_data)
df = pd.DataFrame(data, columns = ['timestamp', 'open', 'high', 'low', 'close'])
current_minute = pd.Timestamp.now().replace(second=0, microsecond=0)

current_row_index = len(df.open)-1

while True:
    try:
        
        while True:
            #if datetime.now().second<59 :
            
                current_data = get_indicators()
                #current_row_index = 0
                # Get current minute
                new_minute = pd.Timestamp.now().replace(second=0, microsecond=0)
                
                # Check if the minute has changed
                if new_minute.minute // 15 != current_minute.minute // 15:
                    df.loc[current_row_index -1,"close"]=df.loc[current_row_index,"open"]
                    # Increment the row index
                    current_row_index =current_row_index + 1
                    df.loc[current_row_index, 'timestamp'] = new_minute
                    current_minute = new_minute
                    df.loc[current_row_index, ['open', 'low', 'high', 'close']] = [current_data['open'], current_data['low'], current_data['high'], current_data['close']]
                    df.to_excel(path_to_data, index=False , encoding='utf-8')
                # Update the current row with the current indicators
                df.loc[current_row_index, ['open', 'high', 'low', 'close']] = [current_data['open'], current_data['high'], current_data['low'], current_data['close']]
                #print(df)
                df.to_excel(path_to_data, index=False, encoding='utf-8')
                
        

    except Exception as e:
     #If an error occurs, log the error and sleep for a bit
     print(f"Error: {e}",datetime.now())



  
