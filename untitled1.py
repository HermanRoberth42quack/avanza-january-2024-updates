# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:23:09 2024

@author: herma
"""
      df.iat[-1, df.columns.get_loc("Section")] = section_value
      adx_longtrend = ADXLongtrend()
      if df.iloc[len(df) - 2]["Sortino Difference"] > 0.0:
          df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
          df.iloc[len(df) - 1, df.columns.get_loc("Happens norm")] = 1

          if adx_longtrend[0] > 0:
              if adx_longtrend[2] > 0:
                  df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                  df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 6
                  Long_buy()
              elif adx_longtrend[1] > 0:
                  df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                  df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                  Long_buy()
              df.loc[(len(df)-1),["Cases"]] =2
              if df.loc[(len(df)-1)]["Section"]< 2.2:
                  df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")]=1
                  Long_buy()
              
              
          elif adx_longtrend[0] < 0:
              if adx_longtrend[1] > 0 and adx_longtrend[2] > 0:
                  df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                  df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                  Long_buy()
              
              elif adx_longtrend[2] > 0 and adx_longtrend[1] < 0:
                  df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                  if df.loc[(len(df)-1)]["Section"]< 2.2:
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                      Long_buy()
                  else: 
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
              elif adx_longtrend[1] < 0:
                  df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                  if df.loc[(len(df)-1)]["Section"]< 2.2:
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                      Long_buy()
                  else: 
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
                  
              
                  
      else :
          if df.loc[(len(df)-2)]["Sortino Difference"]< 0.0 and ADXLongtrend()[0]>0 and ADXLongtrend()[2]>0:
              df.loc[(len(df)-1),["Cases"]]=6
              df.loc[(len(df)-1),["Happens Modified 1"]]=int(1)
              df.loc[(len(df)-1),["Happens Modified 2"]]=int(0)
          elif df.loc[(len(df)-2)]['Fast move(15)']>= df.loc[(len(df)-2)]['Fast move(15) diff 3'] and df.loc[(len(df)-2)]["Fast move(7)"]> df.loc[(len(df)-2)]['Fast move(15)'] and df.loc[(len(df)-2)]["Fast move (5 Delay)"]> df.loc[(len(df)-2)]['Fast move(15)']:
          
              if adx_longtrend[0] > 0:
                  if adx_longtrend[1] > 0:
                      df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 3
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                      Long_buy()
                  else:
                      df.loc[(len(df)-1),["Cases"]] =2
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                      Long_buy()
                  
                  
              else :
                  if adx_longtrend[1] > 0 and adx_longtrend[2] > 0:
                      df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 5
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 2")] = 1
                      Long_buy()
                  
                  elif adx_longtrend[2] > 0 and adx_longtrend[1] < 0:
                      df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 4
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                      Long_buy()
                      
                  elif adx_longtrend[1] < 0:
                      df.iloc[len(df) - 1, df.columns.get_loc("Cases")] = 1
                      df.iloc[len(df) - 1, df.columns.get_loc("Happens Modified 1")] = 1
                      df.loc[(len(df)-1),["Happens Modified 2"]]=int(1)
                      Long_buy()
                
          if df.loc[(len(df)-2)]["Fast Difference"]> float(0.0) :
                 #and df.loc[(len(df)-1)]["Section"]==1
                  df.loc[(len(df)-1),["Happens norm"]]=int(1)
                  
          