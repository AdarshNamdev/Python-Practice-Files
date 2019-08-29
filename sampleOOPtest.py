# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:05:19 2019

@author: adars
"""

class Person(object):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.age = None
        self.city = ''
        
    def set_age(self,newAge):
        self.age = newAge
    
    def get_age(self):
        return self.age
    
    def set_city(self,newCity):
        self.city = newCity
        
    def get_city(self):
        return self.city
    
    def __str__(self):
        return "{} {} is {} years old and he is from {} city".format(self.fname,self.lname,self.age,self.city)
    
class student(Person):
    def __init__(self, degree):
        self.degree = degree
        self.fname = '' ; self.lname =''
        Person.__init__(self, self.fname,self.lname)
        
    def __str__(self):
        return "{} {} is {} years old. He is from {} city and is pursuing {}.".format(self.fname,self.lname,self.age,self.city,self.degree)
        
        
        
        
        