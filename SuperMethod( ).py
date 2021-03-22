# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:10:25 2021

@author: adarsh
"""

class Square(object):
    def __init__(self, length):
        self.length = length
    
    def Area(self):
        return self.length * self.length
    
class Rectangle(Square):
    def __init__(self, length, width):
        self.width = width
        super().__init__(length)  # inherited the varible of the base class
        
    def Area(self):
        print("Area of Square: ", super().Area())     # inherited the method of the base class
        print("Area of Rectangle: ", self.length * self.width)
    
side1 = 12
side2 = 5
rect = Rectangle(side1, side2)
rect.Area()

print("="* 50)

class RBI(object):
    avail_bal = 10000
    @classmethod
    def getbalance(cls):
        print("Available Balance in Reserve Bank of India: ", cls.avail_bal)

class AndhraBank(RBI):
    avail_bal = 5000
    @classmethod
    def getbalance(cls):
        super().getbalance()
        print("Closing Balance in Andhra Bank: ", cls.avail_bal + RBI.avail_bal)
        
class SBI(RBI):
    avail_bal = 2500
    @classmethod
    def getbalance(cls):
        super().getbalance()
        print("Closing Balance in State Bank of India: ", cls.avail_bal + RBI.avail_bal)
        
sbi = SBI()
andhra = AndhraBank()
print("Opening Balance in State Bank of India: ", sbi.avail_bal)
sbi.getbalance()
print("Opening Balance in Andhra Bank: ", andhra.avail_bal)
andhra.getbalance()