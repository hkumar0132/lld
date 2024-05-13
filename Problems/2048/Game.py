from Board import Board
from random import randint
from DirectionFactory import DirectionFactory
from Directions import Directions
from config import POSSIBLE_USER_INPUT


class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self._initialize_game()
        
    def _get_random_value(self, max_value):
        return randint(0, max_value)
    
    def _add_random_value_to_board(self):
        empty_cells = self.board.get_empty_cells()
        idx = self._get_random_value(len(empty_cells)-1)
        [row, col] = empty_cells[idx]
        # print(f'ADDING VALUE TO {row} {col}')
        self.board.add_random_tile(row, col)
            
    def _initialize_game(self):
        for i in range(0, 2):
            self._add_random_value_to_board()
        self.board.print_board()
        
    def start_game(self):
        i = None
        while True:
            
            print('\nMake a move, possible values are 0: LEFT, 1: RIGHT, 2: TOP, 3: BOTTOM\n')
            
            i = int(input())
            direction = DirectionFactory().get_direction(direction=i)
            if i not in POSSIBLE_USER_INPUT:
                print('\nInvalid Move')
                continue
                
            if direction == Directions.LEFT:
                if not self.board.slide_left():
                    self.board.print_board()
                    continue
            elif direction == Directions.RIGHT:
                if not self.board.slide_right():
                    self.board.print_board()
                    continue
            elif direction == Directions.TOP:
                if not self.board.slide_top():
                    self.board.print_board()
                    continue
            elif direction == Directions.BOTTOM:
                if not self.board.slide_bottom():
                    self.board.print_board()
                    continue
                
            if self.board.check_if_game_won():
                print("\nCongratulations")
                break

            self._add_random_value_to_board()
            self.board.print_board()
            
            if len(self.board.get_empty_cells()) == 0:
                print('\nGame Over')
                break
