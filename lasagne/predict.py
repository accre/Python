#!/usr/bin/env python

"""
"""

from __future__ import print_function

import numpy as np
import theano
import theano.tensor as T

import lasagne
from lasagne.utils import floatX

import dill as pickle

from itertools import count
import matplotlib.image as mpimg

def load_data(img_names=["my_four.tif", 
                         "my_four_fancy.tif",
                         "my_four_small.tif"
                         ]):
  """ Loads an input 8 bit image and transforms it to the proper numpy array
  
  :param img_names list of image file paths, assumed to be 28 x 28 uint8 
  :return numpy array of floatX
  """
 
  n_imgs = len(img_names)
  b = np.ones(shape=(n_imgs, 1, 28, 28), dtype=theano.config.floatX)

  for i, img_name in enumerate(img_names):
    a = np.array(mpimg.imread(img_name)) / floatX(256) 
    b[i, 0, :, :] = a
  
  return b


def load_model(data):
  """ Loads a saved lasagne model to use for prediction. 
  
  :param None
  :return trained network"""

  with open('model.dpkl', 'rb') as p_input:
    network = pickle.load(p_input)

  with np.load('model.npz') as f:
    param_values = [f['arr_%d' % i] for i in range(len(f.files))]
  lasagne.layers.set_all_param_values(network, param_values)

  probability = np.array(lasagne.layers.get_output(network, data, 
    deterministic=True).eval())
  
  for row in probability:
    prob_pred = sorted(list(zip(row, count())), reverse=True)
    print('Prediction: %d' % np.argmax(row), end=": ")
    for prob, pred in prob_pred:
      print("%d (%f)" % (pred, prob), end=', ')  
    print()
  
  return probability

def make_predictions():
  d = load_data()
  m = load_model(d)
  return m

if __name__ == "__main__":
  make_predictions()
