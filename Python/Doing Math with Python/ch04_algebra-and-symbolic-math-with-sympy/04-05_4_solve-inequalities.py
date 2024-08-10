'''
Purpose: Solve single-variable inequality functions
Author: Yasen Zhao
Date: 2024/02/21
'''

from sympy import sympify, Symbol, SympifyError, pprint
from sympy.core.relational import Relational, Equality
from sympy import Poly
from sympy import solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality

def isolve(ineq_obj):
    x = Symbol('x')
    
    lhs = ineq_obj.lhs
    rel = ineq_obj.rel_op
    
    if lhs.is_polynomial():
        p = Poly(lhs, x)
        return solve_poly_inequality(p, rel)
    elif lhs.is_rational_function():
        numer, denom = lhs.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        return solve_rational_inequalities([[((p1, p2), rel)]])
    else:
        return solve_univariate_inequality(ineq_obj, x, relational=False)

if __name__ == '__main__':
    ineq = input('Enter one inequality function to solve (single variable as "x"): ')
    try:
        ineq_obj = sympify(ineq)
    except SympifyError:
        print("Invalid Expression Input!")
    else:
        if isinstance(ineq_obj, Relational) and not isinstance(ineq_obj, Equality):
            pprint(isolve(ineq_obj))
        else:
            print('Invalid inequality expression')