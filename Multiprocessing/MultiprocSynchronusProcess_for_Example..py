import time
import multiprocessing

start_time = time.perf_counter()

def sleeper():
    print("sleeping for 1 second...")
    time.sleep(1)
    print("done sleeping...")

if __name__ == "__main__":
    """
    This below 'for' loop will make make the process run Synchronously as we are using the .join() method
    inside the loop body which is making every process to finish first before the next process starts.
    """
    for _ in range(5):
        print(f"======= PROCESS #{_+1} ======")
        process = multiprocessing.Process(target = sleeper)
        process.start()
        process.join()

    end_time = time.perf_counter()

    print("Time taken to execute above code = {} second(s)".format(round(end_time - start_time, 2)))
    


    