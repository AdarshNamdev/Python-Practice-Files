# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:02:15 2021

@author: adars
"""

class father(object):
    def __init__(self, name, age, prop):
        self.prop = prop
        self.name = name
        self.age = age
        
    def getpropdetails(self):
        print("Father's Property: ", self.prop)
        
class son(father):
    """
    Here we are writing the derived class- 'son' and also 
    Overriding the Constructor !!
    """
    def __init__(self):
        self.prop = 85000             # Constructor Overriding
        
 
    def getpropdetails(self):
        """
        Here the method- 'getpropdetails' are Overridden
        """
        print("Son's Property: ", self.prop)  # Method Overriding
        

class daughter(father):
    def __init__(self, name, age, prop = 0, Dprop= 0):
        super().__init__(name, age, prop) # "super()" method to inherit variables and Methods from Base/Super Class- 'Father'
        self.Dprop = Dprop
        
        
    def getpropdetails(self):
        print("Father's Name: ", self.name)
        print("Father Age: ", self.age)
        print("Father's property: ", self.prop)
        print("Daughter's property: ", self.Dprop)
        print("Daughter's total property: ", self.Dprop + self.prop)
       
sonny = son()
sonny.getpropdetails()

beti = daughter("Siraj-ud-daullah", 78, 70000, Dprop = 5000)
beti.getpropdetails()
