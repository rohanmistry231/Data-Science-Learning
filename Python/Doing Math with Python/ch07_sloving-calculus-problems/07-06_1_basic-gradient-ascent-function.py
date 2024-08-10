'''
Purpose: use Gradient Ascent to find the angle at which
the projectile has max range for a given velocity (e.g. 25m/s)
Author: Yasen Zhao
Date: 2024/03/01
'''

import math
from sympy import Symbol, Derivative, sin, pprint

def gradient_ascent(theta0, R1theta, x):
    epcilon = 1e-6
    step_size = 1e-4
    x_old = theta0
    x_new = x_old + step_size * R1theta.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epcilon:
        x_old = x_new
        x_new = x_old + step_size * R1theta.subs({x:x_old}).evalf()
    return x_new

def find_max_theta(R, theta):
    # Calculate the first derivative
    R1theta = Derivative(R, theta).doit()
    # print(R1theta)
    theta0 = 1e-3
    theta_max = gradient_ascent(theta0, R1theta, theta)
    return theta_max

if __name__ == '__main__':
    g = 9.8
    # Get initial velocity
    u = int(input("Enter the initial velocity (e.g. 25 m/s): "))
    # Expression for range
    theta = Symbol('theta')
    R = u**2 * sin(2*theta) / g
    # pprint(R)
    theta_max = find_max_theta(R, theta)
    # print(theta_max)
    print('Theta: {0:.5f}'.format(math.degrees(theta_max)))
    print('Maximum Range: {0:.5f}'.format(R.subs({theta:theta_max})))
    