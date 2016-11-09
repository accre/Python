#!/usr/bin/env python

import threading
import os

def worker():
    """ thread worker function """
    print("Hello")
    print("World!")
    return

threads = []

try:
  N = os.environ["SLURM_NNODES"]
except KeyError:
  print("SLURM environment variable unset: use salloc or sbatch to launch job")
  raise

for i in range(8):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
