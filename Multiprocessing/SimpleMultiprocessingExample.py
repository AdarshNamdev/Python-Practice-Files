import time
import multiprocessing

#start_time = time.perf_counter()

def sleeper():
    print("sleeping for 1 second...")
    time.sleep(1)
    print("done sleeping...")


if __name__ == "__main__":
    start_time = time.perf_counter()
    print("=============================== A simple program on multiprocessing ========================\n")
    myprocess = multiprocessing.Process(target = sleeper)
    myprocess.start()
    myprocess.join()

    end_time = time.perf_counter()

    print("Time taken to execute above code = {} second(s)".format(round(end_time - start_time, 2)))
