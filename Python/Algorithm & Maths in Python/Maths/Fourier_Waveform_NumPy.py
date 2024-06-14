# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:41:53 2017

@author: Tirtha
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 10, 6

# Fourier series of Triangular Waveform
#===============================================
x = np.linspace(-2*np.pi,2*np.pi, 200)
#y = (8/(np.pi**2))*np.sin(x)
#plt.plot(x,y)
# Feel free to change the numbers '57' and '5' around to see what happens
for j in range(4,57,5):
    y = (8/(np.pi**2))*np.sin(x)
    for i in range(3,j):
        if i%2!=0:
            y += (8/(np.pi**2))*((-1)**((i-1)/2))*(1/i**2)*np.sin(i*x)

plt.plot(x,y)

plt.title("Fourier approx. of triangular waveform", fontsize=20)
plt.xlabel("Time-scale", fontsize=20)
plt.ylabel("Magnitude", fontsize=20)
plt.show()

# Fourier series of Square Waveform
#===============================================
x = np.linspace(-2*np.pi,2*np.pi, 200)
y = (4/(np.pi))*np.sin(x)
#plt.plot(x,y)

# Feel free to change the numbers '57' and '5' around to see what happens
for j in range(4,57,5):
    y = (4/(np.pi))*np.sin(x)
    for i in range(3,j):
        if i%2!=0:
            y += (4/(np.pi))*(1/i)*np.sin(i*x)
            
plt.plot(x,y)

plt.title("Fourier approx. of square waveform", fontsize=20)
plt.xlabel("Time-scale", fontsize=20)
plt.ylabel("Magnitude", fontsize=20)
plt.show()