#!/usr/bin/env python

import argparse
from ipyparallel import Client
import numpy as np
import sympy
from helpers import stopwatch, to_numeric
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

  results = views.apply_sync(worker_fun, n)
  my_pi = 4. * simpy.Ration(sum(results), (n * ntasks)).n(20)

  with open(filename, "w") as f:
    f.write("Estimate of pi: %0.16f\n" % my_pi)
    f.write("Actual pi:      %0.16f\n" % PI)
    f.write("Percent error:  %0.16f\n" % np.abs(100. * (PI - my_pi) / PI))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--profile", type=str, required=True,
      help="Name of IPython profile to use")
  parser.add_argument("-n", "--niter", type=str, required=True,
      help="Number of stochastic iterations")
  parser.add_argument("-o", "--output", type=str, required=True,
      help="Name of output file for writing")

  args = parser.parse_args()

  main(args.profile, to_numeric(os.environ['SLURM_NTASKS']), to_numeric(args.niter))
