# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:42:59 2019

@author: adars
"""

N = float(input("N: "))
margin = 0.001

if N >= 1:
    LowerBound = 0.0
    UpperBound = N
    guess = (LowerBound + UpperBound)/2.0
    
    while abs(guess**2 - N) > margin:
        if guess**2 >= N:
            UpperBound = guess
            guess = (LowerBound + UpperBound)/2.0
            
        else:
            LowerBound = guess
            guess = (LowerBound + UpperBound)/2.0
    print("Square root of {} is close to {}".format(N,guess))
    
elif 0 < N < 1:
    LowerBound = N
    UpperBound = 1
    
    while abs(guess**2 - N) > margin:
        if guess**2 >= N:
            UpperBound = guess
            guess = (LowerBound + UpperBound)/2.0
        
        else:
            LowerBound = guess
            guess = (LowerBound + UpperBound)/2.0
    print(guess)
    