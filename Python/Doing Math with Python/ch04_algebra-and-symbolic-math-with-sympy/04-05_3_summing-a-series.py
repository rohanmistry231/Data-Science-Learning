'''
Purpose: Summing an arbitrary series
Author: Yasen Zhao
Date: 2024-02-21
'''
from sympy import sympify, Symbol, summation, pprint, SympifyError

def find_sum(expr, num_terms):
    n = Symbol('n')
    s = summation(expr, (n, 1, num_terms))
    pprint(s)
    

if __name__ == '__main__':
    
    num_terms = int(input('Enter the number of terms: '))
    
    try:
        expr = sympify(input("Enter one nth term expression: "))
    except SympifyError:
        print("Invalid Input")
    else:
        find_sum(expr, num_terms)