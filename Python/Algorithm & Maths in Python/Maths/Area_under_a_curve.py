# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:31:45 2018

@author: Tirtha
"""
import math
def area (func,low,high,stepsize=0.01):
    """
    Accepts arbitrary function of single variable and calculates the area under the curve between 'low'
    and 'high' limits. Stepsize for numerical approximation can be chosen by user or set to 0.01 by default
    """
    area=0
    iter_count=0
    while (low<high):
        fx1 = func(low-stepsize)
        fx2 = func(low+stepsize)
        area+=math.fabs((fx1+fx2)*stepsize*(1/2))
        low+=stepsize
        iter_count+=1
    return (area,iter_count)

# Test function
def f(x):
    f = (0.2*x**2+3*x+2)*np.sin(x)
    return (f)

# Test parameters
low = 5
high = 10
result,iter_count = area(f,low,high)
print("Area under the curve from {} to {} is {}\nTook {} steps to calculate".format(low,high,result,iter_count))

# Plot the function
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(low,high,num=100)
y=f(x)

plt.plot(x,y,lw=3)
plt.grid(True)
plt.show()
    
