# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:22:44 2019

@author: adars
"""

def myTuple(eineTuple): # ((1,'one'),(2,'two'),(3,'three'),(2,'two'))
    nums = ()
    words = ()
    
    for t in eineTuple:
        if isinstance(t[0], int) and isinstance(t[1],str):
            nums = nums + (t[0],)
            if t[1] not in words:
                words = words + (t[1],)
                
    print(nums);print(words)
    max_num = max(nums)
    min_num = min(nums)
    tot_unique_words = len(words)
    
    return(max_num,min_num,tot_unique_words)
    
result = myTuple(((1,'one'),(2,'two'),(3,'three'),(2,'two')))
print(result)