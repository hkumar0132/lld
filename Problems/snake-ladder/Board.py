from typing import List

from models import IBoard, IBoardEntity
from Snake import Snake
from Ladder import Ladder
from Cell import Cell

class Board(IBoard):

    def __init__(self):
        self.cell = []

    def initialize_board(self, N, entities: List[IBoardEntity]):
        for row in range(N):
            current_col = []
            for col in range(N):
                cell = Cell(row, col)
                current_col.append(cell)
            self.cell.append(current_col)

        self.__set_entities(entities)

    def __set_entities(self, entities: List[IBoardEntity]):
        for entity in entities:
            row, col = entity.get_head()
            self.cell[row][col] = entity

    def get_object_at_cell(self, position: List[int]) -> IBoardEntity:
        row, col = position
        return self.cell[row][col]