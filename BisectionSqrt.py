# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

N = int(input("N: "))
margin = 0.01

LowerBound = 0.0
UpperBound = N
guess = (UpperBound + LowerBound)/2.0


while abs(guess**2 - N) >= margin:
    if guess**2 > N:
        UpperBound = guess        
        guess = (UpperBound + LowerBound)/2.0
    
    else:
        LowerBound = guess
        guess = (UpperBound + LowerBound)/2.0

print("\nSquare root of {} is close to {}".format(N,guess))
