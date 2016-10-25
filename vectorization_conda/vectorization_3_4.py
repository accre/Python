#!/usr/bin/env python
#
# Python 3.x script demonstrating vectorized execution
#
import numpy as np
from timeit import timeit

N = 10000
nr = 100
t = np.linspace(-10, 10, N)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))

# native, naive, non-vectorized implementation
def native():
  for i in range(N):
    x1[i] = np.sin(t[i])
print("native    : %fs" % timeit("native()", number=nr, globals=globals()))

# vectorized implementation
def vectorized():
  x2 = np.sin(t)

print("vectorized: %fs" % timeit("vectorized()", number=nr, globals=globals()))

native()
vectorized()

if ( np.array_equal(x1,x2) ):
    print("arrays equal!")
