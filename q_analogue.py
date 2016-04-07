"""
Created on 16/1/25
@author: Yida Yin
"""
import itertools
import sympy
import utils
from GeneratePermutations import Permutation


class QAnalogue(object):
    # ------------Some q-analogue ----------------------
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

    @staticmethod
    def qNumber(n):
        """
        :return: q-analogue of the positive integer n: [n]q = 1 + q + q^2 + ... + q^(n-1)
        """
        assert n >= 0
        if n == 0:
            return 1
        q = sympy.symbols("q")
        res = 0
        for i in range(n):
            res += q ** i
        return res

    @staticmethod
    def qFactorial(n):
        """
        :return: q-analogue of n!: [n]q! = [1]q * [2]q * ... * [n]q
        """
        assert n >= 0
        res = 1
        for i in range(n + 1):
            res *= QAnalogue.qNumber(i)
        return res

    @staticmethod
    def qCombination(n, k):
        """
        :return: q-analogue of binary coefficient c(n,k): c[n,k]q = [n]q! / ([c]q! * [n-c]q! )
        """
        if n >= k >= 0:
            return QAnalogue.qFactorial(n) / (QAnalogue.qFactorial(k) * QAnalogue.qFactorial(n - k))
        return 0

    @staticmethod
    def qCombination_square(n, k):  # TODO:
        if n >= k >= 0:
            return utils.product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=n) / \
                   utils.product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=k) / \
                   utils.product(fun=lambda x: QAnalogue.qNumber(2 * x), start=0, end=n - k)
        return 0

    # ----- Some help functions ------------
    @staticmethod
    def performStatisticsOnq(statistic, generator):
        """
        :param statistic: A statistic function, such as maj, inv.
        :param generator: A generator generates permutations
        :return: A q-polynomial
        """
        q = sympy.symbols("q")
        res = 0
        pe = map(statistic, generator)
        pe_set = set(pe)
        for value in pe_set:
            res += pe.count(value) * q ** value
        return res

    @staticmethod
    def qExp(n):
        q = sympy.symbols("q")
        return q ** n


if __name__ == "__main__":
    from SomeStatictics import StatisticsOnAn, StatisticsOnBn, StatisticsOnDn
    n = 4
    # On group of Type-B three statistics should have the same distribution
    print QAnalogue.performStatisticsOnq(StatisticsOnBn.fmaj, Permutation.generateSignedPermutations(n)) \
          ==  QAnalogue.performStatisticsOnq(StatisticsOnBn.nmaj, Permutation.generateSignedPermutations(n)) \
          == QAnalogue.performStatisticsOnq(StatisticsOnBn.length, Permutation.generateSignedPermutations(n))