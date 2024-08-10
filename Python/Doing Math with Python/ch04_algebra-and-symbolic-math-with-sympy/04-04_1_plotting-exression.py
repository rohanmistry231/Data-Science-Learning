'''
Purpose: Plot the graph of an input expression by user
Author: Yasen Zhao
Date: 2024-02-20
'''

from sympy import Symbol, sympify, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def plot_expression(expr):
    y = Symbol('y')
    # Question: no need 'x' definition as Symbol? It's working
    print(expr)
    solutions = solve(expr,y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__ == '__main__':
    expr = input('Please enter one expression with x and y: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr)