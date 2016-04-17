"""
Created on #DATA
@author: Yida Yin
"""
import itertools
from Exceptions import InvalidPermutation


def is_An(func):
    # this function checks whether sigma belongs to Sn
    def statistics(sigma):
        if set(sigma) != set(range(1, len(sigma)+1)):
            raise InvalidPermutation
        return func(sigma)
    return statistics


def is_Bn(func):
    # this function checks whether sigma belongs to Bn
    def statistics(sigma):
        if len(set(sigma)) != len(sigma) or set([abs(i) for i in sigma]) != set(range(1, len(sigma)+1)):
            raise InvalidPermutation
        return func(sigma)
    return statistics


def is_Dn(func):
    # this function checks whether sigma belongs to Dn
    def statistics(sigma):
        # if not Bn
        if len(set(sigma)) != len(sigma) or set([abs(i) for i in sigma]) != set(range(1, len(sigma)+1)):
            raise InvalidPermutation
        # if not even
        if len([i for i in sigma if i < 0]) % 2 != 0:
            #print "Warning: Not A Even Permutation"
            pass
        return func(sigma)
    return statistics


class StatisticsOnAn(object):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

    @staticmethod
    def des(sigma):
        """
        :param sigma: permutation
        :return: Descent Statistics
        :rtype : int
        """
        res = len([i + 1 for i in range(len(sigma) - 1) if sigma[i] > sigma[i + 1]])
        return res

    @staticmethod
    def exc(sigma):
        """
        :param sigma: permutation
        :return: Excedance Statistics
        :rtype : int
        """
        res = len([i for i, s in enumerate(sigma) if s > i + 1])
        return res

    @staticmethod
    def inv(sigma):
        """
        :param sigma: permutation
        :return: Inversion Statistics
        :rtype : int
        """
        res = 0
        for x in itertools.combinations(sigma, 2):
            if x[0] > x[1]:
                res += 1
        return res

    @staticmethod
    def maj(sigma):
        """
        :param sigma: permutation
        :return: Major Index Statistics
        :rtype : int
        """
        res = sum([i + 1 for i in range(len(sigma) - 1) if sigma[i] > sigma[i + 1]])
        return res

    @staticmethod
    def Des(sigma):  # TODO
        return [i + 1 for i in range(len(sigma) - 1) if sigma[i] > sigma[i + 1]]


class StatisticsOnBn(StatisticsOnAn):

    @staticmethod
    @is_Bn
    def Neg(sigma):  # TODO
        return [i for i, s in enumerate(sigma) if s < 0]

    @staticmethod
    @is_Bn
    def neg(sigma):
        """
        :param sigma: permutation
        :return: Number of negative letters of sigma
        :rtype : int
        """
        return len(StatisticsOnBn.Neg(sigma))

    @staticmethod
    @is_Bn
    def fmaj(sigma):
        """
        :param sigma: Signed permutation
        :return: Flag Major Index Statistics = 2 * maj(sigma) + neg(sigma)
        :rtype : int
        """
        return 2 * StatisticsOnAn.maj(sigma) + StatisticsOnBn.neg(sigma)

    @staticmethod
    def partial_order(x1, x2):
        """
        return True if x1 > x2 based on the partial order, else False
        partial order: -1 < -2 < ... < -n < ... < 0 < 1 < 2 < ... < n < ...
        """
        if x1 >= 0 or x2 >= 0:
            return x1 > x2
        elif x1 < 0 and x2 < 0:
            return x1 < x2
        else:
            return x1 > 0

    @staticmethod
    @is_Bn
    def maj_partial(sigma):
        return sum([i + 1 for i in range(len(sigma) - 1) if StatisticsOnBn.partial_order(sigma[i], sigma[i + 1])])

    @staticmethod
    @is_Bn
    def fmaj_partial(sigma):
        """
        calculate the fmaj index based on partial order:
        -1 < -2 < ... < -n < ... < 0 < 1 < 2 < ... < n < ...
        """
        return 2*StatisticsOnBn.maj_partial(sigma) + StatisticsOnBn.neg(sigma)

    @staticmethod
    def length(sigma):
        return StatisticsOnAn.inv(sigma) - sum([sigma[i] for i in StatisticsOnBn.Neg(sigma)])

    @staticmethod
    @is_Bn
    def nmaj(sigma):
        NDes = [i + 1 for i in range(len(sigma) - 1) if sigma[i] > sigma[i + 1]]
        NDes += [-s for s in sigma if s < 0]
        return sum(NDes)
        # Alternatively,
        #return StatisticsOnBn.maj(sigma) - sum([sigma[i] for i in StatisticsOnBn.Neg(sigma)])


class StatisticsOnDn(StatisticsOnAn):
    @staticmethod
    @is_Dn
    def N1(sigma):
        return StatisticsOnBn.neg(sigma)

    @staticmethod
    @is_Dn
    def N2(sigma):
        N_2 = []
        for item in itertools.combinations(range(len(sigma)), 2):
            if sigma[item[0]] + sigma[item[1]] < 0:
                N_2.append([sigma[item[0]], sigma[item[1]]])
        return N_2

    @staticmethod
    @is_Dn
    def Dmaj(sigma):   # TODO
        if sigma:
            sigma = list(sigma)
            sigma[-1] = abs(sigma[-1])
            return StatisticsOnBn.fmaj(sigma)
        else:
            return 0

    @staticmethod
    @is_Dn
    def length(sigma):
        N_2 = StatisticsOnDn.N2(sigma)
        return len(N_2) + StatisticsOnAn.inv(sigma)


if __name__ == "__main__":
    test0 = [3, 5, 2, 4, 1, 6]
    test1 = [-3, 1, -6, 2, -4, -5]
    print StatisticsOnDn.length(test1)
