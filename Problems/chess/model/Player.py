from abc import ABC, abstractclassmethod

class Player(ABC):
    def __init__(self, color):
        self.color = color