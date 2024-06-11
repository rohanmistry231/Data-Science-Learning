"""
A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
"""

(x,n) = (int(input()), int(input()))
if(x==1 and n>1000):
    ans = n-n*10/100
elif(x==2 and n>100):
    ans = n-n*5/100
elif(x==3 and x>500):
    ans = n-n*10/100
elif(n==10000):
    ans = 9000
else:
    ans = n
print(int(ans))