# -*- coding: utf-8 -*-
from random import randint

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class Walker:
    def __init__(self, initial, home):
        self.x = [initial]
        self.home = home
        self.steps = 0

    def move(self):
        """take one step"""
        if randint(1, 2) == 1:
            self.x.append(self.x[self.steps] + 1)
        else:
            self.x.append(self.x[self.steps] - 1)
        self.steps += 1

    def is_at_home(self):
        """to check whether the student is at home"""
        return self.x[self.steps] == self.home

    def get_position(self):
        """to access the students current position"""
        return self.x[self.steps]

    def get_steps(self):
        """to access the number of steps the student has taken in
        total"""
        return self.steps


def five_simulations(distance):
    """Function to create 5 simulations"""
    steps_home = []
    for _ in range(0, 5):
        w = Walker(0, distance)
        while not w.is_at_home():
            w.move()
        steps_home.append(w.get_steps())
    return steps_home


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50, 100]
    for i in distances:
        print('Distance: {} -> Path lengths: {}'.format(
            i, five_simulations(i)))
