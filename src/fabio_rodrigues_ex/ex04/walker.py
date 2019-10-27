# -*- coding: utf-8 -*-
from random import randint

__author__ = 'Fábio Rodrigues Pereira'
__email__ = 'faro@nmbu.no'


class Walker:
    def __init__(self, initial, home):
        self.initial = initial
        self.home = home

    def move(self):
        """take one step"""
        pass

    def is_at_home(self):
        """to check whether the student is at home
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        """
        pass

    def get_position(self):
        """to access the students current position"""
        pass

    def get_steps(self):
        """to access the number of steps the student has taken in
        total"""
        pass

    pass
