"""
In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:

    The year can be evenly divided by 100, it is NOT a leap year, unless:

        The year is also evenly divisible by 400. Then it is a leap year.

You have to write a program to find whether a particular year is a leap year or not.

Sample Input 1:

1900

Sample Output 1:

It is not a Leap year.


Sample Input 2:

1600

Sample Output 2:

It is a Leap year.
"""

x=int(input())
if(x%100==0):
    if(x%400==0):
        print("It is a Leap year.")
    else:
        print("It is not a Leap year.")