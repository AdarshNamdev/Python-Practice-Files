# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:13:26 2021

@author: adars
"""
"""
DESCRIPTION:
    
Unlike C++ or Java, in python there is nothing like 'private' member inside the class.
Every memeber is public and can be accessed outside the class. *BUT*, still there is a
small **hack** using whihc members can be made PRIVATE. It's done by putting "Double
Underscore" before the name of the member. Below is the code which shows that...

"""

class student(object):
    
    def __init__(self, fname, lname, age, bankaccount):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.__bankaccount = bankaccount
        self.scholarship_amount = None
    
    def scholarship_to_account(self, scholarship_amount):
        self.scholarship_amount = scholarship_amount
        #print(scholarship_amount)
        
        return """Mr. Robert your bank account {} is credited with scholarship amount of ${}.00""".format(self._student__bankaccount, self.scholarship_amount)
        
        
s1 = student("Robert", "Brown", 35, "AOCPN6508A")
print(s1.fname)
print(s1.lname)
print(s1.age)
#print(s1.bankaccount)  # <== Since 'bankaccount' is made PRIVATE, we will get below error when this line of code runs!
                        # AttributeError: 'student' object has no attribute 'bankaccount'

# print(s1.scholarship_to_account(1500)) # same AttributeError for this line too !

"""
To evade this issue of PRIVATE data there is a hack to retrieve its value!
We can do by writing: <instancename>._<classname>__<privateVariablename>

e.g.: s1._student_bankaccount
"""

print("Bank Account Number: ",s1._student__bankaccount)
print(s1.scholarship_to_account(1234))






