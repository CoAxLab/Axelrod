import unittest

from axelrod import all_strategies


class TestNames(unittest.TestCase):
    def test_all_strategies_have_names(self):
        names = [s.name for s in all_strategies if s.name]
        self.assertEqual(len(names), len(all_strategies))

    def test_all_names_are_unique(self):
        names = set(s.name for s in all_strategies)
        self.assertEqual(len(names), len(all_strategies))
