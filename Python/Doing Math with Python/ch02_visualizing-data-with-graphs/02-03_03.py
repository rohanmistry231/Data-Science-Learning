'''
Purpose: Simple plot using pyplot from matplotlib
Author: Yasen Zhao
Date: 2024/02/13
'''

import matplotlib.pyplot

def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]
    
    matplotlib.pyplot.plot(x_numbers, y_numbers)
    matplotlib.pyplot.show()

if __name__ == '__main__':
    create_graph()