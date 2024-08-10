'''
Purpose: Visualize Quadratic Function
Author: Yasen Zhao
Date: 2024/02/14
'''

import matplotlib.pyplot as plt

def draw_graph(x1, y1, x2, y2):
    plt.plot(x1, y1, x2, y2)
    plt.legend(["y=x**2 + 2*x + 1", "y=-x**2 + 2*x + 1"])
    plt.show()

if __name__ == '__main__':
    x_values = range(-100, 102, 2)
    y1_values =[]
    y2_values =[]    
    for x in x_values:
        function1 = x**2 + 2*x + 1
        function2 = -x**2 + 2*x + 1
        y1_values.append(function1)
        y2_values.append(function2)
    draw_graph(x_values, y1_values, x_values, y2_values)