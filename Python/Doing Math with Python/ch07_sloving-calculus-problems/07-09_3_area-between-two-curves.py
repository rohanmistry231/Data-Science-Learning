'''
Purpose: calculate area between two given curves
Author: Yasen Zhao
Date: 2024/03/02
'''

from sympy import Integral, Symbol, sympify, SympifyError

def find_area(f, g, var, a, b):
    area1 = Integral(f - g, (var, a, b)).doit()
    area2 = Integral(g - f, (var, a, b)).doit()
    return area1, area2

if __name__ == '__main__':
    
    f = input('Enter the upper function in one variable: ')
    g = input('Enter the lower function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the lower bound of the enclosed region: '))
    b = float(input('Enter the upper bound of the enclosed region: '))
    
    try:
        f = sympify(f)
        g = sympify(g)
    except SympifyError:
        print('One of your input functions is entered invalid!')
    else:
        var = Symbol(var)
        area1, area2 = find_area(f, g, var, a, b)
        print('Area between function {0} and {1} is: {2} or {3}.'.format(f, g, area1, area2))