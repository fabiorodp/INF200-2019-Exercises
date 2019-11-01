# -*- coding: utf-8 -*-
from walker_sim.py import Walker, Simulation

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


def main_simulations():
    """
    The main section of the script shall simulate
    -  20 walks from start 0 to home 20 for each of the following left
        boundaries: 0, -10, -100, -1000, -10000. The right boundary
        shall be 20 in all cases.
    -  Print results as left boundary followed by a list of the 20 walk
        durations for that left boundary.
    """
    pass


if __name__ == '__main__':
    main_simulations()
