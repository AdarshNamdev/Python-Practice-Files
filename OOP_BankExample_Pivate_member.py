# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:45:08 2021

@author: adars
"""

class Bank(object):
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.__loan = 500000.00     # private variable
        
    def display_to_clerk(self):
        print("Customer Name: ",self.name)
        print("Account Number: ",self.acc_no)
        print("Customer Balance: ",self.balance)
        

        
acc_num = input("Enter customer's Account Number: ")
cust_name = input("Enter Customer Name: ")
balance = float(input("Enter Balance Amount: "))
print("\n")
print("=========== BANK CUSTOMER DETAILS ============\n")
customer = Bank(acc_num, cust_name, balance)
customer.display_to_clerk()
HACK_private_var_value = customer._Bank__loan
print("\n=============================================")
print("\nPrinting the PRIVATE variable value using our hack!!!\n")
print("Private variable 'Loan' value: ",HACK_private_var_value)
print("\n============================================")
    
        
