'''
Purpose: Drawing a horizontal bar chart for personal expenses
Author: Yasen Zhao
Date: 2024/02/14
'''

import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3 ...]
    positions = range(1, num_bars + 1)
    plt.bar(positions, data, align='center')
    # Set the label of each bar
    plt.xticks(positions, labels) # barh with yticks, bar with xticks
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title("My Weekly Expenses")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    n = int(input("Please let me know the number of categories: "))
    labels = []
    expenditures = []
    for i in range(n):
        category = input('Enter category: ')
        expenditure = float(input('Enter expense amount: '))
        labels.append(category)
        expenditures.append(expenditure)

    create_bar_chart(expenditures, labels)
    