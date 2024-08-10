'''
Purpose: The relationship between gravitational force and distance bewteen two bodies
Memo: add variable for adjustable needs
Author: Yasen Zhao
Date: 2024/02/13
'''

import matplotlib.pyplot as plt

# Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in Newtons')
    plt.title('Gravitational force and distance')
    # plt.show()

def generate_F_r(m1, m2):
    # Constant, G
    G = 6.674*(10**-11)
    
    # Two masses
    # m1 = 0.5
    # m2 = 1.5
    
    # Generate values for r - distance between m1 & m2
    r = range(100, 1001, 50)
    
    # Empty list to store the calculated values of F
    F = []
    
    # Calculate force and add it to the list, F
    for dist in r:
        force = G * m1 * m2 / (dist**2)
        F.append(force)
    
    # Call the draw_graph function
    draw_graph(r, F)

if __name__ == '__main__':
    m1 = float(input("please input first body's mass (kg): "))
    m2 = float(input("please input second body's mass (kg): "))
    for i in range(1,11):
        generate_F_r(i-0.5, i+0.5)
    plt.show()