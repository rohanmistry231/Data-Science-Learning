'''
Purpose: Draw the trajectory of a body in porjectile motion
Author: Yasen Zhao
Date: 2024/02/13
'''

'''
Generate equally spaced floating point
numbers between two given values
'''
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title("Projectile motion of a object")

def draw_trajectory(u, theta):
    
    theta = math.radians(theta)
    g = 9.8
    
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g
    
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)
    
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
    
    draw_graph(x, y)

if __name__ == '__main__':
    # try:
    #     u = float(input("Enter the initial velocity (m/s): "))
    #     theta = float(input("Enter the angle of projections (degrees): "))
    # except ValueError:
    #     print("You entered an invalid input")
    # else:
    #     draw_trajectory(u, theta)
    #     plt.show()    
    
    # # List of three different initial velocities
    # u_list = [20, 40, 60]
    # theta = 45
    # for u in u_list:
    #     draw_trajectory(u, theta)
    # plt.legend([20, 40, 60])
    # plt.show()
    
    # List of three different initial angle
    u = 40
    theta_list = [10, 30, 50, 70, 90, 110]
    for theta in theta_list:
        draw_trajectory(u, theta)
    plt.legend([10, 30, 50, 70, 90, 110])
    plt.show()