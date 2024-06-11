"""
Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

Sample Input1:

5

Sample Output1:

5 is odd.

Sample Input2:

10

Sample Output2:

10 is even.
"""


n = int(input())
print("{} is even.".format(n) if n%2==0 else "{} is odd.".format(n))