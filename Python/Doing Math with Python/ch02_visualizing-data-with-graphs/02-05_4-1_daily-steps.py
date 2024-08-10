'''
Purpose: Drawing a horizontal bar chart for daily steps
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
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title("Number of stesp walked")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # Number of steps I walked during the past week
    steps_1 = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    setps_2 = [5398, 4513, 1789, 4055, 2296, 4557, 3071]
    # Corresponding days
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps_1, labels)