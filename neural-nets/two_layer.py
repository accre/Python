#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import numpy as np
import argparse


def nonlin(x, deriv=False):
  if deriv:
    return x * (1 - x)
  return 1.0 / (1 + np.exp(-x))


def two_layer_eg(alpha=1.0, hidden_dim=4):
  """ Constructs a simple neural network for learning binary classes.

  :param alpha: tuning parameter for slope in gradient descent method
  :param hidden_dim: number of hidden dimensions of the feature space
  :return None
  """
  
  # Sets the random seed for repeatability
  np.random.seed(42)
  
  n_features = 3
  n_observations = 4 

  if 0:
    X = np.array([ [0, 0, 1],
                   [0, 1, 1],
                   [1, 0, 1],
                   [0, 1, 1]
                 ])
    y = np.array([[0, 0, 1, 1]]).T
  else:
    X = np.random.randint(2, size=(n_observations, n_features))
    y = np.random.randint(2, size=(n_observations, 1))


  n_realizations = 1000
  errors = np.empty((n_realizations, 1), dtype=np.float)

  
  synapse_0 = 2 * np.random.rand(n_features, hidden_dim) - 1
  synapse_1 = 2 * np.random.rand(hidden_dim, 1) - 1
  
  print('Iteration / Error:')

  for i in range(n_realizations):
    
    # Feed forward through layers 0, 1, and 2
    layer_1 = nonlin(np.dot(X, synapse_0))
    layer_2 = nonlin(np.dot(layer_1, synapse_1))
    
    # how much did we miss the target value?
    layer_2_error = y - layer_2
    
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    layer_2_delta = layer_2_error * nonlin(layer_2, deriv=True)
    
    # how much did each layer_1 value contribute to the layer_2 error 
    # (according to the weights)?
    layer_1_error = layer_2_delta.dot(synapse_1.T)
    
    # in what direction is the target layer_1?
    # were we really sure? if so, don't change too much.
    layer_1_delta = layer_1_error * nonlin(layer_1, deriv=True)
    
    synapse_1 += alpha * layer_1.T.dot(layer_2_delta)
    synapse_0 += alpha * X.T.dot(layer_1_delta)
    
    errors[i] = np.sum(layer_2_error ** 2)
    if i % 100 == 0:
      print("%d / %f" % (i, errors[i]))
    

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Get command line options.")
  parser.add_argument("--alpha", 
      metavar="a", 
      type=float, 
      nargs="?",
      default=1.0,
      help="tuning parameter for stochastic gradient descent")

  parser.add_argument("--hidden_dim",
      type=int,
      nargs="?",
      default=4,
      help="number of hidden layers in the neural net"
      )

  args = parser.parse_args()
  
  two_layer_eg(alpha=args.alpha, hidden_dim=args.hidden_dim)
