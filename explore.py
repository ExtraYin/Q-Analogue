"""
Created on 16/1/25
@author: Yida Yin
"""

from q_analogue import *
from utils import *
from SomeStatictics import StatisticsOnAn, StatisticsOnBn, StatisticsOnDn


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
    return (1 - q ** n) / (1 - q)


a1 = [3, 6, -5, -2]
a2 = [-1, 4, 7, -8]
lhs = summation(lambda x: QAnalogue.qExp(StatisticsOnDn.Dmaj(x)), lst=Permutation.shuffle(a1, a2))
rhs = QAnalogue.qExp(StatisticsOnDn.Dmaj(a1) + StatisticsOnDn.Dmaj(a2))
rhs *= QAnalogue.qCombination_square(len(a1)+len(a2), len(a1))

print lhs.subs('q', 1.12)
print rhs.subs('q', 1.12)


lhs *= QAnalogue.qExp(4)
rhs = summation(lambda x: QAnalogue.qExp(StatisticsOnBn.fmaj(x)), lst=Permutation.shuffle(a1, a2))
print lhs.subs('q', 1.12)
print rhs.subs('q', 1.12)





Permutation.shuffle(([1,3,4],[2,5]))
