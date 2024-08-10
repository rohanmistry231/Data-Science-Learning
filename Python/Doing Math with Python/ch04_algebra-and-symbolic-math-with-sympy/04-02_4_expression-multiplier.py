'''
Purpose: product of two expressions
Author: Yasen Zhao
Date: 2024/02/19
'''

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    prod = expand(expr1*expr2)
    print(prod)

if __name__ == '__main__':
    expr1 = input('Enter the first expression: ')
    expr2 = input('Enter the second expression: ')
    
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print("Invalid input")
    else:
        product(expr1, expr2)