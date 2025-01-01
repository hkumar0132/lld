from typing import List

from models import IPiece, PieceType
from .PieceFactory import PieceFactory

class Board:

    def __init__(self, size: int) -> None:
        self.cells: List[List[IPiece]] = []
        self.size = size
        self.piece_factory = PieceFactory()
        self.__initialize_board()

    def __initialize_board(self):
        for _ in range(self.size):
            current_row = []
            for _ in range(self.size):
                current_row.append(self.piece_factory.get_piece(PieceType.EMPTY))
            self.cells.append(current_row)

    def get_object_at_cell(self, row, col) -> IPiece:
        return self.cells[row][col]
    
    def occupy_cell(self, position, piece_type: PieceType):
        row, col = position
        self.cells[row][col] = self.piece_factory.get_piece(piece_type)

    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.cells[row][col].get_piece_type().value, end=" | ")
            print()

    
    def get_free_cells(self):
        free_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col].get_piece_type() == PieceType.EMPTY:
                    free_cells.append([row, col])
        return free_cells