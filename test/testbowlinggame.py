import unittest
from game.bowlinggame import bowlinggame

class testbowlinggame(unittest.TestCase):
    
    def setUp(self):
        self.game = bowlinggame()

    def test_scorezero(self):
        self.assertEqual(self.game.score ,0)
        print(str(self.game.score))

    def test_allgutters(self):
        self.roll_many(0, 20)
        self.assertEquals(0, self.game.roll_score())
        print(str(self.game.score))
  
    def test_allones(self):
        self.roll_many(1, 20)
        self.assertEquals(20, self.game.roll_score())
        print(str(self.game.score))

    def test_onesparewiththreerolls(self):
        self.roll_spare()
        self.game.roll(5)
        self.roll_many(0, 17)
        self.assertEqual(20, self.game.roll_score())

    def roll_many(self, pins, num):
        for a in range(num):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)
