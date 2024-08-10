'''
Purpose: plot one 20,000 interations of the Henon's Function (static)
Author: Yasen Zhao
Date: 2024/02/27
'''

import matplotlib.pyplot as plt

def transform(p):
    x, y = p
    x1 = y + 1.0 - 1.4 * x * x
    y1 = 0.3 * x
    p = (x1, y1)
    return p

if __name__ == '__main__':
    p = (0, 0)
    # print(p)
    x = [p[0]]
    y = [p[1]]
    n = int(input("Enter the numbers of iterations: "))
    for i in range(1,n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    # print(p)
    plt.plot(x, y, 'o')
    plt.show()