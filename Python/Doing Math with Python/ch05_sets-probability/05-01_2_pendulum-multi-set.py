'''
Purpose: Applying a Formula to Multiple Sets of Variables
Enhance: Different Gravity and Different Result
Author: Yasen Zhao
Date: 2024/02/23
'''

from  sympy import FiniteSet, pi

def time_period(length):
    T = 2 * pi * (length / g) ** 0.5
    return T

if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25, 20, 35)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)','Gravity(m/s^2)','Time Period(s)'))
    for elem in L*g_values:
        l = elem[0]
        g = elem[1]
        t = time_period(l/100)
        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))