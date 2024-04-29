# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:46:30 2024

@author: herma
"""
import pandas as pd
import threading

import sys
import time

from maintv import TvDatafeed,Interval
import threading
import datetime
from datetime import datetime
path_to_data = r'C:\Users\herma\Desktop\Dax_data\15min.xlsx'

# Create a lock for synchronization
excel_lock = threading.Lock()
tv = TvDatafeed()
def append_historical_data():
    try:
        # Get historical data
        
        dax_data = tv.get_hist("DE30EUR", 'OANDA', interval=Interval.in_15_minute, n_bars=500)
        
        # Acquire the lock before accessing the Excel file
        with excel_lock:
            # Read existing Excel file
            dax_data.to_excel(path_to_data, index=True)
            #sys.exit()
            
        print("Historical data appended successfully 15min.",datetime.now())
        #return True
        #return True  # Return True indicating success
    
    except Exception as e:
        #print("Error appending historical data:", e)
    #return False  # Return False indicating failure
        a=5

#success = False  # Initialize success flag

while True:  # Continue until success
    try:
        append_historical_data()  # Try to append historical data
        # Sleep for 10 seconds before retrying
    except KeyboardInterrupt:
        print("Process interrupted.")
        sys.exit()

from tradingview_ta import TA_Handler, Interval
def get_indicators():
    dax = TA_Handler(
        symbol="DE30EUR",
        screener="cfd",
        exchange="OANDA",
        interval=Interval.INTERVAL_15_MINUTES
    )
    return dax.get_indicators(["open", "high", "low", "close"])

def update_excel():
    while True:
        try:
            with excel_lock:
                data = pd.read_excel(path_to_data)
                df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close'])
                current_minute = pd.Timestamp.now().replace(second=0, microsecond=0)
                current_row_index = len(df.open) - 1
                
                current_data = get_indicators()
                new_minute = pd.Timestamp.now().replace(second=0, microsecond=0)
                
                if new_minute.minute // 15 != current_minute.minute // 15:
                    df.loc[current_row_index - 1, "close"] = df.loc[current_row_index, "open"]
                    current_row_index += 1
                    df.loc[current_row_index, 'timestamp'] = new_minute
                    current_minute = new_minute
                    df.loc[current_row_index, ['open', 'low', 'high', 'close']] = [current_data['open'], current_data['low'], current_data['high'], current_data['close']]
                    df.to_excel(path_to_data, index=False)
                else:
                    df.loc[current_row_index, ['open', 'high', 'low', 'close']] = [current_data['open'], current_data['high'], current_data['low'], current_data['close']]
                    df.to_excel(path_to_data, index=False)
        except Exception as e:
            print("Error:", e)

# Start the update_excel function in a separate thread
#update_thread = threading.Thread(target=update_excel)
#update_thread.start()