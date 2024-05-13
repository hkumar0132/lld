from random import randint

class Dice:
    def __init__(self):
        self.min_dice_limit = 1
        self.max_dice_limit = 6
    
    def roll(self):
        return randint(self.min_dice_limit, self.max_dice_limit)