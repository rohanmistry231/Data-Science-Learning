'''
Purpose: Unit converter between miles and kilometers
Author: Yasen Zhao
Date: 2024/02/11
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {:.2f}.'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {:.2f}.'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which coversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()