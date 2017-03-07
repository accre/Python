#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = np.random.rand(1000,1)
else:
    data = None
data = comm.scatter(data, root=0)

print("Process %d has data" % rank, data)

data *= 2
print("Process %d now has data" % rank, data)

data /= 2
print("Process %d now has data" % rank, data)

if 0:
    comm.reduce(data, op=MPI.SUM)

    print("The root is %d" % MPI.ROOT)
    if rank == 0:
        print("The sum is %d" % data)
