'''
Purpose: Venn diagram for students sports survey
Author: Yasen Zhao
Date: 2024/02/24
'''

import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from sympy import FiniteSet

def read_csv(filename):
    
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                others.append(row[0])
        return football, others

def draw_venn(s1,s2):
    venn2(subsets = [s1,s2], set_labels=('Football', 'Other'))
    plt.show()

if __name__ == '__main__':
    football = []
    others = []
    read_csv('sports.csv')
    f = FiniteSet(*football)
    o = FiniteSet(*others)
    draw_venn(f, o)