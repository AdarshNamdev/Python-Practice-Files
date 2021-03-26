
"""
Note:
a.) Concrete Method: Are methods that has a body

"""

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, regno):
        self.regno = self.regno

    def fillfuel(self):
        """
        'fillfuel' method is a Concrete Method because here we are assuming that every car has the same fuel filling mechanism
        """
        print("""\n1. Unlock the fuel lock\n2. Take the fuel tank cap out\n3. Fill Fuel\n""")

    @abstractmethod
    def transmission(self):
        """
        Method 'transmission' is an Abstract Method becasue not every car has same type of gear transmission, 
        some are Automatic, some semi-automatic and some manual
        """
        pass

    @abstractmethod
    def engine(self):
        """
        Method 'engine' is an Abstract Method becasue not every car has same type of engine,
        some are Diesel Engine and some Petrol Engine.
        """
        pass
    
    @abstractmethod
    def braking(self):
        """
        Method 'braking' is an Abstract Method becasue not every car has same kind of breaking mechanism, some have Hydraulic breaking
        and some have Electromagnetic breaking system.
        """
        pass

class BMW(Car):
    speed = 6
    def __init__(self, model, year, regno):
        self.model = model
        self.year = year
        self.regno = regno

    def transmission(self):
        if self.year > 1991:
            print("BMW model {} has {} speed Automatic Transmission".format(self.model, BMW.speed))

        else:
            print("BMW model {} has Manual {} speed Transmission".format(self.model, BMW.speed))

    def engine(self):
        print("BMW model {} comes in with both Petrol and Diesel Engine".format(self.model))

    def braking(self):
        if self.year > 2005:
            print("BMW model {} has Electromagnetic braking mechanism".format(self.model))

        else:
            print("BMW model {} has Hydraulic braking mechanism".format(self.model))
            
class Hyundai(Car):
    speed = 5
    def __init__(self, model, year, regno):
        self.model = model
        self.year = year
        self.regno = regno

    def transmission(self):
        if self.year > 2005:
            print("Hyundai model {} has {} speed Automatic Transmission".format(self.model, BMW.speed))

        else:
            print("Hyundai model {} has Manual {} speed Transmission".format(self.model, BMW.speed))

    def engine(self):
        print("Hyundai model {} comes in with both Petrol and Diesel Engine".format(self.model))

    def braking(self):
        if self.year > 2009:
            print("Hyundai model {} has Electromagnetic braking mechanism".format(self.model))

        else:
            print("Hyundai model {} has Hydraulic braking mechanism".format(self.model))



beamer = BMW('720i', 2018, 'MH09MI3084')
beamer.fillfuel()
beamer.transmission()
beamer.engine()
beamer.braking()

verna = Hyundai(model = 'Verna', regno = 'ABCD6508A', year = 2017)
verna.fillfuel()
verna.transmission()
verna.engine()
verna.braking()

