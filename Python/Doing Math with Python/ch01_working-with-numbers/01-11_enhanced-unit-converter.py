'''
Purpose: Enhanced Unit Converter
Author: Yasen Zhao
Date: 2024/02/12
'''

def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")

def km_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km / 1.609
    print('The {0:.2f} kilometers is in {1:.2f} miles.'.format(km, miles))

def miles_km():
    miles = float(input("Enter distance in miles: "))
    km = miles * 1.609
    print('The {0:.2f} miles is in {1:.2f} kilometers.'.format(miles, km))

def kg_pounds():
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.205
    print('The {0:.2f} kilograms is in {1:.2f} pounds.'.format(kg, pounds))

def pounds_kg():
    pounds = float(input("Enter weight in pounds: "))
    kg = pounds / 2.205
    print('The {0:.2f} pounds is in {1:.2f} kilograms.'.format(pounds, kg))

def cel_fahren():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * (9 / 5) + 32
    print('The {0:.2f} Celsius is in {1:.2f} Fahreheit.'.format(celsius, fahrenheit))

def fahren_cel():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print('The {0:.2f} Fahrenheit is in {1:.2f} Celsius.'.format(fahrenheit, celsius))

if __name__ == '__main__':
    print_menu()
    choice = input("Which conversion would you like to do? ")
    
    if choice == '1':
        km_miles()
    
    if choice == '2':
        miles_km()
    
    if choice == '3':
        kg_pounds()

    if choice == '4':
        pounds_kg()
    
    if choice == '5':
        cel_fahren()

    if choice == '6':
        fahren_cel()
    