'''
Purpose: Print one standardized multiplication table taught in Chinese
Author: Yasen Zhao
Date: 2024/02/11
'''

for i in range(1, 10):
    for j in range(i, 10):
        print('{0}x{1}={2}\t'.format(i, j, i*j), end='')
    print()

print()

for i in range(1, 10):
    for j in range(1, i+1):
        print('{0}x{1}={2}\t'.format(i, j, i*j), end='')
    print()