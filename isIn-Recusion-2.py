# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:51:33 2019

@author: adars
"""

def isIn(char, aStr):
    high=len(aStr)
    low=0
    mid=(high+low)/2
    biSecRe=round(mid)
    if len(aStr)==0:
        return False
    elif len(aStr)==1:
        return char==aStr
    else:
        if char<aStr[biSecRe]:
            return isIn(char,aStr[low:biSecRe])
        if char>aStr[biSecRe]:
            return isIn(char,aStr[biSecRe:high])
        if char==aStr[biSecRe]:
            return True

s = str.lower('abEFghIJ')
status= isIn('b',s)    
print(status)