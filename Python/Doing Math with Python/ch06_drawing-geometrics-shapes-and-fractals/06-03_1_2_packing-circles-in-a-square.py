'''
Purpose: Packing Circles into a Square
Author: Yasen Zhao
Date: 2024/2/27
'''

import matplotlib.pyplot as plt

def draw_square():
    square = plt.Polygon(
        [(1,1),(edge_length+1,1),(edge_length+1,edge_length+1),(1,edge_length+1)],
        closed=True
    )
    return square

def draw_circle(p, r):
    circle = plt.Circle(p, radius=r, fc = 'y')
    return circle

if __name__ == '__main__':
    edge_length = int(input("Enter the edge length of square: "))
    radius = float(input("Enter the radius of circle to pack inside: "))
    ax = plt.gca()
    s = draw_square()
    ax.add_patch(s)
    y = 1+radius
    while y < edge_length+1:
        x = 1+radius
        while x < edge_length+1:
            p = (x,y)
            c = draw_circle(p, radius)
            ax.add_patch(c)
            x += 2 * radius
        y += 2 * radius
    plt.axis('scaled')
    plt.show()