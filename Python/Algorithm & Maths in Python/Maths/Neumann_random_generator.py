# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 00:02:21 2017
@author: Tirtha

Generate 3- or 4-digit random numbers by Neumann Pseudo-Random generation process
"""
def Neumann_random_generator(seed):
    
    n = seed
    random = []
    random.append(n)
    count = 1

    while count<50000:
        m = 7*n**2+13*n**3+19*n**4
        strm = str(m)
        if len(strm) < 8:
            strm = '0'*(8-len(strm))+strm
        randn = int(strm[2:6])
        n = randn
        random.append(randn)
        #set_rnd = set(random)
        count +=1
#        if (len(set_rnd)!= len(random)) or (False):
#             random.pop()
#             break

    return (random)

ask_seed = int(input ("Please enter the seed:"))
r = Neumann_random_generator(ask_seed)

#for i in r:
    #print (i, end='  ')

# Plotting the histogram of the numbers to see distribution
import matplotlib.pyplot as plt

plt.hist(r,50, alpha=0.6)