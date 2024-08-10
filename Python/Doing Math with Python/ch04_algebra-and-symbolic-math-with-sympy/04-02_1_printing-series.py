'''
Purpose: print the series
Author: Yasen Zhao
Date: 2024/02/19
'''

from sympy import Symbol, pprint, init_printing

def print_series(n):
    
    init_printing(order='rev-lex')
    
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x ** i)/i
    pprint(series)

if __name__ == '__main__':
    n = int(input('Enter the number of terms you want in series: '))
    print_series(n)