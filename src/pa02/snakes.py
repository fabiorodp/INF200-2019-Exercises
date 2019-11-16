# -*- coding: utf-8 -*-
import random as rd

__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


class Board:
    def __init__(self):
        self.goal = 90
        self.snakes_ladders = {
            1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
            24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def goal_reached(self, position):
        """return true if it is passed a position at or beyond the
        goal"""
        return True if position >= self.goal else False

    def position_adjustment(self, position):
        """returns the number of positions the player must move forward
        (in case of a ladder) or backward (chute), to get to the correct
        position. If the player is not at the start of a chute or ladder,
        the method returns 0"""
        return self.snakes_ladders[position] - position \
            if position in self.snakes_ladders else 0


class Player:
    """its subclasses manage information about player position,
    including information on which board a player lives"""

    def __init__(self):
        self.board = Board()
        self.position = 0

    def move(self):
        """It implements a die cast, the following move and,
        if necessary, a move up a ladder or down a chute.
        It does not return anything"""
        self.position += rd.randint(1, 6)
        # print(self.position)
        self.position += self.board.position_adjustment(self.position)
        # print(self.position)
        if self.board.goal_reached(self.position):
            # print(self.position)
            raise RuntimeError('Player won the game')


class ResilientPlayer(Player):
    """When a resilient player slips down a chute, he will take extra
    steps in the next move, in addition to the roll of the die. The
    number of extra steps is provided as an argument to the constructor,
    default is 1. Extra steps are taken immediately after the steps
    prescribed by the die and before snakes and ladders are checked"""

    def __init__(self):
        super().__init__()
        self.extra_steps = 1


class LazyPlayer(Player):
    """After climbing a ladder, a lazy player drops a given number of
    steps. The number of dropped steps is an optional argument to the
    constructor, default is 1. The player never moves backward: if, e.g.,
    the die cast results in 1 step and the player is to drop 3 steps,
    the player does not move -2 steps but just stays in place"""

    def __init__(self):
        super().__init__()
        self.dropped_steps = 1


if __name__ == '__main__':
    p1 = Player()
    while True:
        p1.move()
        # print('moved')
