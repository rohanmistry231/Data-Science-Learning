'''
Purpose: read from online trend csv file and do plotting
Author: Yasen Zhao
Date: 2024/02/18
'''

import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        summer = []
        autumn = []
        for row in reader:
            summer.append(float(row[1]))
            autumn.append(float(row[2]))
        return summer, autumn

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel("Summer")
    plt.ylabel("Autumer")
    plt.show()

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
    summer, autumn = read_csv('multiTimeline.csv')
    scatter_plot(summer,autumn)
    corr = find_corr_x_y(summer,autumn)
    print('Correlation: {0:.2f}'.format(corr))