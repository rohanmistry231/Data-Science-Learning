'''
Purpose: Draw a Square
Author: Yasen Zhao
Date: 2024/2/27
'''

import matplotlib.pyplot as plt

def draw_square():
    ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
    square = plt.Polygon([(1,1),(5,1),(5,5),(1,5)], closed=True)
    ax.add_patch(square)
    plt.show()

if __name__ == '__main__':
    draw_square()