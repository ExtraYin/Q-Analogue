"""
Created on 16/1/25
@author: Yida Yin
"""

from q_analogue import *
from utils import *
from SomeStatictics import StatisticsOnAn, StatisticsOnBn, StatisticsOnDn

def secondExample(n=3, k=1, test_q=None):
    test_q = 1 if test_q is None else test_q

    def ratio(j):
        a = (-1) ** j * QAnalogue.qExp(nCr(j, 2))
        b = QAnalogue.qFactorial(j)
        return a / b

    lhs = QAnalogue.performStatisticsOnq(StatisticsOnAn.maj,
                                         Permutation.generatePermutationsWithKFixedPoints(n, k))
    rhs = QAnalogue.qFactorial(n) / QAnalogue.qFactorial(k) * summation(ratio, 0, n - k)
    print lhs.subs('q', test_q) if hasattr(lhs, 'subs') else lhs
    print rhs.subs('q', test_q) if hasattr(rhs, 'subs') else rhs


def thirdExample(n=5, test_q=None):
    test_q = 1 if test_q is None else test_q
    result_0 = QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj,
                                              [item for item in
                                               Permutation.generateSignedPermutationsWithKFixedPoints(n, 0)])

    def ratio(k):
        a = (-1) ** k * QAnalogue.qExp(2 * nCr(k, 2))
        b = product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=k)
        return a / b

    result = product(fun=lambda k: QAnalogue.qNumber(2 * k), start=0, end=n) * summation(ratio, 0, n)
    print result_0.subs('q', test_q) if hasattr(result_0, 'subs') else result_0
    print result.subs('q', test_q) if hasattr(result, 'subs') else result


def fourthExample(n=3, k=1, test_q=None):
    test_q = 1 if test_q is None else test_q

    def ratio(j):
        a = ((-1) ** j) * QAnalogue.qExp(2 * nCr(j, 2))
        b = product(fun=lambda y: QAnalogue.qNumber(2 * y), start=0, end=j)
        return a / b

    lhs = QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj,
                                         Permutation.generateSignedPermutationsWithKFixedPoints(n, k))
    rhs = product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=n) / \
          product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=k) * \
          summation(ratio, 0, n - k)
    print lhs.subs('q', test_q) if hasattr(lhs, 'subs') else lhs
    print rhs.subs('q', test_q) if hasattr(rhs, 'subs') else rhs


def fourthExample_partial(n=3, k=1, test_q=None):
    test_q = 1 if test_q is None else test_q

    def ratio(j):
        a = ((-1) ** j) * QAnalogue.qExp(2 * nCr(j, 2))
        b = product(fun=lambda y: QAnalogue.qNumber(2 * y), start=0, end=j)
        return a / b

    lhs = QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj_partial,
                                         Permutation.generateSignedPermutationsWithKFixedPoints(n, k))
    rhs = product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=n) / \
          product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=k) * \
          summation(ratio, 0, n - k)
    print lhs.subs('q', test_q) if hasattr(lhs, 'subs') else lhs
    print rhs.subs('q', test_q) if hasattr(rhs, 'subs') else rhs


#print StatisticsOnBn.fmaj_partial([2, -5, -3, -1, 4])


def bi(sigma):
    n = len(sigma)
    res = []
    Des = StatisticsOnBn.Des(sigma)
    neg = len(Des)
    Des.sort()
    for item in sigma:
        if sigma >= 0:
            res.append(item)
        elif sigma < 0:
            res.append(Des[neg - Des.index(item) - 1])
    return res


def qNumber2(n):
    """
    :return: q-analogue of the positive integer n: [n]q = 1 + q + q^2 + ... + q^(n-1)
    """
    assert n >= 0
    if n == 0:
        return 1
    q = sympy.symbols("q")
    q *= (-1)
    res = 0
    for i in range(n):
        res += q ** i
    return (1 - q**n) / (1-q)


lhs = summation(lambda x: QAnalogue.qExp(StatisticsOnDn.Dmaj(x)), lst=Permutation.shuffle([3, -6, 5, -2], [1, 4]))
rhs = QAnalogue.qCombination_square(6, 4) * QAnalogue.qExp(StatisticsOnDn.Dmaj([3, -6, 5, -2]) + StatisticsOnDn.Dmaj([1, 4]))

lhs *= QAnalogue.qExp(1)
rhs *= QAnalogue.qExp(2)

print lhs.subs('q', 1.12)
print rhs.subs('q', 1.12)



