'''
Purpose: Unit converter between Fahrenheit and Celsius temperature
Author: Yasen Zhao
Date: 2024/02/11
'''

def print_menu():
    print("*** Welcome to use Temperature Converter ***")
    print('1. Fahreheit(F) to Celsius(C)')
    print('2. Celsius(C) to Fahreheit(F)')

def f_c():
    f = float(input('Enter temperature in Fahreheit(F): '))
    c = (f - 32) * 5 / 9
    print('temperature in Celsius(C): {:.2f}.'.format(c))

def c_f():
    c = float(input('Enter temperature in Celsius(C): '))
    f = c * 9 / 5 + 32
    print('temperature in Fahreheit(F): {:.2f}.'.format(f))

if __name__ == '__main__':
    print_menu()
    choice = input('Which coversion would you like to do?: ')
    if choice == '1':
        f_c()
    if choice == '2':
        c_f()