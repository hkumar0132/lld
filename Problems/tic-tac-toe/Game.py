from typing import List
from random import randint
from collections import defaultdict

from models.impl import Board
from models import IPlayer, PieceType

class Game:

    def initialize_game(self, matrix_size: int, players: List[IPlayer]):
        self.matrix_size = matrix_size
        self.board : Board = Board(matrix_size)
        self.players = players

    # TODO - pass row, col to this function and only check row, col and diagnoals passing through it
    # This can be done in O(1) -> using hashmap
    def __is_winner(self):

        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        diag_dict = defaultdict(set)

        for row in range(self.matrix_size):
            for col in range(self.matrix_size):
                piece = self.board.get_object_at_cell(row, col).get_piece_type()
                row_dict[row].add(piece)
                col_dict[col].add(piece)

                if row == col:
                    diag_dict[row - col].add(piece)
                elif row + col == self.matrix_size - 1:
                    diag_dict[row + col].add(piece)
        
        for value in row_dict.values():
            if len(value) == 1 and value.pop() != PieceType.EMPTY:
                return True

        for value in col_dict.values():
            if len(value) == 1 and value.pop() != PieceType.EMPTY:
                return True
            
        for value in diag_dict.values():
            if len(value) == 1 and value.pop() != PieceType.EMPTY:
                return True
        
        return False

    def start_game(self):

        game_over = False
        while not game_over:
            for player in self.players:
                print(f"Player {player.get_player_name()} turn")
                free_cells = self.board.get_free_cells()
                if (len(free_cells)) == 0:
                    print("Game tied")
                    game_over = True
                    break

                random_index = randint(0, len(free_cells) - 1)
                print(free_cells[random_index])
                current_cell = free_cells[random_index]
                self.board.occupy_cell(current_cell, player.get_piece_type())

                self.board.print_board()
                
                if (self.__is_winner()):
                    print(f"Player {player.get_player_name()} has won")
                    game_over = True
                    break             