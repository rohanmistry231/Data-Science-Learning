'''
Purpose: Verify the continuity of a Function at a Point
Author: Yasen Zhao
Date: 2024/03/01
'''

from sympy import Symbol, sympify, SympifyError, Limit

def check_continuity(f, var, a):
    f_val = f.subs({var:a})
    lim1 = Limit(f, var, a, dir="+").doit()
    lim2 = Limit(f, var, a, dir="-").doit()
    
    if f_val == lim1 and lim1 == lim2:
        print('{0} is continuity at {1}'.format(f, a))
    else:
        print('{0} is NOT continuity at {1}'.format(f, a))

if __name__ == '__main__':
    f = input('Enter a function with single variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the point to check the continuity at: '))
    
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered!')
    else:
        var = Symbol(var)
        check_continuity(f, var, a)