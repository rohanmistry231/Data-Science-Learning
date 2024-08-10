'''
Purpose: Saving Graph Image using savefig
Author: Yasen Zhao
Date: 2024/02/13
'''

import matplotlib.pyplot as plt

def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]
    
    plt.plot(x_numbers, y_numbers)
    # plt.show()
    plt.savefig('mygraph.png')

if __name__ == '__main__':
    create_graph()