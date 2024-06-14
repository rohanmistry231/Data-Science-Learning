# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:59:36 2018

@author: Tirtha
"""

"""
Simple recursive program to generate the sequence of coins (of value 3 and 5) for any amount > 8.
This can be used to show that any integer amount of money (> 8) can be paid using coins of 3 and 5. 
"""
def coins2pay(amount):
    # Base cases
    if amount==8:
        return [3,5]
    elif amount==9:
        return [3,3,3]
    elif amount==10:
        return [5,5]
    # Recursive case
    else:
        coins=coins2pay(amount-3)
        coins.append(3)
        return coins