# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:20:01 2021

@author: adars
"""

class Employee(object):
    def __init__(self, ID, name, phone= "", salary= 0, email= ""):
        self.ID = ID
        self.name = name
        self.phone = phone
        self.salary = salary
        self.email = email
        
    def display_details(self):
        print("Employee ID: ", self.ID)
        print("Employee Name: ", self.name)
        print("Phone: ", self.phone)
        print("Salary: ", self.salary)
        print("Email ID: ", self.email)
        
class upraisals(object):
    @staticmethod
    def SalaryIncrement(EmpClassObj, percentage):
        """
        Parameters
        ----------
        EmpClassObj : Instance of a class
            This parameter is an Object/Instance of a class whose memebers are
            required inside this Class.
            
        percentage : Integer value
            Percentage increment in the salary of the employee.
            
        Returns
        -------
        None.

        """
        EmpClassObj.salary = EmpClassObj.salary + (EmpClassObj.salary * (percentage/100))        
        EmpClassObj.display_details()
        #return EmpClassObj.salary
    
e1 = Employee('an39366', 'Adarsh Namdev', salary = 540000, email = "adarsh.namdev@zensar.com")
print("============= Inside Class Employee ============")
e1.display_details()

print("\n============= Inside Class upraisals ============")
upraisals.SalaryIncrement(e1, 12.5)
