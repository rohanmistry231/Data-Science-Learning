'''
Purpose: Better Correlation Coefficient-Finding
Author: Yasen Zhao
Date: 2024/02/18
'''

def find_corr_x_y(x,y):
    
    if len(x) != len(y):
        print('The two datasets has different numbers of elements')
        return None # "None" can be checked as False in boolean
    
    n = len(x)
    
    # Find the sum of the products
    
    # method 1 using zip()
    # prod = []
    # for xi, yi in zip(x,y):
    #     prod.append(xi*yi)
    
    # method 2:
    prod = [xi*yi for xi,yi in zip(x,y)]
    
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
    # x = [1,2,3,6,4]
    # y = [5,8,2,5,3]
    x = [1,2,3,4,5]
    y = [10,8,6,4,2,3]
    corr = find_corr_x_y(x,y)
    if not corr:
        print('Correlation coefficient could not be calcuated!')
    else:
        print('The correlation of {0} and {1} is: {2}'.format(x, y, corr))