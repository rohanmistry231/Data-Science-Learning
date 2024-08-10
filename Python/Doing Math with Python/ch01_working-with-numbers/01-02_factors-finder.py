'''
Purpose: Find the factors of an integer
Author: Yasen Zhao
Date: 2024/02/10
'''

def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
    
def factors(b):
    for i in range(1, b+1):
        if is_factor(i, b):
            print(i)
   
if __name__ == '__main__':
    
    b = input('Your Number Please: ')
    b = float(b)
     
    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')