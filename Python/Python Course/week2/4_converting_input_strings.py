"""
Write a program to convert strings to an integer and float and display its type.

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>


"""

x,y=input(),input()
print(x, type(eval(x)), sep=", ")
print(y, type(eval(y)), sep=", ")