'''
Purpose: Estimate the area of given circle (r) and plotting
Author: Yasen Zhao
Date: 2024/02/25
'''

import math
import random
import matplotlib.pyplot as plt

def estimate(radius, total_point):
    center = (radius, radius)
    area_of_square = (2*radius) ** 2
    in_circle = 0
    
    for i in range(total_point):
        x = random.uniform(0, 2 * radius)
        y = random.uniform(0, 2 * radius)
        p = (x, y)
        d = math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2)
        if d <= radius:
            in_circle = in_circle + 1   # can be "in_circle += 1"
    
    return (in_circle / total_point) * area_of_square

if __name__ == '__main__':
    radius = float(input('Enter the radius of circle: '))
    area_of_circle = math.pi * (radius ** 2)
    print('Radius: {0:.5f}, Area in theory: {1:.5f}'.format(radius, area_of_circle))
    
    total_points = range(1,1000)
    
    points_axis = []
    estimated_axis = []
    
    for points in total_points:
        points_axis.append(points)
        estimate_result = estimate(radius, points)
        # print('Estimated ({0} darts): {1:.5f}'.format(points, estimate_result))
        estimated_axis.append(estimate_result)
    
    plt.plot(points_axis, estimated_axis)
    plt.show()
    