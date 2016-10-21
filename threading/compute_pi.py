#!/usr/bin/env python

import threading
import numpy as np
from helpers import stopwatch

def worker(result, index, num_elems):
  """ thread worker function """
  xy = np.random.rand(num_elems,2)  
  result[index] = 4 * np.mean(xy[:,0] ** 2 + xy[:,1] ** 2 < 1.0)


if __name__ == "__main__":
  threads = []
  num_threads = 16 
  n_per_thread = 1000000

  t0_summary = dict()
  t1_summary = dict()

  with stopwatch("multi-threaded execution", t0_summary):
    r_par = np.empty(num_threads)
    
    # Starts the processes
    for i in range(num_threads):
      t = threading.Thread(target=worker, 
          args=(r_par, i, n_per_thread))
      threads.append(t)
      t.start()
    
    # Joins the worker threads to the "master" thread
    for i in range(num_threads):
      t.join()

    print("Estimate of pi: %f" % r_par.mean())

  with stopwatch("single-threaded execution", t1_summary):
    r_seq = np.empty(1) 
    worker(r_seq, 0, num_threads * n_per_thread)
    print("Estimate of pi: %f" % r_seq[0])

  print("\nSpeedup: %f" % (t1_summary['elapsed'] / t0_summary['elapsed']))
