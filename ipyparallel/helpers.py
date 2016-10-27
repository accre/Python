# -*- coding: utf-8 -*-
import contextlib
import time


@contextlib.contextmanager
def stopwatch(message,summary=None):
  """Context manager that prints how long a block takes to execute."""
  t0 = time.time()
  try:
    yield
  finally:
    t1 = time.time()
  elapsed = t1-t0
  print('Total elapsed time for %s: %f s' % (message, elapsed))
  if summary is not None:
    summary['elapsed'] = elapsed 


def to_numeric(n):
  try:
    return int(n)
  except ValueError:
    try:
      return int(float(n))
    except:
      raise
  except:
    raise
