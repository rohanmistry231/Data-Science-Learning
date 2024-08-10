'''
Purpose: Draw Scatter Plots
Author: Yasen Zhao
Date: 2024/02/17
'''

import matplotlib.pyplot as plt

def find_corr_x_y(x,y):
    n = len(x)
    
    # Find the sum of the products
    prod = []
    for xi, yi in zip(x,y):
        prod.append(xi*yi)
    
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2
    
    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    x_square_sum = sum(x_square)
    
    y_square = []
    for yi in y:
        y_square.append(yi ** 2)
    y_square_sum = sum(y_square)
    
    # use formula to calculate correlation
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    
    correlation = numerator / denominator
    
    return correlation

if __name__ == '__main__':
    
    x1 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]

    y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

    x2 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]

    y2 = [9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]

    x3 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]

    y3 = [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

    x4 = [8.0,8.0,8.0,8.0,8.0,8.0,8.0,19.0,8.0,8.0,8.0]

    y4 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89]
    
    if (len(x4)==len(y4)):
        print('The correlation of \n{0} \nand \n{1} \nis: {2:.5f}'.format(x4, y4, find_corr_x_y(x4,y4)))
    else:
        print('dismatch on the data sets length')

    plt.scatter(x4,y4)

    # plt.scatter(x2,y2)

    # plt.scatter(x3,y3)

    # plt.scatter(x4,y4)

    plt.show()