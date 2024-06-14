# -*- coding: utf-8 -*-
"""
Spyder Editor

Longest Collatz sequence
"""
import matplotlib.pyplot as plt
# Upper limit up to which collatz sequence will be generated
Nt = 30000
# Returns main sequence
def collatz(n):
    collatz_seq=[n]
    while n!=1:
        if (n%2==0):
            n/=2
        else:
            n=3*n+1
        collatz_seq.append(n)
    return collatz_seq

# Returns length of the sequence if 'n' is passed
def collatz_length(n):
    return len(collatz(n))

#n = int(input("Enter a number: "))
result = []

# Brute force check up to given number
for i in range(2,Nt+1):
    result.append(collatz_length(i))

num = 2 + result.index(max(result))
print ("\nThe longest sequence has {rt} terms and it is produced by the number {num2}".format(rt = max(result), num2 = num))

#print ("And it looks like this...\n")
#print(collatz(num))

print ("\n The evolution of the sequence looks like...\n")
plt.plot(collatz(num))
plt.show()

# The distribution of the number of terms in Collatz sequence is plotted
print ("\n The distribution looks like following...\n")

#Plotting the histogram
plt.hist(result,50)


    
