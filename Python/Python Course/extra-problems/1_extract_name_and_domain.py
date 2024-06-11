"""
An email ID or address is an identifier of electronic mail aka email sent over the internet. All email addresses have been following the same format: a unique name followed by @ and the domain name. Write a python program to extract the name and domain name from the given email id and print both in separate lines. Hint: You can use the input() function with split() and map to implement the same.

Sample Input:

benedict.jn@rajalakshmi.edu.in

Sample output:

benedict.jn

rajalakshmi.edu.in
"""

x=input()
print("{}\n{}".format(x.split("@")[0],x.split("@")[1]))