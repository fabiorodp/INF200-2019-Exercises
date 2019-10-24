# -*- coding: utf-8 -*-

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'

"""The main program shall instantiate at least one generator of each 
class and print a few numbers from each."""


class LCGRand:
    """
    It implements a linear congruential generator (LCG),
    which generates numbers according to the following equation
    r[n+1] = a * r[n] mod m
    where a = 7**5 = 16807 and m = 2**31-1.
    The constructor takes a single argument,
    the seed (in addition to self).
    """
    def __init__(self, seed):
        pass

    def rand(self):
        """
        Returns the next random number
        Should not take any arguments except self
        """
        pass


class ListRand:
    """
    It shall be based on a list of numbers.
    The constructor takes a list of numbers, and rand() returns the
    first number from that list when it is called for the first time,
    the second number when called the second time...
    It shall raise a RuntimeError if rand() is called after the
    last number in the list has been delivered.
    """
    def __init__(self):
        pass

    def rand(self):
        """
        Returns the next random number
        Should not take any arguments except self
        """
        pass
