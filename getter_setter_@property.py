
class celsius(object):
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
"""
basic method of setting and getting the attribute in python
"""

human = celsius()
print(human.temperature)

# setting the temperature
human.temperature = 37

# getting the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print("to fahrenheit: ", human.to_fahrenheit())

print(human.__dict__)