'''
Purpose: example of using matplotlib's Circle patch
Author: Yasen Zhao
Date: 2024/02/25
'''

import matplotlib.pyplot as plt

def create_circle():
    circle = plt.Circle((0,0), radius = 0.5, fc='g', ec='r')
    # fc - face color, ec - edge color
    return circle

def show_shape(patch):
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.add_patch(patch)    
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = create_circle()
    show_shape(c)