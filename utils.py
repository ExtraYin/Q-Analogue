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


if __name__ == "__main__":
    pass
    #from q_analogue import *
    # 2 * 4 * 6 * 8 * 10 =
    #print product(lambda x: 2*x, 1, 5) == 3840
    # [2]q! * [4]q! * [6]q! = (q + 1)*(q**3 + q**2 + q + 1)*(q**5 + q**4 + q**3 + q**2 + q + 1)
    #print product(fun=lambda k: QAnalogue.qNumber(2*k), start=1, end=3)