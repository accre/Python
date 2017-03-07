# -*- coding: utf-8 -*-
import contextlib
import time


@contextlib.contextmanager
def stopwatch(message):
  """Context manager that prints how long a block takes to execute."""
  t0 = time.time()
  try:
    yield
  finally:
    t1 = time.time()
print('Total elapsed time for %s: %f s' % (message, t1 - t0))
