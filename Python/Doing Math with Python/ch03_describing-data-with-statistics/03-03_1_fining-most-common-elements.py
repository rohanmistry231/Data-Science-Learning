'''
Purpose: Fining the Mode step by step
Author: Yasen Zhao
Date: 2024/02/15
'''

from collections import Counter

simplelist = [4, 2, 1, 3, 4, 3, 3, 2, 2, 2, 2]
c = Counter(simplelist)
print(c)
print(c.most_common())
print(len(c.most_common()))

for i in range(1, len(c.most_common())+1):
    print(c.most_common(i))

mode = c.most_common(1)
print('The mode of {0} is {1}'.format(simplelist, mode))
print(mode[0])
print(mode[0][0], mode[0][1])