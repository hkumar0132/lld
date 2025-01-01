from typing import List
from ConfigurationMemento import ConfigurationMemento

class Caretaker:

    def __init__(self) -> None:
        self.mementos : List[ConfigurationMemento] = []

    def add_memento(self, memento: ConfigurationMemento):
        self.mementos.append(memento)

    def undo(self) -> ConfigurationMemento:
        if (len(self.mementos) > 1):
            self.mementos.pop()
            return self.mementos[-1]