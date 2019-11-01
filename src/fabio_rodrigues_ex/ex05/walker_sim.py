# -*- coding: utf-8 -*-
from random import randint

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class Walker:
    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker's home
        """
        self.x = [start]
        self.home = home
        self.steps = 0

    def move(self):
        """Change coordinate by +1 or -1 with equal probability."""
        if randint(1, 2) == 1:
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

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of
        steps.

        Returns
        -------
        int
            The number of steps taken
        """

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
