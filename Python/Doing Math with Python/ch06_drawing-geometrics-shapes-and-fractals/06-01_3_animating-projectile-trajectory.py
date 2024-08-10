'''
Purpose: Animate the trajectory of an object in projectile motion
Author: Yasen Zhao
Date: 2024/02/25
'''

import matplotlib.pyplot as plt
from matplotlib import animation
import math

g = 9.8

def get_intervals(u, theta):
    t_flight = 2 * u * math.sin(theta) / g
    print(t_flight)
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start += interval
    print(intervals)
    return intervals

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * math.cos(theta) * t
    y = u * math.sin(theta) * t - 0.5 * g * t * t
    circle.center = x, y
    return circle

def create_animation(u, theta):
    
    intervals = get_intervals(u, theta)
    
    tmax = u * math.sin(theta) / g
    xmin = 0
    xmax = u * math.cos(theta) * intervals[-1]
    ymin = 0
    ymax = u * math.sin(theta) * tmax - 0.5 * g * tmax * tmax
    
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    # ax.set_aspect('equal')
    circle = plt.Circle((xmin, ymin), 3.0)
    ax.add_patch(circle)    
    anim = animation.FuncAnimation(
        fig,
        update_position,
        fargs = (circle, intervals, u, theta),
        frames = len(intervals),
        interval = 2,
        repeat = True
    )
    plt.title('Projectile Motion Demo')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('Pleae enter valid input')
    else:
        theta = math.radians(theta)
        create_animation(u, theta)