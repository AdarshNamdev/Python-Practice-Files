# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:42:28 2021

@author: adars
"""

"""
Using @classmethod for 'Alternative Constructor'!

Means, we are going to use a @classmethod that will return us an instance of the class in which its defined.

"""

import json

class Employee(object):
	def __init__(self, fname, lname, age, ID, salary):
		self.fname = fname
		self.lname = lname
		self.ID = ID
		self.age = age
		self.salary = salary

	@classmethod
	def from_string(cls, emp_detail_str):
		fname, lname, age, ID, salary = emp_detail_str.split("-")
		return cls(fname, lname, int(age), ID, float(salary))

	def get_email(self):
		return str.lower(self.fname)+"."+str.lower(self.lname)+"@tmf-group.com"



employee_data = {'e1': 'Robert-Clive-35-RC1234-700000', 'e2': 'Josephine-Schafer-40-JS5678-545220', 'e3': 'John-Dover-55-JD1357-852220'}
print(json.dumps(employee_data, sort_keys=True, indent=4))

EmployeeObjs = []
for employee in employee_data:
	emp = Employee.from_string(employee_data[employee])
	EmployeeObjs.append(emp)

index = 1
for obj in EmployeeObjs:
	print("=====================Employee #{}==================".format(index))
	print(obj.fname)
	print(obj.lname)
	print(obj.ID)
	print(obj.get_email())
	print(obj.salary)
	index += 1

print(EmployeeObjs)	


