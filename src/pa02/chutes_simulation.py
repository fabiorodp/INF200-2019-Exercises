# -*- coding: utf-8 -*-

__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


class Simulation:
    def __init__(self):
        pass

    def single_game(self):
        pass

    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winner_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass


if __name__ == '__main__':
    sim = Simulation([Player, Player, ResilientPlayer, ResilientPlayer,
                      ResilientPlayer, LazyPlayer],
                     randomize_players=True)
