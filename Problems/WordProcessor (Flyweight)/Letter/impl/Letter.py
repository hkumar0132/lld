from Letter import ILetter

class Letter(ILetter):

    def __init__(self, font_size: int, font_weight: int, character: str):
        self.font_size = font_size
        self.font_weight = font_weight
        self.character = character

    def display(self, row: int, col: int):
        print(row, col)