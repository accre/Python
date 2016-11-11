#!/usr/bin/env python

from multiprocessing import Pool
import numpy as np
from helpers import CPUS_PER_TASK 
import argparse


def worker_pi(n):
  xy = np.random.rand(n, 2)
  return 4 * np.mean(np.sum(np.power(xy,2), axis=1) <= 1.0) 


def main(n=int(1e4), n_threads=CPUS_PER_TASK):
  print("{0} threads, {1} elements per thread".format(n_threads,n))

  pool = Pool(n_threads)
  result = np.mean(
    pool.map(worker_pi, (n for _ in range(n_threads)))
    )
  pool.close()
  pool.join()

  return result


if __name__ == "__main__":
  parser = argparse.ArgumentParser("Compute digits of pi in parallel")
  parser.add_argument('-n', '--niter', nargs='?', type=int, default=10000,
      help='number of iterations')

  args = parser.parse_args()
  print("pi is approximately %0.12f" % main(args.niter))
