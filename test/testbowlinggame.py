import unittest
from game.bowlinggame import bowlinggame

class testbowlinggame(unittest.TestCase):
    
    def setUp(self):
        self.game = bowlinggame()

    def test_ScoreZero(self):
        self.assertEqual(self.game.score, 0)
        print(str(self.game.score))

    def test_CanRecordRollingofBall(self):
        self.game.roll(1)
        self.assertEqual(self.game.rolls, [1])
        self.game.roll(2)
        self.assertEqual(self.game.rolls, [1, 2])
        print(str(self.game.score))

    def test_AllGutters(self):
        self.roll_many(0, 20)
        self.assertEquals(self.game.roll_score(), 0)
        print(str(self.game.score))
  
    def test_AllOnes(self):
        self.roll_many(1, 20)
        self.assertEquals(self.game.roll_score(), 20)
        print(str(self.game.score))

    def test_OneSparewithThreeRolls(self):
        self.roll_spare()
        self.game.roll(5)
        self.roll_many(0, 17)
        self.assertEqual(self.game.roll_score(), 20)

    def test_OneStrikewithTwoRolls(self):
        self.roll_strike()
        self.game.roll(5)
        self.game.roll(5)
        self.roll_many(0, 16)
        self.assertEqual(self.game.roll_score(), 30)

    def test_PerfectScoreGame(self):
        self.roll_many(10, 12)
        self.assertEquals(self.game.roll_score(), 300)


    def roll_many(self, pins, num):
        for a in range(num):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)
