"""
Created on 16/1/25
@author: Yida Yin
"""
import math


# ----------- Some other operations -----------------
def product(fun, start=1, end=1, lst=None):
    """
    return the product of function "fun", from start to end.
    """
    lst = range(start, end + 1) if lst is None else lst
    return reduce(lambda x, y: x * y, map(fun, lst))


def summation(fun, start=1, end=1, lst=None):
    """
    return the sum of function "fun", from start to end.
    """
    lst = range(start, end + 1) if lst is None else lst
    return sum(map(fun, lst))


def combineTwoFun(fun1, fun2):
    return lambda x: fun1(fun2(x))


def nCr(n, r):
    if n < r:
        return 0
    f = math.factorial
    return f(n) / f(r) / f(n - r)