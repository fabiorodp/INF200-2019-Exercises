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
        return position - self.snakes_ladders[position] \
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
        if self.board.goal_reached(self.position):
            raise StopIteration
        elif self.position in self.board.snakes_ladders:
            self.position += self.board.position_adjustment(
                self.position)


class ResilientPlayer(Player):
    def __init__(self):
        super().__init__()
        self.extra_steps = 1


class LazyPlayer(Player):
    def __init__(self):
        super().__init__()
        self.dropped_steps = 1


if __name__ == '__main__':
    p1 = Player()
    p1.move()
    print(p1.position)
