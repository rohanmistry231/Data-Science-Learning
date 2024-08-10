'''
Purpose: Derivative Calculator
Author: Yasen Zhao
Date: 2024/02/29
'''

from sympy import sympify, SympifyError, Symbol, Derivative, pprint

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var)
    print(d.doit())
    pprint(d.doit())

if __name__ == '__main__':
    f = input('Enter a function: ')
    var = input('Enter the variable to differentiate with respect to: ')
    
    try:
        f = sympify(f)
    except SympifyError:
        print('Invavid input.')
    else:
        derivative(f, var)