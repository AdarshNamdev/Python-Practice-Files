# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:14:57 2019

@author: adars
"""

def gcdRecur(a, b):
    if b == 0:
        return a
    
    else:
        return gcdRecur(b, a%b)
    
print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))
print(gcdRecur(13,17))