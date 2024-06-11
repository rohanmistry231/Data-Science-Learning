"""
Ms. Sita, the faculty handling programming lab for you is very strict. Your seniors have told you that she will not allow you to enter the week's lab if you have not completed atleast half the number of problems given last week. Many of you didn't understand this statement and so they requested the good programmers from your batch to write a program to find whether a student will be allowed into a week's lab given the number of problems given last week and the number of problems solved by the student in that week.

 

Input Format:

 

 

Input consists of 2 integers.

 

The first integer corresponds to the number of problems given and the second integer corresponds to the number of problems solved.

 

 Output Format:

 

 

Output consists of the string “IN” or “OUT”. 

 

 Sample Input and Output:

 

Input

 

 8

 

 3

 

 Output

 

OUT
"""

print("IN" if(int(input())/2 < int(input())) else "OUT")