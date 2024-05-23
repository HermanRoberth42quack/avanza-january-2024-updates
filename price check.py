# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:40:11 2024

@author: Herman Roberth
"""
def check_orders2(watchlist_index):
    r = avanza.get_watchlists()[watchlist_index].get('orderbooks')
    min_values = [float('inf'), float('inf')]  # To store the two smallest values

    for z in r:
        warrant_info = avanza.get_warrant_info(str(z)).get("quote").get("sell")
        cu = 0.1 if warrant_info is None else warrant_info

        # Update the two smallest values
        if cu < min_values[0]:
            min_values = [cu, min_values[0]]
        elif cu < min_values[1]:
            min_values[1] = cu

    # Check if either of the two smallest values is less than 0.8
    if min_values[0] < 0.75 or min_values[1] < 0.75:
        return 1
    return 0

def check_orders(watchlist_index):
    r = avanza.get_watchlists()[watchlist_index].get('orderbooks')
    min_values = [float('inf'), float('inf')]  # To store the two smallest values

    for z in r:
        warrant_info = avanza.get_warrant_info(str(z)).get("quote").get("sell")
        cu = 0.1 if warrant_info is None else warrant_info

        # Update the two smallest values
        if cu < min_values[0]:
            min_values = [cu, min_values[0]]
        elif cu < min_values[1]:
            min_values[1] = cu

    # Check if either of the two smallest values is less than 0.8
    if min_values[0] < 0.8 or min_values[1] < 0.8:
        return 1
    return 0

def Long_Order_check():
    return check_orders(0)

def Short_Order_check():
    return check_orders(2)

def Combined_Order_check():
    if Long_Order_check() == 1 or Short_Order_check() == 1:
        print("checking")
        Long_Remove_watchlist()
        Short_Remove_watchlist()
        Long_add_to_watchlist()
        Short_add_to_watchlist()
    else:
        print("check done")