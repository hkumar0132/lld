from collections import defaultdict
from Letter import ILetter
from Letter.impl import Letter

class LetterFactory:

    def __init__(self) -> None:
        self.cache : dict[str, ILetter] = defaultdict()

    def create_letter(self, character):
        if character in self.cache:
            print("hit")
            return self.cache[character]
        
        letter = Letter(12, 500, character)
        self.cache[character] = letter
        return letter