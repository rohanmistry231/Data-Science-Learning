'''
Purpose: using higher-order derivatives to find maxima and minima
Author: Yasen Zhao
Date: 2024/03/01
'''

from sympy import Symbol, Derivative, solve, pprint
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = Symbol('x')
    f = x**5 - 30 * x**3 + 50 * x
    pprint(f)
    x_min = -5
    x_max = 5
    d1 = Derivative(f,x).doit()
    critical_points = solve(d1)
    pprint(d1)
    pprint(critical_points)
    d2 = Derivative(f,x,2).doit()
    pprint(d2)
    
    A = critical_points[2]
    B = critical_points[0]
    C = critical_points[1]
    D = critical_points[3]
    
    print('=====Evaluatation on 2nd Order Derivative=====')
    print('Evaluate Point B: {0:.5f}'.format(d2.subs({x:B}).evalf()))
    print('Evaluate Point C: {0:.5f}'.format(d2.subs({x:C}).evalf()))
    print('Evaluate Point A: {0:.5f}'.format(d2.subs({x:A}).evalf()))
    print('Evaluate Point D: {0:.5f}'.format(d2.subs({x:D}).evalf()))
    
    print('=====Evaluatation on the boundary value=====')
    print('Evaluate Point x_min: {0:.5f}'.format(f.subs({x:x_min}).evalf()))
    print('Evaluate Point x_max: {0:.5f}'.format(f.subs({x:x_max}).evalf()))
    
    # Show in discrete curve plotting
    x_points = []
    y_points = []
    y1_points = []
    y2_points = []
    for i in range(-1000,1001):
        x_points.append(i/200)
        y_points.append(f.subs({x:i/200}))
        y1_points.append(d1.subs({x:i/200}))
        y2_points.append(d2.subs({x:i/200}))
    plt.plot(x_points, y_points, x_points, y1_points, x_points, y2_points)
    plt.show()