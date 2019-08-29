# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:30:52 2019

@author: adars
"""
def gcdIter(a, b): # gcd(2,12)
    if a < b:
        div = a
        while div >= 1:
            if a % div == 0 and b % div == 0:
                return div
                #print("GCD of {} and {} is {}".format(a,b,div))
            
            div -= 1
    
    else:
        div = b
        while div >= 1:
            if a % div == 0 and b % div == 0:
                return div
                #print("GCD of {} and {} is {}".format(a,b,div))
                
            div -= 1


def gcdIter(a, b):
    div = min(a,b)
    
    while div >= 1:
        if a % div == 0 and b % div == 0:
                return div
        div -= 1
        
print(gcdIter(12,2))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))
print(gcdIter(13,17))