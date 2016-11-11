#!/usr/bin/env python

import os

def get_cpus_per_task():
  """ Returns the SLURM environment variable if set else throws
  KeyError """

  try:
    return os.environ["SLURM_CPUS_PER_TASK"]
  except KeyError:
    print("SLURM environment variable unset: \
        use salloc or sbatch to launch job")
    raise

CPUS_PER_TASK = int(get_cpus_per_task())
