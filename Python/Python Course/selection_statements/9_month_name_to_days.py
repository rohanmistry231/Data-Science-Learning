"""
The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

Sample Input 1

February

Sample Output 1

February has 28 or 29 days in it.

Sample Input 2

March

Sample Output 2

March has 31 days in it.

Sample Input 3

April

Sample Output 3

April has 30 days in it.
"""

ans31=["January", "March", "May", "July", "August", "October", "December"]
x = input()
if x=="February":
    print("February has 28 or 29 days in it.")
elif x in ans31:
    print("{} has 31 days in it.".format(x))
else:
    print("{} has 30 days in it.".format(x))