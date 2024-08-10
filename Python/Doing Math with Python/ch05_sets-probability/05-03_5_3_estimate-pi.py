'''
Purpose: Estimate the value of pi
Author: Yasen Zhao
Date: 2024/02/25
'''

import math
import random

def estimate(total_point):
    radius = 1
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
        
    total_points = [1000, 100000, 1000000, 10000000]
    
    for points in total_points:
        print('Known Pi Value: {0}. Estimated Pi: {1:.5f}'.format(math.pi, estimate(points)))
    