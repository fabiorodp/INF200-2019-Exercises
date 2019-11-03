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
    a, m = 7 ** 5, 2 ** 31 - 1

    def __init__(self, seed):
        self.generator, self.infinite = seed, True

    def rand(self):
        """
        Returns the next random number
        Should not take any arguments except self
        """
        self.generator *= LCGRand.a
        self.generator %= LCGRand.m
        return self.generator

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while self.infinite:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError('__iter__ called twice')
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError('__next__ called before __iter__')
        if self.num_generated_numbers == self.length:
            raise StopIteration
        self.num_generated_numbers += 1
        return self.generator.rand()
