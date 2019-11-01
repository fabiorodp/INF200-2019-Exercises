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

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        pass


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
        pass

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
        pass


random_number_generator = LCGRand(1)
for rand in generator.random_sequence(10):
    print(rand)

for i, rand in generator.infinite_random_sequence():
    print(f'The {i}-th random number is {rand}')
    if i > 100:
        break
