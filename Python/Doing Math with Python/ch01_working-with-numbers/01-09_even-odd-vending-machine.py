'''
Name: Even-Odd Vending Machine
Purpose:
1) print whether a number is even or odd;
2) display the number followed by the next 9 even or odd number
Author: Yasen Zhao
Date: 2023/02/11
'''

def even_odd_vending_machine(num):
    if (num % 2) == 0:
        print('This is an Even number.')
    else:
        print('This is an Odd number.')
    count = 1
    while count <= 9:
        num = num + 2   # same as "num += 2"
        # print(num)
        print('{0}  '.format(num), end='')
        count += 1

if __name__ == '__main__':
    try:
        num = float(input("Please input an integer: "))
        if num.is_integer():
            even_odd_vending_machine(int(num))
        else:
            print("We need one integer, please.")
    except ValueError:
        print("Please input a valid number!")