
# this is a decorator function

def greet(decoratedfunction):
    def modify_decorated_funcs(*args):
        print("Good Morning Guys! this function is decorated with greetings")
        result = decoratedfunction(*args)
        print("Summation is: ",result)
        print("Wow! Thanks for using this function. Have a great day ahead.")

        return result
        
    return modify_decorated_funcs

@greet
def adder(*args):   # <== decorated function
    return sum(args)


