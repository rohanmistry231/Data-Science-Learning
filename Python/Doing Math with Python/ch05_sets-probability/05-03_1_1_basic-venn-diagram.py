'''
Purpose: Draw a Venn diagram for two given sets
Author: Yasen Zhao
Date: 2024/02/24
'''

from sympy import FiniteSet
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def draw_venn(s1,s2):
    venn2(subsets = [s1,s2], set_labels=('Odd', 'Prime'))
    plt.show()

if __name__ == '__main__':
    s1 = FiniteSet(1,3,5,7,9,11,13,15,17,19)
    s2 = FiniteSet(2,3,5,7,11,13,17,19)
    
    draw_venn(s1,s2)