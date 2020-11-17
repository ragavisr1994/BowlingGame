import unittest
from game.bowlinggame import bowlinggame

class testbowlinggame(unittest.TestCase):

    def setUp(self):
        self.game = bowlinggame()

    def test_scorezero(self):
        self.assertEqual(self.game.score ,0)
        print(str(self.game.score))
