class bowlinggame():
    def __init__(self):
        self.rolls = []
        self.score = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def roll_score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.strike(roll_index):
                score += 10 + self.rolls[roll_index+1] + self.rolls[roll_index+2]
                roll_index += 1
            elif self.spare(roll_index):
                score += 10 + self.rolls[roll_index+2]
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index+1]
                roll_index += 2
        return score

    def spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1] == 10 

    def strike(self, roll_index):
        return self.rolls[roll_index] == 10
