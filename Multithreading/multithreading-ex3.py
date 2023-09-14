import threading
import time

def my_function():
    print("Start of the thread")
    time.sleep(3)
    print("End of the thread")

# Create a thread
thread = threading.Thread(target=my_function, daemon= True)

# Start the thread
thread.start()

print("Main thread continues executing other tasks")
print("Main thread finished")