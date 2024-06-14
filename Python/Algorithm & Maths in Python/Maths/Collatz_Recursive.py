# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:01:52 2018

@author: Tirtha
"""
"""
This function computes the length of a collatz sequence by recursion. It does not store the sequence.
It also determines the longest Collatz sequence up to some given number.
"""
import time
t1=time.time()
def collatz_length(seed,count):
    # Base case
    n=seed
    if n==1:
        return count
    elif (n%2==0):
        return collatz_length(n/2,count+1)
    else:
        return collatz_length(3*n+1,count+1)

Nt = 60000
result = []
for i in range(2,Nt+1):
    result.append(collatz_length(i,0))

num = 2 + result.index(max(result))

print ("\nThe longest sequence has {rt} terms and it is produced by the number {num2}".format(rt = max(result), num2 = num))

t2=time.time()
print("Time taken",t2-t1)
