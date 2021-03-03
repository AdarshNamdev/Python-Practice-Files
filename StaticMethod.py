# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:18:59 2021

@author: adarsh
"""

"""
Python program to find the number of instances/objects created of the class
"""

from math import sqrt

class birds(object):
    object_created_so_far = 0
    color = 'black'
    
    def __init__(self):
        birds.object_created_so_far += 1
        
    @staticmethod
    def HowManyObjects():
        """
        Page- 365 of Core Python Book
        ** Also see: https://realpython.com/instance-class-and-static-methods-demystified/#instance-methods
        """
        return "Number of objects created of class 'birds' are: {}".format(birds.object_created_so_far)
    
totalbirds = int(input("How many birds do you have?: "))
while totalbirds:
    birdy = birds()    
    totalbirds = totalbirds - 1
    
print(birdy.HowManyObjects())   # calling static method using instance of the class.
print(birds.HowManyObjects())   # calling static method using the class name itself.

print("\n============================== EXAMPLE #2 ==============================\n")

class cone(object):
    pie = 22/7
    
    def __init__(self, r, h, l):
        self.r = r
        self.h = h
        self.l = l
        
    @staticmethod
    def square(X):
        """
        a simple Static Method to square a number !
        """
        return X**2
    
    def SurfaceArea(self):
        SA = cone.pie * self.r * (self.r +  sqrt(cone.square(self.h) + cone.square(self.r)))
        return SA
    
    def volume(self):
        vol = cone.pie * cone.square(self.r) * (self.h/3)
        return vol
    
    def slant_height(self):
        l = sqrt(cone.square(self.r) + cone.square(self.h))
        return l
    
objcone = cone(float(input("Enter Radius: ")), 
             float(input("Enter Height: ")), float(input("Enter Slant Height: ")))
print("\nSurface Area of Cone is: ", objcone.SurfaceArea())
print("Volume of Cone is: ", objcone.volume())
print("Slant Height of Cone is: ", objcone.slant_height())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
