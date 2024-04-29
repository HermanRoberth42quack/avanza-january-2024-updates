# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:31:35 2023

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

tv = TvDatafeed()
account_number=9651099
 

symbolD= 'DE30EUR' #'GRXEUR' 
exchangeD= 'OANDA' #'FOREXCOM'

symbolDVIX= 'VIX' 
exchangeDVIX='PEPPERSTONE' 

#snp_500=tv.get_hist(symbol="SPXUSD",exchange="FOREXCOM",interval=Interval.in_daily,n_bars=50)
dax_data=tv.get_hist(symbol=symbolD,exchange=exchangeD,interval=Interval.in_daily,n_bars=50)
pd.set_option('display.max_columns', None)
#percentsnp=(snp_500.close-snp_500.open)/snp_500.open
#percentdax=(dax_data.close-dax_data.open)/dax_data.open
#a=percentdax.cov(percentsnp)

#correlation=a/(talib.STDDEV(dax_data.close)[49]*talib.STDDEV(snp_500.close)[49])
print(dax_data)