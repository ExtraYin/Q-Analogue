"""
Created on 16/4/19
@author: Yida Yin
"""

from q_analogue import *
from utils import *
from SomeStatictics import StatisticsOnAn, StatisticsOnBn, StatisticsOnDn

n = 5

print "---> Calculate major([2, -5, -3, -1, 4])"
assert StatisticsOnBn.major([2, -5, -3, -1, 4]) == 6
print "Pass"

print "---> Calculate flag-major([2, -5, -3, -1, 4])"
assert StatisticsOnBn.flag_major([2, -5, -3, -1, 4]) == 15
print "Pass"

print "---> Calculate inv([2, -5, -3, -1, 4])"
assert StatisticsOnBn.inv([2, -5, -3, -1, 4]) == 3
print "Pass"

print "---> Calculate Des([2, -5, -3, -1, 4])"
# Note this Des is not the same as the Des on An, instead, it uses the partial order
assert StatisticsOnBn.Des_partial([2, -5, -3, -1, 4]) == [1, 2, 3]
print "Pass"

# ----------------------------------------------------------------------------------------------------------

print "---> On group of Type-B three statistics should have the same distribution"
assert QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj, Permutation.generateSignedPermutations(n)) \
       == QAnalogue.performStatisticsOnq(StatisticsOnBn.nmaj, Permutation.generateSignedPermutations(n)) \
       == QAnalogue.performStatisticsOnq(StatisticsOnBn.length, Permutation.generateSignedPermutations(n))
print "Pass"


# -----------------------------------------------------------------------------------------------------------
def derangement_on_an(n=3, k=1, test_q=None):
    """WACH's formula"""
    test_q = 1 if test_q is None else test_q

    def ratio(j):
        a = (-1) ** j * QAnalogue.qExp(nCr(j, 2))
        b = QAnalogue.qFactorial(j)
        return a / b

    lhs = QAnalogue.performStatisticsOnq(StatisticsOnAn.maj,
                                         Permutation.generatePermutationsWithKFixedPoints(n, k))
    rhs = QAnalogue.qFactorial(n) / QAnalogue.qFactorial(k) * summation(ratio, 0, n - k)
    assert lhs.subs('q', test_q) == rhs.subs('q', test_q)


print "---> Derangement on An"
derangement_on_an()
print "Pass"


def derangement_on_bn(n=5, test_q=None):
    """CHOW's formula"""
    test_q = 1 if test_q is None else test_q
    result_0 = QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj,
                                              [item for item in
                                               Permutation.generateSignedPermutationsWithKFixedPoints(n, 0)])

    def ratio(k):
        a = (-1) ** k * QAnalogue.qExp(2 * nCr(k, 2))
        b = product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=k)
        return a / b

    result = product(fun=lambda k: QAnalogue.qNumber(2 * k), start=0, end=n) * summation(ratio, 0, n)
    assert result_0.subs('q', test_q) == result.subs('q', test_q)


print "---> Derangement on Bn"
derangement_on_bn()
print "Pass"

print "---> Garsia-Gessel Theorem"
a1 = [3, 6, -5, -2]
a2 = [-1, 4, 7, -8]
lhs = summation(lambda x: QAnalogue.qExp(StatisticsOnBn.fmaj(x)), lst=Permutation.shuffle(a1, a2))
rhs = QAnalogue.qExp(StatisticsOnBn.fmaj(a1) + StatisticsOnBn.fmaj(a2))
rhs *= QAnalogue.qCombination_square(len(a1)+len(a2), len(a1))
assert abs(lhs.subs('q', 1.12) - rhs.subs('q', 1.12)) < 0.000000001
assert abs(lhs.subs('q', 0.12) - rhs.subs('q', 0.12)) < 0.000000001
print "Pass"
