"""
Table 34-1. try statement clause forms

Clause form                                          Interpretation
````````````                                       ``````````````````
except                           :          Catch all (or all other) exception types.
except name                      :          Catch a specific exception only.
except name as value             :          Catch the listed exception and assign its instance.
except (name1, name2)            :          Catch any of the listed exceptions.
except (name1, name2) as value   :          Catch any listed exception and assign its instance.
else                             :          Run if no exceptions are raised in the try block.
finally                          :          Always perform this block on exit


Formally, there may be any number of except clauses, but you can code else only if
there is at least one except, and there can be only one else and one finally. Through
Python 2.4, the finally clause must appear alone (without else or except); the try/
finally is really a different statement. As of Python 2.5, however, a finally can appear
in the same statement as except and else




"""


try:
    with open("D:\Github\Python-Practice-Files\IamDone", 'r') as fh:
        for line in fh:
            print(line)

except Exception as exep:
    print("We have some error: ", exep)

else:
    print("I only runs when the TRY block ran successfully without an execption")

finally:
    print("Oh Boy! finally block always runs! no matter what -)")