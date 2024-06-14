# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:44:38 2017

@author: Tirtha
"""
Nt = 10000
def even_check(n):
    list_num = list(str(n))
    if '0' in list_num or '2' in list_num or '4' in list_num or '5' in list_num or '6' in list_num or '8' in list_num:
        return True

def rotateN(n):
    ln_num = len(str(n))
    str_num = str(n)
    result = [n]
    
    for i in range(ln_num-1):
        rotated = str_num[1:]+str_num[0]
        result.append(rotated)
        str_num = rotated
     
    return result   

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

def is_circular_prime(n):
    if even_check(n):
        return False
        
    if (not is_prime(n)):
        return False
    
    rot = rotateN(n)
    flag = True
    
    for i in range(len(rot)):
        if not is_prime(int(rot[i])):
            flag = False
    
    return flag

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

def circular_prime_count(N):
    result = []
    primes = primes_sieve(N)
    for i in primes:
        if is_circular_prime(i):
            result.append(i)
    return len(result)
n_result = circular_prime_count(Nt)+2

print ("Number of circular primes up to {} is as following: {}".format(Nt, n_result))
