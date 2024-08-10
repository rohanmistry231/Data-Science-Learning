'''
Purpose: Culculate the value of a series
Author: Yasen Zhao
Date: 2024/02/19
'''

from sympy import Symbol, pprint, init_printing

def print_series(n, x_value):
    
    init_printing(order='rev-lex')
    
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x ** i)/i
    pprint(series)
    
    series_value = series.subs({x:x_value})
    print('Value of the series as {0:.2f} is {1:.2f}'.format(x_value, series_value))

if __name__ == '__main__':
    n = int(input('Enter the number of terms you want in series: '))
    x_value = float(input('Enter the value of x for evaluating: '))
    print_series(n, x_value)