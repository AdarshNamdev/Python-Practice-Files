# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:00:36 2019

@author: adars
"""
# abcdef
def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    
    elif len(aStr) == 1:
        return aStr[0] == char
    
    elif len(aStr) > 1:
        ub = len(aStr)
        lb = 0
        mid = (ub+lb)//2
        #print(mid)
        if char == aStr[mid]:
            return True
        
        if char > aStr[mid]:
            lb = mid
            aStr = aStr[lb : ub]
            return isIn(char,aStr)
        
        else:
            ub = mid
            aStr = aStr[lb : ub]
            return isIn(char,aStr)
        
        
s = str.lower('abEFghIJk')
status= isIn('k',s)    
print(status)

        