"""Tests for the Defector strategy."""

import axelrod
from .test_player import TestPlayer

C, D = axelrod.Actions.C, axelrod.Actions.D


class TestDefector(TestPlayer):

    name = "Defector"
    player = axelrod.Defector
    expected_classifier = {
        'memory_depth': 0,
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_state': False,
        'manipulates_source': False
    }

    def test_strategy(self):
        # Test that always defects.
        self.first_play_test(D)
        self.second_play_test(D, D, D, D)


class TestTrickyDefector(TestPlayer):

    name = "Tricky Defector"
    player = axelrod.TrickyDefector
    expected_classifier = {
        'memory_depth': float('inf'),  # Long memory
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        # Starts by defecting.
        self.first_play_test(D)
        self.second_play_test(D, D, D, D)

    def test_cooperates_if_opponent_history_has_C_and_last_three_are_D(self):
        opponent_actions = [D, C, D, D, D] + [D, D]
        actions = [(D, D), (D, C), (D, D), (D, D), (D, D)] + [(C, D), (C, D)]
        self.versus_test(axelrod.MockPlayer(opponent_actions), actions)

    def test_defects_if_opponent_never_cooperated(self):
        opponent_actions = [D, D, D, D, D] + [D, D]
        actions = [(D, D), (D, D), (D, D), (D, D), (D, D)] + [(D, D), (D, D)]
        self.versus_test(axelrod.MockPlayer(opponent_actions), actions)

    def test_defects_if_opponent_last_three_are_not_D(self):
        opponent_actions = [D, C, D, D, D] + [C, D]
        actions = [(D, D), (D, C), (D, D), (D, D), (D, D)] + [(C, C), (D, D)]
        self.versus_test(axelrod.MockPlayer(opponent_actions), actions)
