'''
Purpose: demo how to catch error in Simpify
Author: Yasen Zhao
Date: 2024/02/19
'''

from sympy import sympify
from sympy.core.sympify import SympifyError

expr = input('Enter a methematical expression: ')

try:
    expr = sympify(expr)
except SympifyError:
    print('Invalid Input')
else:
    print(expr)