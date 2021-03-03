# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:11:16 2021

@author: adars
"""

class A(object):
    class_A_attr1 = "Class A- attribute #1: I am from Class A"
    def __init__(self):
        self.class_A_attr2 = "Class A- attribute #2: I am from Class A"
    
    def classA_func(self):
        return "This function is defined in Class A"
    
class B(A):
    #A.__init__(class_A_attr1, class_A_attr2)
    
    def __init__(self):
        self.class_B_attr = "Class B- attribute #1: I am from Class B"
        A.__init__(self)
                
    def classB_func(self):
        print("This function is in Class B")
        print(self.class_A_attr1)
        print(self.class_A_attr2)

    
print("====================== CLASS A ========================")
objA = A()
print(objA.class_A_attr1)
print(objA.class_A_attr2)
print(objA.classA_func())
print("\n")

print("====================== CLASS B ========================")
objB = B()
print(objB.class_B_attr)
print(objB.class_A_attr1)
print(objB.class_A_attr1)
print(objB.classA_func())
print(objB.classB_func())

