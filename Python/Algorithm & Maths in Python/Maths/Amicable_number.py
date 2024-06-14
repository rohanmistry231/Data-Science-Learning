# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:51:59 2017
@author: Tirtha

Search for all amicable number pairs up to 10,000 and finding their sum
#Barebne code
"""
import math
def divisor_sum(n):
    div_sum=1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            div_sum+=i
            if (i*i!=n):
                div_sum+=int((n/i))
    return div_sum

def is_amicable(a,b):
    if (divisor_sum(a)==b and divisor_sum(b)==a):
        return True
    else:
        return False

result = 0
lsta =[]
lstb= []
k=0
while k<10:
    for i in range(1000*k,1000*(k+1)):
        for j in range (i+1,min([10000,2*i])):
            if is_amicable(i,j):
                lsta.append(i)
                lstb.append(j)
                result+=i+j
    print ("Finished loop for {}\n".format(k))
    k+=1
print (result)
 