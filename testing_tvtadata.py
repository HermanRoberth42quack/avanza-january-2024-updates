# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:02:40 2024

@author: herma
"""

import pandas as pd




import talib


path_to_data=  r"C:\Users\herma\Desktop\Dax_data\15min.xlsx"
def Dax5minData():
   
    data = pd.read_excel(path_to_data, engine='openpyxl')
    df = pd.DataFrame(data, columns = ['datetime', 'open', 'high', 'low', 'close'])
    dax_data=df
    return dax_data
def ADX47():
    dax_data=Dax5minData()

    real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=42)
    a=real[len(dax_data.open)-1]
    return a
#print(ADX47())

def ADXdif():
    #dax_data=df
    #real = talib.ADX(dax_data.high, dax_data.low, dax_data.close, timeperiod=42)
    #a=(real- real.shift(1))*50
    a=5
    return a


print(Dax5minData())