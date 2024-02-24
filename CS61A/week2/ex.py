"""Our first Python source file."""
# python3 -m doctest ex.py
from operator import floordiv, mod


def divide_exact(n, d=10):
  """Return the quotient and remainder of dividing N by D

  >>> q, r = divide_exact(2013, 10)
  >>> q
  201
  >>> r
  3
  """
  return floordiv(n, d), mod(n, d)

def absolute_value(x):
  """Return the absolute value of x."""
  # python3 -i ex.py
  if x < 0:
    return -x
  elif x == 0:
    return 0
  else:
    return x