'''
Purpose: draw two lines in one plot
Author: Yasen Zhao
Date: 2024/02/20
'''

from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')

p = plot(2*x+3, 5*x+1, x*x-5, legend=True, show=False)

p[0].line_color = 'b'
p[1].line_color = 'r'

p.show()