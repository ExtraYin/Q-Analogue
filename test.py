"""
Created on 16/4/19
@author: Yida Yin
"""

from q_analogue import *
from utils import *
from SomeStatictics import StatisticsOnAn, StatisticsOnBn, StatisticsOnDn

n = 5

print "On group of Type-B three statistics should have the same distribution"
assert QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj, Permutation.generateSignedPermutations(n)) \
        == QAnalogue.performStatisticsOnq(StatisticsOnBn.nmaj, Permutation.generateSignedPermutations(n)) \
        == QAnalogue.performStatisticsOnq(StatisticsOnBn.length, Permutation.generateSignedPermutations(n))
print "Pass"

print "Calculate major([2, -5, -3, -1, 4])"
assert StatisticsOnBn.major([2, -5, -3, -1, 4]) == 6
print "Pass"

print "Calculate flag-major([2, -5, -3, -1, 4])"
assert StatisticsOnBn.flag_major([2, -5, -3, -1, 4]) == 15
print "Pass"


print "Calculate inv([2, -5, -3, -1, 4])"
assert StatisticsOnBn.inv([2, -5, -3, -1, 4]) == 3
print "Pass"

print "Calculate Des([2, -5, -3, -1, 4])"
# Note this Des is not the same as the Des on An, instead, it uses the partial order
assert StatisticsOnBn.Des([2, -5, -3, -1, 4]) == [1, 2, 3]
print "Pass"





