import time
import multiprocessing

start_time = time.perf_counter()

def sleeper():
    print("sleeping for 1 second...")
    time.sleep(1)
    print("done sleeping...")

if __name__ == "__main__":
    """
    This below 'for' loop will make make the processes run A-Synchronously as we are using the .join() method
    inside the another 'for' loop which is making every process to finish once there execution is completed.

    Take a close look at the execution time !
    """
    list_of_processes = []
    for _ in range(5):
        print(f"======= PROCESS #{_+1} ======")
        process = multiprocessing.Process(target = sleeper, args = [])
        process.start()
        #process.join()
        list_of_processes.append(process)

    for process in list_of_processes:
        process.join()

    end_time = time.perf_counter()

    print("Time taken to execute above code = {} second(s)\n".format(round(end_time - start_time, 2)))
    


    