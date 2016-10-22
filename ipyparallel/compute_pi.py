#!/usr/bin/env python

import argparse
from ipyparallel import Client
import numpy as np
from helpers import stopwatch
import os


PI = 3.141592653589793

def worker_fun_1(n=1000):
  """ worker function """
  from random import random 
  s = 0
  for i in range(n):
    if random() ** 2 + random() ** 2 <= 1:
      s += 1
  
  return s 



def worker_fun_2(n=1000):
  """ worker function """
  import numpy as np
 
  chunksize = 1000000
  b = max(n // chunksize, 1)
 
  s = 0
  for i in range(b):
    s +=  np.sum(np.sum(np.square(np.random.rand(chunksize, 2)), axis=1) < 1.)

  slop = n - b * chunksize
  if n > 0:
    s +=  np.sum(np.sum(np.square(np.random.rand(slop, 2)), axis=1) < 1.)
  
  return s 


def main(profile, ntasks, niter):
  rc = Client(profile=profile)
  views = rc[:]
  # with views.sync_imports():
  #  import numpy as np

  n = round(niter / ntasks)

  results = views.apply_sync(worker_fun_2, n)
  my_pi = 4. * sum(results) / (n * ntasks)

  print("Estimate of pi: %0.16f" % my_pi)
  print("Actual pi:      %0.16f" % PI)
  print("Percent error:  %0.16f" % np.abs(100. * (PI - my_pi) / PI))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--profile", type=str, required=True,
      help="Name of IPython profile to use")
  parser.add_argument("-n", "--niter", type=int, required=True,
      help="Number of stochastic iterations")
  
  args = parser.parse_args()

  main(args.profile, int(os.environ['SLURM_NTASKS']), args.niter)
