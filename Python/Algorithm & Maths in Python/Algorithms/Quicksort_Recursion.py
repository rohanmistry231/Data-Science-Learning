# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:28:05 2018

@author: Tirtha
"""

def quicksort(lst):
    #count_op=0
    if lst==[]:
        return (lst)
    else:
        pivot=lst[0]
        smaller_lst = [n for n in lst if n<pivot]
        pivot_lst = [n for n in lst if n==pivot]
        greater_lst = [n for n in lst if n>pivot]
        
        return (quicksort(smaller_lst)+pivot_lst+quicksort(greater_lst))

import random

N_test=20
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))

print("Original list:",test_lst)
print("Sorted list:",quicksort(test_lst))