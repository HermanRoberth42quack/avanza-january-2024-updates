# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:19:33 2024

@author: herma
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:19:54 2024

@author: herma
"""
import sys
import time
import pandas as pd
from maintv import TvDatafeed,Interval
import threading
import datetime
from datetime import datetime

path_to_data = r"C:\Users\herma\Desktop\Dax_data\15min.xlsx"

# Create a lock for synchronization
excel_lock = threading.Lock()


#username = 'Herman_Roberth'
#password = 'Ledzeppelinpinkfloyd123'
tv = TvDatafeed()
def append_historical_data():
    try:
        # Get historical data
        
        dax_data = tv.get_hist("DE30EUR", 'OANDA', interval=Interval.in_15_minute, n_bars=500)
        
        # Acquire the lock before accessing the Excel file
        with excel_lock:
            # Read existing Excel file
            dax_data.to_excel(path_to_data, index=False)
            #sys.exit()
            
        print("Historical data appended successfully.",datetime.now())
        #return True
        return True  # Return True indicating success
        
    except FileNotFoundError:
        print("Error: Excel file not found.")
    except PermissionError:
        print("Error: Permission denied to write to Excel file.")
    except Exception as e:
        print("Error appending historical data:", e)
    return False  # Return False indicating failure

success = False  # Initialize success flag

while not success:  # Continue until success
    try:
        success = append_historical_data()  # Try to append historical data
        if not success:
            time.sleep(5)  # Sleep for 10 seconds before retrying
    except KeyboardInterrupt:
        print("Process interrupted.")
        sys.exit()
        
        
a=5
if a==5:
    print("hi")