#!/usr/bin/env python
#
# Python 3.x script demonstrating pycuda  
#

from __future__ import print_function
import contextlib
import time

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np
import copy


@contextlib.contextmanager
def stopwatch(message):
    """Context manager that prints how long a block takes to execute."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
    print('Total elapsed time for %s: %f s' % (message, t1 - t0))


mod = SourceModule("""
  __global__ void doublify(float *a)
  {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    a[idx] = sin(a[idx]);
  }
  """)

sin_devf = mod.get_function("doublify")

def test_one(n):
    """ Tests an element-wise function 

    :param n: integer number of elements
    :return None
    """
    print(n)

    a = np.ones((n,1), dtype=np.float32)
    with stopwatch("testing sine function on CPU"):
        y = np.sin(a)      

    #y_dev = copy.copy(a) 
    y_dev = np.ones((n,1), dtype=np.float32)
    with stopwatch("testing sine function on GPU"):
        sin_devf(cuda.InOut(y_dev), 
                block=(512, 1, 1), 
                grid=(int(n / 512), 1))      
    print(np.sum((y_dev - y) ** 2))
     

if __name__ == "__main__":

    test_one(2 ** 23);
    if False:
        test_two(2000);
        test_three(2000);
