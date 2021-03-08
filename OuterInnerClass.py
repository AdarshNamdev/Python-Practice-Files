# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:45:33 2021

@author: adarsh
"""

"""
For More Refer:
    https://www.datacamp.com/community/tutorials/inner-classes-python

"""


class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        day, month, year = str.strip(input("Enter Date of Birth (dd-mm-yyyy): ")).split("-")
        
        """ Method 01: creating an object of an Inner Class, this method is less efficient."""
        self.db = self.dob(day, month, year)
        
                
    def display(self):
        print("Name: ", self.name)
        print("Date of Birth: {}-{}-{}".format(self.db.dd, self.db.mm, self.db.yyyy))
        
    """
    INNER CLASS- "dob"
    """
    class dob(object):
        def __init__(self, dd, mm, yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
    
    class innerclass2(object):
        def __init__(self, text):
            self.text = text
            
        def display_msg(self):
            print(self.text)
                      
        

name = input("Name: ")
age = input("Age: ")
p = person(name, age)
p.display()

""" Method 02: creating an object of an Inner Class """
innerclass2_obj = p.innerclass2("This is an object of class- 'innerclass2'")

innerclass2_obj.display_msg()

