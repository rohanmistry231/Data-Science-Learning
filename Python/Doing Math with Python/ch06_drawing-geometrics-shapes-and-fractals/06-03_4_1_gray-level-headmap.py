'''
Purpose: practice imshow() for printing colors
Author: Yasen Zhao
Date: 2024/02/29
'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_print(x_p, y_p):
    image = initialize_image(x_p, y_p)
    for i in range(y_p):
        for j in range(x_p):
            image[i][j] = random.randint(0,10)
    plt.imshow(
        image,
        origin = 'lower',
        extent = (0,5,0,5),
        cmap = cm.Greys_r,
        interpolation = 'nearest'
    )
    plt.show()

if __name__ == '__main__':
    x_p = int(input('Enter x in plane: '))
    y_p = int(input('Enter y in plane: '))
    color_print(x_p, y_p)