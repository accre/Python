#!/usr/bin/env python

from helpers import stopwatch
import numpy as np
import theano
import theano.tensor as T
from theano.tensor.nlinalg import matrix_inverse

## Perform an element-wise operation on a vector
# read the float specification from the configuration
FLOATX = theano.config.floatX

# Set the random number generator
rng = np.random

# Create theano tensor variables
x = T.dvector('x')
out = T.sum(T.sin(x))

# Create the symbolic graph
f = theano.function([x], outputs=[out])

# Create the host data
x_data = rng.rand(2 ** 26).astype(FLOATX)

with stopwatch("computing sum of sine of all elements"):
  f = theano.function([x], outputs=T.sum(T.sin(x)))
  sum_y0 = f(x_data)
  print("%0.6f" % sum_y0)


## Solve a matrix equation 
A = T.matrix('A')
b = T.vector('b')
out = T.dot(matrix_inverse(A), b)
f = theano.function([A, b], out)


N = 2 ** 13
A_host = rng.rand(N, N).astype(FLOATX)
b_host = rng.rand(N).astype(FLOATX)

with stopwatch("computing A inverse b"):
  g = f(A_host, b_host)
