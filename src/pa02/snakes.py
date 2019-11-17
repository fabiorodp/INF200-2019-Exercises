# -*- coding: utf-8 -*-
import random as rd

__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


class Board:
    LADDERS = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
               (65, 82), (68, 85)]
    CHUTES = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
              (74, 12), (87, 70)]

    def __init__(self, ladders=LADDERS, chutes=CHUTES, goal=90):
        self.goal = goal
        self.chutes_ladders = {ladder[0]: ladder[1] for ladder in
                               ladders}
        self.chutes_ladders.update(
            {chute[0]: chute[1] for chute in chutes})

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
        self.board = board
        self.position = 0
        self.num_moves = 0

    def move(self):
        """It implements a die cast, the following move and,
        if necessary, a move up a ladder or down a chute.
        It does not return anything"""
        self.position += rd.randint(1, 6)
        # print(self.position)
        self.position += self.board.position_adjustment(self.position)
        self.num_moves += 1
        # print(self.position)
        #if self.board.goal_reached(self.position):
            # print(self.position)
         #   raise RuntimeError('Player won the game')


class ResilientPlayer(Player):
    """When a resilient player slips down a chute, he will take extra
    steps in the next move, in addition to the roll of the die. The
    number of extra steps is provided as an argument to the constructor,
    default is 1. Extra steps are taken immediately after the steps
    prescribed by the die and before snakes and ladders are checked"""

    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.extra_after_sliding = False

    def move(self):
        prev_pos = self.position
        steps = self.extra_steps if self.extra_after_sliding else 0
        new_pos = self.position + rd.randint(1, 6) + steps
        self.position = self.board.position_adjustment(new_pos)
        if prev_pos < self.position:
            self.extra_after_sliding = False
        self.num_moves += 1


class LazyPlayer(Player):
    """After climbing a ladder, a lazy player drops a given number of
    steps. The number of dropped steps is an optional argument to the
    constructor, default is 1. The player never moves backward: if, e.g.,
    the die cast results in 1 step and the player is to drop 3 steps,
    the player does not move -2 steps but just stays in place"""

    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        self.drops_after_climbing = False

    def move(self):
        prev_pos = self.position
        dropped = self.dropped_steps if self.drops_after_climbing else 0
        new_dropped_pos = self.position + max(0, rd.randint(1,
                                                            6) - dropped)
        self.position = self.board.position_adjustment(new_dropped_pos)
        if prev_pos < self.position:
            self.drops_after_climbing = False
        self.num_moves += 1


class Simulation:

    def __init__(self, player_field, board=None, seed=123456,
                 randomize_players=False):
        if randomize_players:
            rd.shuffle(player_field)
        self.board = board if board else Board()
        self.player_field = player_field
        self.player_types = frozenset(
            pc.__name__ for pc in player_field)
        self.results = []

    def single_game(self):
        moves = 0
        players = [player(self.board) for player in self.player_field]
        while True:
            moves += 1
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.num_moves, type(player)
        return moves

    def run_simulation(self, num_games):
        self.results = [self.single_game() for _ in range(num_games)]
        return self.results

    def get_results(self):
        return self.results

    def players_per_type(self):
        """
        Returns a dict mapping player classes to number of players.
        """

        return {player_type.__name__:
                    self.player_field.count(player_type)
                for player_type in frozenset(self.player_field)}

    def winners_per_type(self):
        """
        Returns dict showing number of winners for each type of player.
        """

        winner_types = list(zip(*self.results))[1]
        return {player_type: winner_types.count(player_type)
                for player_type in self.player_types}

    def durations_per_type(self):
        """
        Returns dict mapping winner type to list of game durations for type.
        """

        return {player_type: [d for d, t in self.results if t == player_type]
                for player_type in self.player_types}




#if __name__ == '__main__':
 #   p1 = Player()
  #  while True:
  #      p1.move()
        # print('moved')
