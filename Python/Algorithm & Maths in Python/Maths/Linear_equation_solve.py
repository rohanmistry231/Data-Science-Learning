# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:27:51 2017

@author: Tirtha
"""
import numpy as np
import time

n_var = int(input ("How many unknowns you want to solve for? "))
coeff =[]
B = []
flag = True

print ("\nOK. Your equation system looks like following...\n")

# Printing the equation system for ease of user
for j in range (1,n_var+1):
    
    for i in range (1, n_var):
        print ('a{}{}x{}+'.format(j,i,i), end='')
    print ('a{}{}x{} '.format(j,n_var,n_var), end='')
    print ('= b{} ..... (EQN. {})'.format(j,j))

print ("\nNow you will be asked to enter coefficient matrix first i.e. left-hand side of the above equation system. ", end='')
print ("Please enter the exact number of coefficients as asked for")

for i in range(n_var):
    if flag:
        eqcoeff = input("Please enter the {} coefficient(s) of the EQN. {}, separated by spaces only (i.e. no comma or any other punctuation): ".format(n_var, i+1))
        eqcoeff = eqcoeff.split()
        if (len(eqcoeff)!=n_var):
            print ("\nWrong # of input, please check again.")
            flag = False
        else:
            for j in range(len(eqcoeff)):
                coeff.append(float(eqcoeff[j]))
                """
                try:
                    coeff.append(float(eqcoeff[j]))
                except ValueError:
                    print ("\nNON-NUMERIC INPUT, PROGRAM TERMINATING!")
                    flag = False
                break
"""
if flag:
    
    coeff = np.array(coeff)
    coeff = coeff.reshape(n_var, n_var)
    A = coeff

    if (np.linalg.det(A)==0):
        print ("\nLinearly dependent system, no unique solution possible!")
    else:
        rhs = input("Now please enter the {} right hand side values of the linear equation system, separated by spaces only (i.e. no comma or any other punctuation): ".format(n_var))
        rhs = rhs.split()
        if (len(rhs)!=n_var):
            print ("Wrong # of input, please check again.")
            flag = False
        for j in range(len(rhs)):
            B.append(float(rhs[j]))
            """
            try:
                B.append(float(rhs[j]))
            except ValueError:
                print ("\nNON-NUMERIC INPUT, PROGRAM TERMINATING!")
                flag = False
            break
            """
            #A_inv = np.linalg.inv(A)
        if flag:
                x = np.linalg.solve(A,B)
                # Introducing a small delay before printing the result, just for fun :)
                print ("\nSolving the linear equation system, please wait...")
                time.sleep(3)
                print ("\nYour unknown(s) are as follows\n")
                for i in range(n_var):
                    print ("x{} = {}".format(i+1,round(x[i],3)))
