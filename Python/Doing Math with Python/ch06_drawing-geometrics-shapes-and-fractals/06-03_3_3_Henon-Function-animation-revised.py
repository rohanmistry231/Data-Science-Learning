'''
Purpose: plot one 20,000 interations of the Henon's Function (dynamic)
Author: Yasen Zhao
Date: 2024/02/27
'''

import matplotlib.pyplot as plt
from matplotlib import animation

def transform(p):
    x, y = p
    x1 = y + 1.0 - 1.4 * x * x
    y1 = 0.3 * x
    p = (x1, y1)
    return p

def update_points(i, x, y, plot):
    plot.set_data(x[:i], y[:i])
    return plot

if __name__ == '__main__':
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    n = int(input("Enter the numbers of iterations: "))
    for i in range(1,n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    fig = plt.gcf()
    ax = plt.axes(
        xlim = (min(x), max(x)),
        ylim = (min(y), max(y))
    )
    plot = plt.plot([], [], 'o')[0]
    anim = animation.FuncAnimation(
        fig,
        update_points,
        fargs = (x, y, plot),
        frames = len(x),
        interval = 2
    )
    # plt.plot(x, y, 'o')   # this is one wrongly duplicated line
    plt.title('Animated Henon Function')
    plt.show()