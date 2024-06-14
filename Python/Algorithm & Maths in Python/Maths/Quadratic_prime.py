# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:59:25 2017

@author: Tirtha
"""
"""
Considering quadratics of the form:
n^2+a*n+b, where |a|<1000 and |b|≤1000, and |n| is the modulus/absolute value of n

This program finds the product of the coefficients, a and b, for the quadratic 
expression that produces the maximum number of primes for consecutive values 
of n, starting with n=0.
"""
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
        for i in range(2,int(pow(n-1,0.5))+2):
            if (n%i == 0):
                #print ("Not a prime")
                return False
        else:
            #print ("Prime!")
            return True

lst =[]
lsta =[]
lstb =[]
maxn = 0
for i in range(-100,100):
    for j in range (-100,100):
        n = 0
        while is_prime(n**2+i*n+j):
            n+=1
        lst.append(n-1)
        lsta.append(i)
        lstb.append(j)

a = lsta[lst.index(max(lst))]
b = lstb[lst.index(max(lst))]

print ("Longest prime sequence is {} numbers".format(max(lst)))

print ("Product of the coefficients of the quadratic prime producing longest sequence is {}".format(a*b))
