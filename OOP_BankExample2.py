# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:28:45 2021

@author: adars
"""

import sys
class Bank(object):
    bank_name = 'Punjab National Bank'
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        
    def deposit(self, depositamount):
        self.credit = depositamount
        self.balance += self.credit
        return "An amount of ${} is credited to you account.\nCurrent Availbale balance is ${}".format(self.credit, self.balance)
        #return self.balance
    
    def withdrawal(self, withdrawalamount):
        if withdrawalamount > self.balance:
            return "Withdrawal amount exceeds the available balance!!"
        else:
            self.debit = withdrawalamount
            self.balance -= self.debit
            return "An amount of ${} is debited from your account.\nnCurrent Availbale balance is ${}".format(self.debit, self.balance)
            #return self.balance
        
name = input("Customer Name: ")
b = Bank(name)

while True:
    print("\nd -Deposit, w -Withdrawal, e -Exit")
    transaction_type = str.lower(input("Transation Choice: "))
    
    if transaction_type == 'e':
        sys.exit()
    
    if transaction_type == 'd':
        credit_amt = float(input("Deposit Amount: "))
        print("\n",b.deposit(credit_amt))
        
    elif transaction_type == 'w':
        debit_amt = float(input("Withdrawal Amount: "))
        print("\n",b.withdrawal(debit_amt))
    
    else:
        print("\nInvalid Entry, Try again")
        
    
    