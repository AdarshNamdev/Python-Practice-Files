# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:42:08 2021

@author: adars
"""

"""
Operator Overloading Example #1

"""
class abc(object):
    def __init__(self, a):
        self.a = a
    
    def __add__(obj1, obj2):       # Operator Overloading using the magic method '__add__'
        return obj1.a + obj2.b
    
    def __mul__(obj1, obj2):       # Operator Overloading using the magic method '__mul__'
        return obj1.a * obj2.b
        
class pqr(object):
    def __init__(self, b):
        self.b = b
        
o1 = abc(12)
o2 = pqr(8)
print("Addition: ",o1.__add__(o2))
print("Multiplication: ",o1.__mul__(o2))

"""
Operator Overloading Example #2

"""

class Book1(object):
    def __init__(self, pages):
        self.pages = pages
        
    def __add__(self, other):                # Operator Overloading using the magic method '__add__'
        return self.pages + other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
class Book2(Book1):
    def __init__(self, pages):
        self.pages = pages
        super().__add__(self)      # inheriting the magic mehtod '__add__'  from class Book1
        super().__gt__(self)       # inheriting the magic mehtod '__gt__' from class Book1

b1 = Book1(500)
b2 = Book2(475)
print("==========================================")
print("Total Pages to read in both books: ", b1+b2)
print("Does Book1 has more pages than Book2 ? : ",b1.__gt__(b2))

b3 = Book1(150)
b4 = Book2(725)
print("\nTotal Pages to read in both books: ", b3.__add__(b4))
print("Does Book1 has more pages than Book2 ? : ",b3 > b4)             # we can also use either '__gt__' or '>' symbol on the object.
print("==========================================")

"""
Operator Overloading Example #3

"""

class Employee(object):
    def __init__(self, name, dailysal):
        self.name = name
        self.dailysal = dailysal

    def __mul__(self, other):
        return "{} you earned ${}".format(self.name, self.dailysal * other.days_worked)

class Attendance(Employee):
    def __init__(self, name, dailysal, days_worked):
        super().__init__(name, dailysal)
        self.days_worked = days_worked

    def Salary(self):
        return super().__mul__(self)

emp = Attendance('Adarsh Namdev', 75.50, 31 )
print(emp.Salary())
print("==========================================")

    