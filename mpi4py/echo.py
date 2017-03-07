#!/usr/bin/env python
from mpi4py import MPI
import subprocess

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

host_name = subprocess.check_output("hostname").strip()
print("Hostname: {0} Rank: {1}".format(host_name, rank))

if rank == 0:
  master = host_name
else:
  master = None

master = comm.bcast(master, root=0)
print("Hostname: {0} Master: {1}".format(host_name, master))
