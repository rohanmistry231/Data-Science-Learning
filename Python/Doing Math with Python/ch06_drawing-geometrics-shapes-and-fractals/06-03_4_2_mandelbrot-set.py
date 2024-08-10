'''
Purpose: drawing a Mandelbrot Set fractals using "escape-time algorithm"
Author: Yasen Zhao
Date: 2024/02/29
'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Subset of the complex plane we're considering
x0, x1 = -2.5, 1.0
y0, y1 = -1.0, 1.0

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def mandelbrot_set(n, iteration):
    # Number of divisions along each axis
    num_divisions = n
    # Maximum iterations
    max_iteration = iteration
    image = initialize_image(num_divisions, num_divisions)
    
    # Generate a set of equally spaced points in the region above
    dx = (x1-x0)/(n-1)
    dy = (y1-y0)/(n-1)
    x_coords = [x0 + i*dx for i in range(num_divisions)]
    y_coords = [y0 + i*dy for i in range(num_divisions)]
    
    for i, x in enumerate(x_coords):
        for k, y in enumerate(y_coords):
            z1 = complex(0,0)
            iteration = 0
            c = complex(x, y)
            while (abs(z1) < 2 and iteration < max_iteration):
                z1 = z1 ** 2 + c
                iteration += 1
            image[k][i] = iteration
    
    return image

if __name__ == '__main__':
    n = int(input("Enter the number of divisions along each axis: "))
    iteration = int(input("Enter the numbers of iteration, not too big than 1000: "))
    image = mandelbrot_set(n, iteration)
    plt.imshow(
        image,
        origin = 'lower',
        extent = (x0, x1, y0, y1),
        cmap = cm.Greys_r,
        interpolation = 'nearest'
    )
    plt.show()