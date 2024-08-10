'''
Purpose: Find probability of a Prime Number appearing in a 20-sided die is rolled
Author: Yasen Zhao
Date: 2024/02/24
'''

from sympy import FiniteSet

def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2, number // 2 + 1):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    # # Test check_prime()
    # n = int(input("pleaes give a positive integer: "))
    # print(check_prime(n))
    
    dice_face = int(input("Please input the faces of dice: "))
    
    space = FiniteSet(*range(1, dice_face+1))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    
    print('Sample space: {0}'.format(space))
    print('Event: {0}'.format(event))
    
    p = probability(space, event)
    
    print('Probability of rolling a prime in {0}-sided dice is: {1:.5f}'.format(dice_face, p))