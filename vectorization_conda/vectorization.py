#!/usr/bin/env python
#
# Python 3.x script demonstrating vectorized execution
#
from __future__ import print_function
from timeit import timeit
setup = """
import numpy as np

N = int(1e6)
t = np.linspace(-10, 10, N)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
"""

nr = 10

# native, naive, non-vectorized implementation
native = """
for i in range(N):
    x1[i] = np.sin(t[i])
"""

print("native    : %fs" % timeit(native, setup=setup, number=nr))

# vectorized implementation
vectorized = """
x2 = np.sin(t)
"""
print("vectorized: %fs" % timeit(vectorized, setup=setup, number=nr))


def test_equality():
  """ Test equality of the methods, indepently of the speed test """
  
  import numpy as np
  
  N = 10000
  t = np.linspace(-10, 10, N)
  x1 = np.zeros(len(t))
  x2 = np.zeros(len(t))
   
  for i in range(N):
    x1[i] = np.sin(t[i])
    
  x2 = np.sin(t)
  
  if ( np.array_equal(x1,x2) ):
    print("arrays equal!")

test_equality()
