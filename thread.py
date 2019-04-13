#!/usr/bin/python

import threading
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )


if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_time, args=("Thread-1", 4, )) 
    t2 = threading.Thread(target=print_time, args=("Thread-2", 8, )) 
    t3 = threading.Thread(target=print_time, args=("Thread-3", 12, )) 
  
    # starting threads 
    t1.start() 
    t2.start() 
    t3.start()
    # wait until threads are completely executed 
    t1.join() 
    t2.join() 
    t3.join()
    # all threads completely executed 
    print("Done!") 











