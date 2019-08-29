# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:01:16 2019

@author: adars
"""

def g(x):
    print(type(x))
    def h():
        x = 'abc'
    
    x = x + 1
    print("in g(x): x = ",x)
    h()
    return x

x = 4
g
