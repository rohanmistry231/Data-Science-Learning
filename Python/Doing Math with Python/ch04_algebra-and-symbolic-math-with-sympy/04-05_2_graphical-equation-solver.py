'''
Purpose: Graphical Equation Solver
Author: Yasen Zhao
Date: 2024/02/21
'''

from sympy import Symbol, solve, sympify, SympifyError
from sympy.plotting import plot

def solve_plot_equation(expr1, expr2, x, y):
    # Solve
    solution = solve((expr1, expr2), dict=True)
    print(solution)
    if solution:
        print('x:{0} y:{1}'.format(solution[0][x],solution[0][y]))
    else:
        print('no solution found!')
    
    # Plotting
    eq1_y = solve(expr1,'y')[0]
    eq2_y = solve(expr2,'y')[0]
    plot(eq1_y, eq2_y, legend=True)


if __name__ == '__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print("Invalid Input")
    else:
        x = Symbol('x')
        y = Symbol('y')
        solve_plot_equation(expr1, expr2, x, y)