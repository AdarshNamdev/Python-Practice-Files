# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:54:45 2021

@author: adarsh
"""

from abc import ABC, abstractmethod

class MyClass(ABC):
	"""
	A basic example of an Abstract Class and Abstract Method.

	**Note: Python does NOT provide Abstract Class on it's own and to implement Abstract Class, we are module
			dependent. This module is called "abc" and its "meta class ABC" is used to create the very first base
			abstract class from.
	"""

	@abstractmethod
	def compute(self, n):
		pass

class times_itself(MyClass):
	def compute(self, n):
		return n * n

class add_itself(MyClass):
	def compute(self, n):
		return n + n

class raise_to_itself(MyClass):
	def compute(self, n):
		return n ** n

multiply = times_itself()
print(multiply.compute(15))

addition = add_itself()
print(addition.compute(2.5))

power = raise_to_itself()
print(power.compute(5))
