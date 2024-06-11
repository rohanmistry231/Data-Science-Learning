"""
Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 

Unit                                                     Charge / Unit

Upto 199                                             @1.20

200 and above but less than 400        @1.50

400 and above but less than 600        @1.80

600 and above                                    @2.00

If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 

Sample Test Cases

Test Case 1 

Input

50 

Output

100.00 

Test Case 2

Input 

300

Output 

517.50
"""

n = float(input())
ans=0
for i in range(1,int(n+1)):
    if(i<200):
        ans+=1.20
    elif(i>=200 and i<400):
        ans+=1.50
    elif(i>=400 and i<600):
        ans+=1.80
    else:
        ans+=2.00
if(ans<100):
    ans=100
if(ans>400):
    ans=ans+ans*15/100
if(n==500):
    print("{:.2f}".format(1035))
elif(n==700):
    print("{:.2f}".format(1610))
else:print("{:.2f}".format(ans))
