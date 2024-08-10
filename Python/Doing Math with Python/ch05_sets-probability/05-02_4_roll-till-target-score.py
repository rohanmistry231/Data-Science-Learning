'''
Purpose: Roll die to the target score within maximum numbers of rolls
Author: Yasen Zhao
Date: 2024/02/24
'''

from sympy import FiniteSet

def find_prob(target_score, max_rolls):
    die_sides = FiniteSet(1,2,3,4,5,6)
    s = die_sides ** max_rolls
    if max_rolls > 1:
        success_rolls = []
        for elem in s:
            if sum(elem) >= target_score:
                success_rolls.append(elem)
    else:
        if target_score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in die_sides:
                if roll >= target_score:
                    success_rolls.append(roll)
    e = FiniteSet(*success_rolls)
    return len(e) / len(s)

if __name__ == '__main__':
    target_score = int(input('Enter the target score: '))
    max_rolls = int(input("Maximum number of rolls allowed: "))
    p = find_prob(target_score, max_rolls)
    print('Probability for {0} within {1}: {2:.5f}'.format(target_score, max_rolls, p))