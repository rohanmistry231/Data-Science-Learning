'''
Purpose: create one growing circle
Author: Yasen Zhao
Date: 2024/02/25
'''

import matplotlib.pyplot as plt
from matplotlib import animation

def create_circle():
    circle = plt.Circle((0,0), radius = 0.05, fc='g', ec='r')
    # fc - face color, ec - edge color
    return circle

def update_radius(i, circle):
    circle.radius = i * 0.5
    return circle

def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)    
    anim = animation.FuncAnimation(
        fig,
        update_radius,
        fargs = (circle,),
        frames = 20,
        interval = 50,
        repeat = True
    )
    plt.title('Simple Circle Animation')
    plt.show()

if __name__ == '__main__':
    create_animation()