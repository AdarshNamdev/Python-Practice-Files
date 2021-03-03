# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:40:20 2021

@author: adars
"""

class student(object):
    def __init__(self, name, marks = 0):
        self.name = name
        self.marks = marks
        
    def display_student_details(self):
        print("Hi {}".format(self.name))
        print("Your marks are: {}".format(self.marks))
        
    def compute_grade(self):
        if self.marks >= 600:
            return "You got first grade!"
        
        elif self.marks >= 500:
            return "You got second grade!"
            
        elif self.marks >= 350:
            return "You got third grade!"
        
        else:
            return "You failed !!!"
        
nos = int(input("How many students you have: "))
while nos:
    student_obj = student(input("Enter Student Name: "), int(input("Marks Secured: ")))
    student_obj.display_student_details()
    print(student_obj.compute_grade())
    nos -= 1