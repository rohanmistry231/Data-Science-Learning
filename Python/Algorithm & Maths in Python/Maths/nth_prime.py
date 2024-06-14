# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:53:34 2017

@author: Tirtha
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
i=0
n=1
final_n=2

Nt = int(input("Enter n, where you want to determine nth prime: "))

while True:
    n+=1
    if is_prime(n):
        i+=1
        if i==Nt:
            final_n = n
            break
    
print ("{}-th prime is {}".format(Nt,final_n))
    