'''
Purpose: Finding the length of a given curve(function)
Author: Yasen Zhao
Date: 2024/03/02
'''

from sympy import Integral, Derivative, sqrt, Symbol, sympify, SympifyError

def find_length(f, var, a, b):
    d = Derivative(f, var).doit()
    length = Integral(sqrt(1+d**2), (var, a, b)).doit().evalf()
    return length

if __name__ == '__main__':
    
    f = input('Enter the function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the lower limit of the variable: '))
    b = float(input('Enter the upper limit of the variable: '))
    
    try:
        f = sympify(f)
    except SympifyError:
        print('Your input functions is entered invalid!')
    else:
        var = Symbol(var)
        length = find_length(f, var, a, b)
        print('Length of function {0} between {1:.3f} and {2:.3f} is: {3:.3f}.'.format(f, a, b, length))