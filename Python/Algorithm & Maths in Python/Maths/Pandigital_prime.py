# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:51:07 2017

@author: Tirtha
"""

import math

def is_prime(n):
    if n< 0:
        return False
    elif n == 0 or n==1:
        return False
    elif n==2:
        return True
    elif (str(n)[-1] == '2') or (str(n)[-1] == '4') or (str(n)[-1] == '6') or (str(n)[-1] == '8'):
        return False
    elif (str(n)[-1]=='5' and n!=5):
        return False
    elif (str(n)[-1]=='0'):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+2):
            if (n%i == 0):
                #print ("Not a prime")
                return False
        else:
            #print ("Prime!")
            return True

def is_pandigital(n,m):
	strn = str(n)
	#strl = len(strn)
	flag = True
	count=1
	for i in range(1,m+1):
		count = count*strn.count(str(i))
	if count!=1:
		return False
	else:
		return True
	
	#return flag

max = 0

for i in range(9876543,1234567,-1):
	if is_pandigital(i,7):
		if is_prime(i):
			max = i
			break

print (max)
