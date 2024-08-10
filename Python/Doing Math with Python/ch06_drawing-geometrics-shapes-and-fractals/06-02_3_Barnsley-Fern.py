'''
Purpose: Barnsley Fern
Reference link: https://en.wikipedia.org/wiki/Barnsley_fern#Construction
Author: Yasen Zhao
Date: 2024/02/27
'''

import random
import matplotlib.pyplot as plt

def transformation_1(p):
    x = p[0]
    y = p[1]
    p = (0.85*x+0.04*y, -0.04*x+0.85*y+1.6)
    return p

def transformation_2(p):
    x = p[0]
    y = p[1]
    p = (0.2*x-0.26*y, 0.23*x+0.22*y+1.6)
    return p

def transformation_3(p):
    x = p[0]
    y = p[1]
    p = (-0.15*x+0.28*y, 0.26*x+0.24*y+0.44)
    return p

def transformation_4(p):
    x = p[0]
    y = p[1]
    p = (0, 0.16*y)
    return p

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    # print(sum_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [0.85, 0.07, 0.07, 0.01]
    tindex = get_index(probability)
    t = transformations[tindex]
    p = t(p)
    return p

def draw_fern(p, n):
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
    n = int(input('Enter the number of points in the Fern: '))
    x, y = draw_fern(p, n)
    # print(x, y)
    # plotting
    plt.plot(x,y,'*')
    plt.title('Fern with {0} points'.format(n))
    plt.show()