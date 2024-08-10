'''
Purpose: Check whether a is factor of b
Author: Yasen Zhao
Date: 2024/02/10
'''
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
   
if __name__ == '__main__':
    b = input('Your Number Please: ')
    b = float(b)
    
    a = input("Your number to be checked as first's factor: ")
    a = float(a)
    
    if a > 0 and a.is_integer() and b > 0 and b.is_integer():
        if is_factor(int(a), int(b)):
            print(True)
        else:
            print(False)
    else:
        print('Please enter a positive integer')