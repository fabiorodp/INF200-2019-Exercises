# -*- coding: utf-8 -*-
from walker_sim import Walker, Simulation
import random as rd

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit, self.right_limit = left_limit, right_limit

    def is_at_left_limit(self):
        return self.get_position() == self.left_limit

    def is_at_right_limit(self):
        return self.get_position() == self.right_limit

    def move(self):
        if rd.randint(1, 2) == 1:
            if self.is_at_right_limit():  # if at r-limit, then pass
                pass
            else:  # then move +1 and step +1
                self.x.append(self.x[self.steps] + 1)
                self.steps += 1
        else:
            if self.is_at_left_limit():  # if at l-limit, then pass
                pass
            else:  # then move -1 and step +1
                self.x.append(self.x[self.steps] - 1)
                self.steps += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.left_limit, self.right_limit = left_limit, right_limit

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
        single = BoundedWalker(self.start, self.home, self.left_limit,
                               self.right_limit)
        while not single.is_at_home():
            single.move()
        return single.get_steps()


if __name__ == '__main__':
    """
    The main section of the script shall simulate
    -  20 walks from start 0 to home 20 for each of the following left
        boundaries: 0, -10, -100, -1000, -10000. The right boundary
        shall be 20 in all cases.
    -  Print results as left boundary followed by a list of the 20 walk
        durations for that left boundary.
    """
    _start = [0, 0, 0, 0, 0]
    _home = [20, 20, 20, 20, 20]
    _seed = [11, 22, 33, 44, 55]
    _left_limit = [0, -10, -100, -1000, -10000]
    _right_limit = [20, 20, 20, 20, 20]
    for x in range(len(_start)):
        w = BoundedSimulation(_start[x], _home[x], _seed[x],
                              _left_limit[x], _right_limit[x])
        print(w.run_simulation(20))
