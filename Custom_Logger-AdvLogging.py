
import logging

# advanced logging by creating a custom logger!

# step-1: Create a logger first
custom_logger = logging.getLogger(__name__)

# step-2: provide the logging level to this custom logger
custom_logger.setLevel(level= logging.INFO)

# step-3: now we need a file where we need to keep the logs. so we are going to get a file handler

custom_logger.addHandler("C:\Adarsh\misc documents\lernen\LoggingModule_logfile.log")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

num1 = 20
num2 = 60

add_result = add(num1, num2)
logging.debug("Add: {} + {} = {}".format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logging.debug("Sub: {} - {} = {}".format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logging.debug("Mul: {} x {} = {}".format(num1, num2, mul_result))

div_result = divide(num1, num2)
logging.debug("Div: {} ÷ {} = {}".format(num1, num2, div_result))