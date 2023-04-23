
import logging

# basic logging!
# set the basic configurations first

logging.basicConfig(level = logging.DEBUG, 
                    filename= "C:\Adarsh\misc documents\lernen\LoggingModule_logfile.log",
                    format = '%(asctime)s: %(levelname)s : %(message)s'
                    )

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