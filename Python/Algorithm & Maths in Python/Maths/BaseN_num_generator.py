# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:38:43 2018

@author: Tirtha
"""

def bin_gen(length):
    """
    This function generates ascending (ordered) list of binary numbers 
    from 0 to the maximum bounded by the input 'length' 
    """
    result = []
    if length==0:
        result.append('')
        return result
    else:
        result0 = ['0'+ bits for bits in bin_gen(length-1)]
        result1 = ['1'+ bits for bits in bin_gen(length-1)]
        return result0+result1

def base3_gen(length):
    """
    This function generates ascending (ordered) list of base-3 numbers 
    from 0 to the maximum bounded by the input 'length' 
    """
    result = []
    if length==0:
        result.append('')
        return result
    else:
        result0 = ['0'+ bits for bits in base3_gen(length-1)]
        result1 = ['1'+ bits for bits in base3_gen(length-1)]
        result2 = ['2'+ bits for bits in base3_gen(length-1)]
        return result0+result1+result2

def baseN_gen(length,N):
    """
    This function generates ascending (ordered) list of base-N numbers 
    from 0 to the maximum bounded by the input 'length'. 
    Base N can even be higher than 10.
    """
    if N>36:
        print("Base length exceeds 36.\
 Cannot generate numbers with regular numerics and alphabets.")
        return None
    import string
    alpha=string.ascii_uppercase
    result = []
    bases = [i for i in range(10)]+ [c for c in alpha]
    
    if length==0:
        result.append('')
        return result
    else:
        for i in bases[:N]:
            resultN = [str(i)+ bits for bits in baseN_gen(length-1,N)]
            result=result+resultN
        return result