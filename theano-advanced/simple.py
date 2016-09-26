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
x = T.vector('x')
out = T.sin(x)

# Create the symbolic graph
f = theano.function([x], outputs=[out])

# Compute the result
with stopwatch("computing sine of all elements"):
  g = f(rng.rand(2 ** 23).astype(FLOATX))


## Solve a matrix equation 
A = T.matrix('A')
b = T.vector('b')
out = T.dot(matrix_inverse(A), b)

f = theano.function([A, b], out)

N = 2048
with stopwatch("computing A inverse b"):
  g = f(rng.rand(N, N).astype(FLOATX), rng.rand(N).astype(FLOATX))
