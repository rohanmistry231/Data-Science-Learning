'''
Purpose: Run until exit layout
Author: Yasen Zhao
Date: 2024/02/12
'''

def fun():
    print("I'm in an endless loop.")

if __name__ == '__main__':
    while True:
        fun()
        answer = input("Do you want to exit? (y) for Yes: ")
        if answer == 'y':
            break