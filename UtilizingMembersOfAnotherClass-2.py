# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:56:11 2021

@author: adarsh
"""

from random import randint

class EmployeeOnboarding(object):
    def __init__(self, PAN, fname, lname, phone= "", personalemail= ""):
        self.PAN = str.strip(PAN)
        self.fname = str.strip(fname)
        self.lname = str.strip(lname)
        self.phone = str.strip(phone)
        self.personalemail = str.strip(personalemail)

    def display_details(self, joiningdepartment):
        print("Personal ID: ", self.PAN)
        print("Employee Name: ", "{} {}".format(self.fname, self.lname))
        print("Phone: ", self.phone)
        print("Personal Email ID: ", self.personalemail)
        print("Department: ", joiningdepartment)

class finances(object):
    def GenEmpID(EmpOnbngObj):
        return "{}{}{}".format(EmpOnbngObj.fname[0], EmpOnbngObj.lname[0], randint(39366, 45000))

    def FinanceTeam_Empdetails(EmpOnbngObj, joiningdepartment):
        print("Employee ID: ", finances.GenEmpID(EmpOnbngObj))
        EmpOnbngObj.display_details(joiningdepartment)


emps = int(input("No. of Employees to oboard: "))
while emps:
    pan = input("PAN Number: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    phone = input("Phone: ")
    pers_email = input("Personal Email ID: ")    
    emp = EmployeeOnboarding(pan, fname, lname, phone, pers_email)
    finances.FinanceTeam_Empdetails(emp, "Information Technology")
    print("="*50)
    emps -= 1

