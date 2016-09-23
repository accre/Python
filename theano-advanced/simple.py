#!/usr/bin/env python

from helpers import stopwatch
import numpy as np
import theano
import theano.tensor as T
from theano.tensor.nlinalg import matrix_inverse


FLOATX = theano.config.floatX
rng = np.random

x = T.vector('x')
out = T.sin(x)
f = theano.function([x], outputs=[out])

with stopwatch("computing sine of all elements"):
  g = f(rng.rand(2 ** 23).astype(FLOATX))


if 1:
  A = T.matrix('A')
  b = T.vector('b')
  out = T.dot(matrix_inverse(A), b)

  f = theano.function([A, b], out)

  N = 2048
  with stopwatch("computing A inverse b"):
    g = f(rng.rand(N, N).astype(FLOATX), rng.rand(N).astype(FLOATX))
