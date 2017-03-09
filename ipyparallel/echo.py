#!/usr/bin/env python

from __future__ import print_function
import argparse
from ipyparallel import Client
import os
from helpers import to_numeric


def worker_fun():
  hostname = subprocess.check_output("hostname").strip()
  print(hostname) 


def main(profile, ntasks, filename_out):
  rc = Client(profile=profile)
  views = rc[:]
  with views.sync_imports():
    import subprocess
  
  views.apply_sync(worker_fun)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--profile", type=str, required=True,
      help="IPython profile")
  parser.add_argument("-t", "--ntasks", type=int, required=False,
      help="Number of tasks",
      default=to_numeric(os.environ['SLURM_NTASKS'])
      )
  parser.add_argument("-o", "--output", type=str, required=True,
      help="Name of output file for writing")

  args = parser.parse_args()

  main(args.profile, 
      args.ntasks, 
      args.output)

