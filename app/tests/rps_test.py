import unittest
from app.models.rps import Player
from app.models.rps_choice import *

class TestChoice(unittest.TestCase):

    def setUp(self):
        self.rock = Player("Tim", "rock")
        self.paper = Player("Joe", "paper")
        self.scissors = Player("Phil", "scissors")
        
    def test_decide_rock_over_scissors(self):
        result = get_result(self.rock, self.scissors)
        self.assertEqual(self.rock, result)