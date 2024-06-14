# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:29:28 2017

@author: Tirtha
"""
"""
This program returns the largest palindrome from the product of two 3-digit number
"""

def is_palindrome(n):
    str_n = str(n)
    if str_n == str_n[-1:0:-1]+str_n[0]:
        return True
    else:
        return False

max = 0
max_i=0
max_j=0

#flag = False
for i in range (999,99,-1):
    for j in range (999,99,-1):       
        if is_palindrome(i*j) and i*j > max:
            max = i*j
            max_i=i
            max_j=j
            #flag = True
            break
        #break
"""
for item in lst:
    if is_palindrome(item) and item > max:
        max = item
"""
print ("Largest palindrome from the product of two 3-digit numbers is {}. It is product of {} and {}".format(max,max_i,max_j))
