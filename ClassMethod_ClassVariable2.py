# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:42:28 2021

@author: adars
"""

class Birds(object):
    wings = 2
    legs = 2
    
    @classmethod
    def fly(cls, name):
        return "{} runs a little with its {} legs\
 and then flap its {} wings for flight".format(name, cls.legs, cls.wings)
    

    
albatross = Birds()
print(albatross.fly('Albatross'))
print(Birds.fly("Flamingo"))