import threading
import time

"""
Output:
``````
Start of Program
End of Program
Wake up!

Explanation:
```````````
This python program when run will have two thread. One is the main thread and another is the
thread that we created using 'threading.Thread()'. 
The main thread continues to execute and prints only "Start of Program" and "End of Program", but not "Wake up!" in the second line,
Although the another threads has already called the 'takeanap' function but becasue of 5 second sleep time , there was a delay
and "Wake up!" gets printed int he end.

If this time.sleep(5) has not never been there then the output would be:

Start of Program
Wake up!
End of Program

"""

print("Start of Program")

def takeanap():
    time.sleep(5)
    print("Wake up!")

threadobj = threading.Thread(target = takeanap)
#print(threadobj)
threadobj.start()

print("End of Program")