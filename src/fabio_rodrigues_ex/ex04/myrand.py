# -*- coding: utf-8 -*-

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class LCGRand:
    """
    It implements a linear congruential generator (LCG),
    which generates numbers according to the following equation
    r[n+1] = a * r[n] mod m
    where a = 7**5 = 16807 and m = 2**31-1.
    The constructor takes a single argument,
    the seed (in addition to self).
    """
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.seed_list = [seed]
        self.index = 0

    def rand(self):
        """
        Returns the next random number
        Should not take any arguments except self
        """
        self.seed_list.append(LCGRand.a * self.seed_list[self.index] %
                              LCGRand.m)
        self.index += 1
        return self.seed_list[self.index]


class ListRand:
    """
    It shall be based on a list of numbers.
    The constructor takes a list of numbers, and rand() returns the
    first number from that list when it is called for the first time,
    the second number when called the second time...
    It shall raise a RuntimeError if rand() is called after the
    last number in the list has been delivered.
    """

    def __init__(self, __list):
        self.__list = __list
        self.iter_list = iter(self.__list)
        self.__index = 0

    def rand(self):
        """
        Returns the next random number
        Should not take any arguments except self
        """

        """
        if list_num < 0:
            raise RuntimeError('Method called after the last number in '
                               'the list has been delivered.')
        """
        self.__index += 1
        if self.__index > len(self.__list):
            raise RuntimeError('Method called after the last number in '
                               'the list has been delivered.')
        return next(self.iter_list)


if __name__ == '__main__':

    a, b = 346, [4, 5, 29, 11]

    # instantiate at least one generator of each class
    c1 = LCGRand(a)
    c2 = ListRand(b)

    # print a few numbers from each
    print(c1.rand(), c1.rand(), c1.rand(), c1.rand(), c1.rand())
    print(c2.rand(), c2.rand(), c2.rand(), c2.rand())
