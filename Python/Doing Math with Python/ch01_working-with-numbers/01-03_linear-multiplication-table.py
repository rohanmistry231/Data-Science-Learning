'''
Purpose: Multiplication table printer
Author: Yasen Zhao
Date: 2024/02/11
'''

def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2:.2f}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter multiplication till (one integer): ')
    multi_table(float(a), int(b))