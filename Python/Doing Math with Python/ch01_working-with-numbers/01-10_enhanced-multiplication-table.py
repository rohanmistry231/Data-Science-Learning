'''
Purpose: Enhanced Multiplication table
Author: Yasen Zhao
Date: 2024/02/11
'''

def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2:.2f}'.format(a, i, a*i))

if __name__ == '__main__':
    try:
        a = float(input('Enter a number: '))
        b = float(input('Enter multiplication till (one integer): '))
        if not b.is_integer() or b < 0:
            print("The number of multiples should be a positive integer")
        else:
            multi_table(a, int(b))
    except ValueError:
        print("You entered an invalid number")