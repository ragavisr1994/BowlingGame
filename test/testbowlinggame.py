import unittest
from game.bowlinggame import bowlinggame

class testbowlinggame(unittest.TestCase):
    
    def setUp(self):
        self.game = bowlinggame()

    def test_scorezero(self):
        self.assertEqual(self.game.score ,0)
        print(str(self.game.score))

    """ def test_recordrollingofball(self):
        self.game.roll(8)
        self.assertEquals(self.game.total_score, 8)
        print(str(self.game.score)) """

    def test_allgutters(self):
        self._roll_many(0, 20)
        self.assertEquals(0, self.game.roll_score())
        print(str(self.game.score))

    def _roll_many(self, pins, num):
        for a in range(num):
            self.game.roll(pins)
