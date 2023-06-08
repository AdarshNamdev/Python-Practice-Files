import threading

def display_multiplication_table(n):
    print("\n==================== MULTIPLICATION TABLE OF: {} =====================\n".format(n))
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n*i))


# this is the sequential way of calling a function

"""
display_multiplication_table(2)
display_multiplication_table(3)
display_multiplication_table(4)
display_multiplication_table(5)
"""


# executing the fuction with different arguments at once using threads !

my_threads = [threading.Thread(target = display_multiplication_table, args= (i,)) for i in (2,3,4,5)]
print(my_threads)

for a_thread in my_threads:
    a_thread.start()
    a_thread.join()    # this join() method makes the thread waits until the current thread runs and stops . *** see output without using the .join() method !!! ***