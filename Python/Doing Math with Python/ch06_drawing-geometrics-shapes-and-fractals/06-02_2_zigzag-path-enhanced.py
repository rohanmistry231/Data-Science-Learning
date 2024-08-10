'''
Purpose: Zigzag path enhanced to all of 4 direction
Author: Yasen Zhao
Date: 2024/02/27
'''

import random
import matplotlib.pyplot as plt

def transformation_1(p):
    x = p[0]
    y = p[1]
    p = (x+1, y-1)
    return p

def transformation_2(p):
    x = p[0]
    y = p[1]
    p = (x+1, y+1)
    return p

def transformation_3(p):
    x = p[0]
    y = p[1]
    p = (x-1, y-1)
    return p

def transformation_4(p):
    x = p[0]
    y = p[1]
    p = (x-1, y+1)
    return p

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    t = random.choice(transformations)
    p = t(p)
    return p

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    # initial point
    p = (0,0)
    n = int(input('Enter the number of iterations: '))
    x, y = build_trajectory(p, n)
    # print(x, y)
    # plotting
    plt.plot(x,y)
    plt.show()