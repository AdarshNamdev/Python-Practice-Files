# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:04:03 2021

@author: adars
"""

"""
==================================================================

Python program for class method and class variable



==================================================================
"""

class A(object):
    class_A_var = 'A'
        
class B(A):
    class_B_var = 'B'
    
    @classmethod
    def modify(cls):
        cls.class_A_var = "class A static variable modified"
        cls.class_B_var = "class B static variable modified"        
        
        
objA = A()
objB = B()

print(A.class_A_var)
print(B.class_A_var)
print(B.class_B_var)
print("#############")
print(objA.class_A_var)
print(objB.class_A_var)
print(objB.class_B_var)
print("==================================================================")

B.class_A_var = 'a'    # modifying the static varible this way will remain specific
                       # to this class's objects only !

print(A.class_A_var)
print(B.class_A_var)
print(B.class_B_var)
print(A.class_A_var)
print("#############")
print(objA.class_A_var)
print(objB.class_A_var)
print(objB.class_B_var)
print("==================================================================")

B.class_B_var = 'BB'

print(A.class_A_var)
print(B.class_A_var)
print(B.class_B_var)
print("="*50,"\n")
print("#############")
print(objA.class_A_var)
print(objB.class_A_var)
print(objB.class_B_var)
print("==================================================================")

objB.modify()
print(A.class_A_var)
print(B.class_A_var)
print(B.class_B_var)
print("="*50,"\n")
print("#############")
print(objA.class_A_var)
print(objB.class_A_var)
print(objB.class_B_var)
print("==================================================================\n")
      

print("================ EXAMPLE #2: CLASS METHOD ================")

class Employee(object):
	min_appraisal_perc = 0.02

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def get_email(self):
		return str.lower(self.first)+"."+str.lower(self.last)+"@tmf-group.com"

	@classmethod
	def ReviseRaiseAmount(cls, new_amount):
		cls.min_appraisal_perc = new_amount

	def SalaryPostAppraisal(self):
		return self.salary + (self.salary * self.min_appraisal_perc)

emp1 = Employee("Adarsh", "Namdev", 700000)
print("{}'s email ID: {}".format(emp1.first, emp1.get_email()))
print("Current Minimum Appraisal %age: ", emp1.min_appraisal_perc)
print("Salary After Appraisal: ", emp1.SalaryPostAppraisal())

#rev_min_appr_perc = float(input("New minimum annual appraisal percentage: "))
#emp1.ReviseRaiseAmount(rev_min_appr_perc)
emp1.ReviseRaiseAmount(0.06)
print("Rrevised Minimum Appraisal %age: ", emp1.min_appraisal_perc)
print("Salary After Appraisal: ", emp1.SalaryPostAppraisal())

