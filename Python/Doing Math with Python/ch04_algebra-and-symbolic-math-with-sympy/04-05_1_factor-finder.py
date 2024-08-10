'''
Purpose: Factor Finder, using factor()
Author: Yasen Zhao
Date: 2024/02/20
'''

from sympy import factor, sympify, SympifyError

def factorize(expr):
    return factor(expr)

if __name__ == '__main__':
    expr = input('Please input one expression for facotrizing: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print("Invalid Input")
    else:
        print(factorize(expr))