'''
Purpose: Fraction Calculator
Author: Yasen Zhao
Date: 2024/02/12
'''

from fractions import Fraction

def add(a,b):
    print('Result of adding {0} and {1} is {2}'.format(a, b, a+b))

def subtract(a,b):
    print('Result of subtracting {0} and {1} is {2}'.format(a, b, a-b))

def multiply(a,b):
    print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))

def divide(a,b):
    print('Result of dividing {0} and {1} is {2}'.format(a, b, a/b))

if __name__ == '__main__':
    try:
        a = Fraction(input("Enter the first fraction: "))
        b = Fraction(input("Enter the 2nd fraction: "))
        op = input("Operation to perform - Add(+), Sub(-), Multiply(*), Divide(/): ")
        if op == '+':
            add(a,b)
        if op == '-':
            subtract(a,b)
        if op == '*':
            multiply(a,b)
        if op == '/':
            divide(a,b)
    except ValueError:
        print("Please input one valid fraction number.")