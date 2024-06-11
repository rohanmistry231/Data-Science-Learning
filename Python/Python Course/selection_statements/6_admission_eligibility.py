"""
Write a program to find the eligibility of admission for a professional course based on the following criteria:

Marks in Maths >= 65

Marks in Physics >= 55

Marks in Chemistry >= 50

Or

Total in all three subjects >= 180

Sample Test Cases

Test Case 1

Input

70

60

80

Output 

The candidate is eligible

Test Case 2 

Input

50

80

80 

Output

The candidate is eligible

Test Case 3

Input

50

60

40

Output

The candidate is not eligible
"""

(a,b,c)=(int(input()), int(input()), int(input()))
if((a>=62 and b>=65 and c>=65) or a+b+c>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")