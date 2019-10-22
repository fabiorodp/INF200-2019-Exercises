# -*- coding: utf-8 -*-
import random as rd
import numpy as np


__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    player = create_players(num_players)
    has_won = False
    winner_moves = 0
    # Initiate a game
    while not has_won:
        # Initiate a round of the game
        for p in range(num_players):
            player[p][0] += rd.randint(1, 6)
            player[p][1] += 1
            # checks if the players are at a ladder
            if player[p][0] in chutes_and_ladders():
                player[p][0] = chutes_and_ladders()[player[p][0]]
                player[p][1] += 1
            # checks if some player passed the 90th square
            elif player[p][0] > 90:
                winner_moves = player[p][1]
                has_won = True
                break
    return winner_moves


def chutes_and_ladders():
    """
    Dictionary with the snakes and ladders
    :return: The square where the player goes once at the snake or ladder
    """
    return {
        1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
        24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70
    }


def create_players(num_players):
    """
    Function to create a list with score and moves of each player
    :param num_players: Number of players in the game
    :return: score and moves of each player
    """
    return [[0, 0] for _ in range(num_players)]


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :return: sequence with number of moves needed in each game
    """
    return [single_game(num_players) for _ in range(num_games)]


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :param seed: random number seed for experiment
    :return: sequence with number of moves needed in each game
    """
    rd.seed(seed)
    return multiple_games(num_games, num_players)


if __name__ == '__main__':
    games_num = 100
    players_num = 4
    arbitrary_seed = 123456
    result = multi_game_experiment(games_num, players_num,
                                   arbitrary_seed)

    print('Shortest game: {:3d}'.format(min(result)))
    print('Longest game: {:3d}'.format(max(result)))
    print('Median game: {:5.2f}'.format(np.median(result)))
    print('Mean of game: {:5.2f}'.format(np.mean(result)))
    print('Standard deviation of game: {:5.2f}'.format(np.std(
        result)))
