# -*- coding: utf-8 -*-
import random as rd

__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


class Board:
    LADDERS = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
               (65, 82), (68, 85)]
    CHUTES = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
              (74, 12), (87, 70)]

    def __init__(self, ladders=None, chutes=None, goal=90):
        if chutes or ladders is None:
            chutes, ladders = self.CHUTES, self.LADDERS

        self.goal = goal
        self.chutes_ladders = {start: end for start, end in
                               ladders + chutes}

    def goal_reached(self, position):
        """return true if it is passed a position at or beyond the
        goal"""
        return position >= self.goal

    def position_adjustment(self, position):
        """returns the number of positions the player must move forward
        (in case of a ladder) or backward (chute), to get to the correct
        position. If the player is not at the start of a chute or ladder,
        the method returns 0"""
        return self.chutes_ladders[position] - position \
            if position in self.chutes_ladders else 0


class Player:
    """its subclasses manage information about player position,
    including information on which board a player lives"""

    def __init__(self, board):
        self.board, self.position, self.num_moves = board, 0, 0

    def move(self):
        """It implements a die cast, the following move and,
        if necessary, a move up a ladder or down a chute.
        It does not return anything"""
        # New position: Add die
        self.position += rd.randint(1, 6)

        # Add chute and ladder
        self.position += self.board.position_adjustment(self.position)

        # Add move count
        self.num_moves += 1


class ResilientPlayer(Player):
    """When a resilient player slips down a chute, he will take extra
    steps in the next move, in addition to the roll of the die. The
    number of extra steps is provided as an argument to the constructor,
    default is 1. Extra steps are taken immediately after the steps
    prescribed by the die and before snakes and ladders are checked"""

    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps, self.slided = extra_steps, False

    def move(self):
        # Check if slided is true and get the extra steps
        num_extra = self.extra_steps if self.slided else 0

        # New position: Add die + extra steps (if applicable)
        self.position += rd.randint(1, 6) + num_extra

        # Save the position
        saved_pos = self.position

        # Add chute and ladder
        self.position += self.board.position_adjustment(self.position)

        # self.slided for next round: True if got the chute, else False
        self.slided = True if saved_pos > self.position else False

        # add move count
        self.num_moves += 1


class LazyPlayer(Player):
    """After climbing a ladder, a lazy player drops a given number of
    steps. The number of dropped steps is an optional argument to the
    constructor, default is 1. The player never moves backward: if, e.g.,
    the die cast results in 1 step and the player is to drop 3 steps,
    the player does not move -2 steps but just stays in place"""

    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps, self.climbed = dropped_steps, False

    def move(self):
        # Check if climbed is true and get the dropped steps
        num_dropped = self.dropped_steps if self.climbed else 0

        # New position: Add die + drop steps (if applicable)
        self.position += max(0, rd.randint(1, 6) - num_dropped)

        # Save the position
        saved_pos = self.position

        # Add chute and ladder
        self.position += self.board.position_adjustment(self.position)

        # self.climbed for next round: True if got the snake, else False
        self.climbed = True if saved_pos < self.position else False

        # add move count
        self.num_moves += 1
