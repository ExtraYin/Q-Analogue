"""
Created on #DATA
@author: Yida Yin
"""
import itertools


class Permutation(object):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

    @staticmethod
    def generatePermutations(n=1):
        """
        generate permutations of length n
        :rtype : generator
        """
        pe = range(1, n + 1)
        return itertools.permutations(pe)

    @staticmethod
    def generatePermutationsWithKFixedPoints(n=1, k=0):
        """
        :param k: number of fixed points
        :return: a permutation with k fixed points
        for n=3, k=0, it's the derangement of number 3,
        which is [2,3,1] and [3,1,2]
        """
        pe = range(1, n + 1)
        for typeA in itertools.permutations(pe):
            if len([i for i in typeA if i == typeA.index(i) + 1]) == k:
                yield (typeA)

    @staticmethod
    def generateSignedPermutations(n=1):
        """
        generate signed permutations of length n
        :rtype : generator
        """
        pe = range(1, n + 1)
        for typeA in itertools.permutations(pe):
            typeB = list(typeA)
            for i in range(len(pe) + 1):
                for chosenElements in itertools.combinations(typeB, i):
                    for element in chosenElements:
                        typeB[typeB.index(element)] = (-1) * element
                    yield tuple(typeB)
                    typeB = list(typeA)

    @staticmethod
    def generateSignedPermutationsWithKFixedPoints(n=1, k=0):
        """
        :param k: number of fixed points
        """
        for typeB in Permutation.generateSignedPermutations(n):
            if len([i for i in typeB if i == typeB.index(i) + 1]) == k:
                yield (typeB)

    @staticmethod
    def generateZeroOne(zero, one):  # TODO: optimize
        for chosen in itertools.combinations(range(zero+one), zero):
            zero_one = []
            i1 = 0
            i2 = 0
            for j in range(zero+one):
                if j in chosen:
                    zero_one.append(0)
                    i1 += 1
                else:
                    zero_one.append(1)
                    i2 += 1
            yield zero_one

    @staticmethod
    def shuffle(p1, p2):  # TODO: optimize
        n = len(p1) + len(p2)
        for chosen in itertools.combinations(range(n), len(p1)):
            shu = []
            i1 = 0
            i2 = 0
            for j in range(n):
                if j in chosen:
                    shu.append(p1[i1])
                    i1 += 1
                else:
                    shu.append(p2[i2])
                    i2 += 1
            yield (shu)

    @staticmethod
    def generate_Even_Signed_Permutation(n):
        for item in Permutation.generateSignedPermutations(n):
            if len(filter(lambda x: x < 0, item)) % 2 == 0:
                yield(item)

    @staticmethod
    def generate_Even_Signed_Permutation_With_k_Fixed_Points(n, k):
        for item in Permutation.generate_Even_Signed_Permutation(n):
            if len([i for i in item if i == item.index(i) + 1]) == k:
                yield (item)

    @staticmethod
    def generate_Delta(n):
        for item in Permutation.generateSignedPermutations(n):
            if item[-1] > 0:
                yield (item)


if __name__ == "__main__":
    print [item for item in Permutation.generatePermutations(0)] == [()]
    print [item for item in Permutation.generatePermutations(-1)] == [()]
    print [item for item in Permutation.generatePermutations(3)] == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    print [item for item in Permutation.generateSignedPermutationsWithKFixedPoints(3, 1)] == [(-1, -2, 3), (-1, 2, -3), (1, -2, -3), (1, 3, 2), (1, -3, 2), (1, 3, -2), (1, -3, -2), (2, 1, 3), (-2, 1, 3), (2, -1, 3), (-2, -1, 3), (3, 2, 1), (-3, 2, 1), (3, 2, -1), (-3, 2, -1)]

    print [item for item in Permutation.generateSignedPermutations(0)] == [()]
    print [item for item in Permutation.generateSignedPermutations(2)] == [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

    print [item for item in Permutation.generateSignedPermutationsWithKFixedPoints(2, 1)] == [(-1, 2), (1, -2)]
    print [item for item in Permutation.generateSignedPermutationsWithKFixedPoints(2, 0)] == [(-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

    print [item for item in Permutation.generateZeroOne(2, 2)] == [[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print [item for item in Permutation.generateZeroOne(2, 0)] == [[0, 0]]

    print [item for item in Permutation.shuffle([1, 2], [3, 0])] == [[1, 2, 3, 0], [1, 3, 2, 0], [1, 3, 0, 2], [3, 1, 2, 0], [3, 1, 0, 2], [3, 0, 1, 2]]
    print [item for item in Permutation.shuffle([], [])] == [[]]