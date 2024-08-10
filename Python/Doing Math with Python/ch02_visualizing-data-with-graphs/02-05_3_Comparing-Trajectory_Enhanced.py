'''
Purpose: Enhanced Projectile Trajectory
Author: Yasen Zhao
Date: 2024/02/14
'''

from matplotlib import pyplot as plt
import math

g = 9.8

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

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title("Projectile motion of different initial velocities and angels")

def draw_trajectory(u, theta, t_flight):
    
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
    
    try:
        num_of_trajectories = int(input('How many trajectories (integer)? '))
        
        velocities = []
        angles = []
        
        for i in range(1, num_of_trajectories+1):
            v = input('Please enter the initial velocity for trajectory {0} (m/s): '.format(i))
            theta = input('Please enter the angle of projection for trajectory {0} (degrees): '.format(i))
            velocities.append(float(v))
            angles.append(math.radians(float(theta)))

    except ValueError:
        print("You entered an invalid input")
        
    else:
        for i in range(num_of_trajectories):
            t_flight = 2 * velocities[i] * math.sin(angles[i]) / g
            S_x = velocities[i] * math.cos(angles[i]) * t_flight
            S_y = velocities[i] * math.sin(angles[i]) * (t_flight / 2) - 0.5 * g * (t_flight / 2)**2
            print('Initial velocity: {0:.2f}, Angle of Projection: {1:.2f}'.format(velocities[i], math.degrees(angles[i])))
            print('T: {0:.2f}, S_x: {1:.2f}, S_y: {2:.2f}'.format(t_flight, S_x, S_y))
            print()
            draw_trajectory(velocities[i], angles[i], t_flight)

        legends = []
        for i in range(0, num_of_trajectories):
            legends.append('{0:.2f} - {1:.2f}'.format(velocities[i], math.degrees(angles[i]))) 
        plt.legend(legends)
        
        plt.show()
        

