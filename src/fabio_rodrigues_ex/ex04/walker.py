# -*- coding: utf-8 -*-

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class Walker:
    def __init__(self, initial, home):
        self.x = [initial]
        self.home = home
        self.steps = 0

    def move(self):
        """take one step"""
        self.x.append(self.x[self.steps] + 1)
        self.steps += 1

    def is_at_home(self):
        """to check whether the student is at home"""
        if self.x[self.steps] == self.home:
            return True
        return False

    def get_position(self):
        """to access the students current position"""
        return self.x[self.steps]

    def get_steps(self):
        """to access the number of steps the student has taken in
        total"""
        return self.steps

    def walking_process(self):
        pass





