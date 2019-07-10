#!/usr/bin/env python
#
# Python script demonstrating vectorized execution
#
from textwrap import dedent
from timeit import timeit
import numpy as np

SETUP = """
import numpy as np
N = int(1e6)
t = np.linspace(-10, 10, N)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
"""
NR = 10


def run_native():
    """native, naive, non-vectorized implementation"""
    native = dedent("""
        for i in range(N):
            x1[i] = np.sin(t[i])
    """)
    result = timeit(native, setup=SETUP, number=NR)
    print("native    : {:6.3f}s".format(result))


def run_vectorized():
    """vectorized implementation"""
    vectorized = dedent("""
        x2 = np.sin(t)
    """)
    result = timeit(vectorized, setup=SETUP, number=NR)
    print("vectorized: {:6.3f}s".format(result))


def test_equality():
    """Test equality of the methods, indepently of the speed test"""
    N = 10000
    t = np.linspace(-10, 10, N)
    x1 = np.zeros(len(t))
    x2 = np.zeros(len(t))

    for i in range(N):
        x1[i] = np.sin(t[i])

    x2 = np.sin(t)

    if (np.array_equal(x1,x2)):
        print("arrays equal!")


if __name__ == '__main__':
    run_native()
    run_vectorized()
    test_equality()
