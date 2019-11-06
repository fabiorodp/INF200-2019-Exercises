# -*- coding: utf-8 -*-
import random as rd

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class Walker:
    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker's home
        """
        self.x = [start]
        self.home, self.steps = home, 0

    def move(self):
        """Change coordinate by +1 or -1 with equal probability."""
        if rd.randint(1, 2) == 1:
            self.x.append(self.x[self.steps] + 1)
        else:
            self.x.append(self.x[self.steps] - 1)
        self.steps += 1

    def is_at_home(self):
        """Returns True if walker is at home position."""
        return self.x[self.steps] == self.home

    def get_position(self):
        """Returns current position."""
        return self.x[self.steps]

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.seed, self.start, self.home = seed, start, home

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of
        steps.

        Returns
        -------
        int
            The number of steps taken
        """
        rd.seed(self.seed)
        single = Walker(self.start, self.home)
        while not single.is_at_home():
            single.move()
        return single.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        return [self.single_walk() for _ in range(0, num_walks)]


if __name__ == '__main__':
    """
    The main section of the script shall simulate
    -  20 walks from start 0 to home 10
    -  20 walks from start 10 to home 0
    -  for each of those cases simulate *twice* with seed value 12345
        and *once* with seed value 54321
    -  print the resulting lists (six lists in total).
    """
    _start = [0, 0, 0, 10, 10, 10]
    _home = [10, 10, 10, 0, 0, 0]
    _seed = [12345, 12345, 54321, 12345, 12345, 54321]
    for x in range(len(_start)):
        w = Simulation(_start[x], _home[x], _seed[x])
        print(w.run_simulation(20))
