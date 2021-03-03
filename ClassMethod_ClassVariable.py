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
print("==================================================================")
      

    