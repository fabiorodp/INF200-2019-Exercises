# -*- coding: utf-8 -*-
import chutes_simulation as cs

__author__ = "Fábio Rodrigues Pereira and Rabin Senchuri"
__email__ = "faro@nmbu.no and rase@nmbu.no"


class TestResilientPlayer:
    def test_resilient_player_got_chute(self):
        """We test here if the chute and slided in
        ResilientPlayer(Board()) are functioning"""
        chute = [5, 3, 30, 37, 27, 12, 70]
        got_chute, game_ended, position, slided = False, False, 0, False
        while not got_chute:
            p = cs.ResilientPlayer(cs.Board())
            while not game_ended:
                if position in chute and slided:
                    got_chute, game_ended = True, True
                else:
                    p.move()
                    position, slided = p.position, p.slided
                    game_ended = p.board.goal_reached(position)
            game_ended = False if not got_chute else True
        assert position in chute
        assert slided
