#!/usr/bin/env python

from random import random

MY_STRING = "This string belongs to the global namespace" \
  "but using globals is discouraged"
print(MY_STRING)


def sub_fun(str1, str2="World!", threshold=0.5):
  """ Prints a string determined by the input

  :param threshold: specifies minimum value that prints 
      "Hello"; default=0.5
  :return None
  """

  if random() > threshold:
    print(str1)
  else:
    print(str2)


def main_fun():
  """ The primary function of the program """
  sub_fun("Hello")
  sub_fun("Hello", "this is dog")
  sub_fun("Hello", str2="this is dog!", threshold=0.7)


if __name__ == "__main__":
  """ __name__ == "__main__" is true if the program
  is executing as a standalone """
  main_fun()
