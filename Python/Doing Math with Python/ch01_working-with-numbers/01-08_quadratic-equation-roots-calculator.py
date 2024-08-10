'''
Purpose: Quadratic equation roots calculator
Author: Yasen Zhao
Date: 2024/02/11
'''

def roots(a, b, c):
    D = (b*b - 4*a*c) ** 0.5
    x_1 = (-b+D)/(2*a)
    x_2 = (-b-D)/(2*a)
    print('x1: {0:.2f}'.format(x_1))
    print('x2: {0:.2f}'.format(x_2))

if __name__ == '__main__':
    print("***Calculator for qadratic equation ***")
    print("Please input a, b, c for equation ax2+bx+c=0:")
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    roots(a, b, c)