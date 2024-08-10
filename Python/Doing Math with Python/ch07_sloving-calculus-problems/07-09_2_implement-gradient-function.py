'''
Purpose: use Gradient Ascent to find the maximum value of a single-variable function
Enhance: add checking for existence of a solutionfor the quation f'(x)=0
Author: Yasen Zhao
Date: 2024/03/01
'''

from sympy import Symbol, Derivative, sympify, solve
import matplotlib.pyplot as plt

def gradient_ascent(x0, f1x, x):
    # check whether f1x=0 has a solution
    if not solve(f1x):
        print('Cannot continue, solution for {0}=0 does not exist.'.format(f1x))
        return
    
    epcilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size * f1x.subs({x:x_old}).evalf()
    X_traversed = []
    while abs(x_old - x_new) > epcilon:
        X_traversed.append(x_new)
        x_old = x_new
        x_new = x_old + step_size * f1x.subs({x:x_old}).evalf()
    return x_new, X_traversed

def gradient_descent(x0, f1x, x):
    # check whether f1x=0 has a solution
    if not solve(f1x):
        print('Cannot continue, solution for {0}=0 does not exist.'.format(f1x))
        return
    
    epcilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old - step_size * f1x.subs({x:x_old}).evalf()
    X_traversed = []
    while abs(x_old - x_new) > epcilon:
        X_traversed.append(x_new)
        x_old = x_new
        x_new = x_old - step_size * f1x.subs({x:x_old}).evalf()
    return x_new, X_traversed

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers

def create_plot(X_traversed, f, var):
    x_val = frange(-6, 6, 0.01)
    f_val = [f.subs({var:x}) for x in x_val]
    plt.plot(x_val, f_val, 'o')
    f_traversed = [f.subs({var:x}) for x in X_traversed]
    plt.plot(X_traversed, f_traversed, 'r.')
    plt.legend(['Function', 'Intermediat point'], loc='best')
    plt.show()

if __name__ == '__main__':
    f = input('Enter a function with one variable: ')
    var = input('Enter the variable to differentite with respect to: ')
    var0 = float(input('Enter the initial value of the variable (float number): '))
    choice = int(input('Choose Global Maximum (1) or Global Minimum (2): '))
    
    try:
        f = sympify(f)
    except:
        print('Invalid function entered!')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        if choice == 1:
            var_max, X_traversed = gradient_ascent(var0, d, var)
            if var_max:
                print('{0}: {1:.5f}'.format(var.name, var_max))
                print('Maximum Range: {0:.5f}'.format(f.subs({var:var_max})))
        else:
            var_min, X_traversed = gradient_descent(var0, d, var)
            if var_min:
                print('{0}: {1:.5f}'.format(var.name, var_min))
                print('Minimum Range: {0:.5f}'.format(f.subs({var:var_min})))
        create_plot(X_traversed, f, var)