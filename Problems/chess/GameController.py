from classes.Bishop import Bishop
from classes.BlackPlayer import BlackPlayer
from classes.Board import Board
from classes.King import King
from classes.Knight import Knight
from classes.Pawn import Pawn
from classes.Queen import Queen
from classes.Rook import Rook
from classes.WhitePlayer import WhitePlayer


class GameController:
    def __init__(self, board_size):
        self.board_size = board_size
        self.white_pieces = []
        self.black_pieces = []
        self.initialize_game()
        
    def _create_pieces(self, color, piece_name, class_name, i, j):
        piece = class_name(piece_name, color)
        self.board.set_player_position(piece, i, j)
        
    def initialize_game(self):
        self.white_player = WhitePlayer()
        self.black_player = BlackPlayer()
        self.board = Board(self.board_size, self.white_player, self.black_player)
        
        for i in range(0, 8):
            self._create_pieces('white', 'WP', Pawn, 6, i)
            self._create_pieces('black', 'BP', Pawn, 1, i)
        
        self._create_pieces('white', 'WR', Rook, 7, 0)
        self._create_pieces('white', 'WR', Rook, 7, 7)
        
        self._create_pieces('black', 'BR', Rook, 0, 0)
        self._create_pieces('black', 'BR', Rook, 0, 7)
        
        self._create_pieces('white', 'WN', Knight, 7, 1)
        self._create_pieces('white', 'WN', Knight, 7, 6)
        
        self._create_pieces('black', 'BN', Knight, 0, 1)
        self._create_pieces('black', 'BN', Knight, 0, 6)
        
        self._create_pieces('white', 'WB', Bishop, 7, 2)
        self._create_pieces('white', 'WB', Bishop, 7, 5)
        
        self._create_pieces('black', 'BB', Bishop, 0, 2)
        self._create_pieces('black', 'BB', Bishop, 0, 5)
        
        self._create_pieces('white', 'WK', King, 7, 4)
        self._create_pieces('white', 'WQ', Queen, 7, 3)
        
        self._create_pieces('black', 'BK', King, 0, 4)
        self._create_pieces('black', 'BQ', Queen, 0, 3)
        
    def start_game(self):
        print('Waiting for command...')
        white_player_turn = True
        while True:
            self.board.print_board()
            i = input()
            if i == 'exit':
                break
            
            start_position = i[0]
            end_position = i[1]
            
            start_row = ord(start_position[0]) - ord('a')
            start_col = int(start_position[1]) - 1
            
            end_row = ord(end_position[0]) - ord('a')
            end_col = int(end_position[1]) - 1
            
            if start_row < 0 or start_row > self.board_size or end_row < 0 or end_row > self.board_size
                print('\nInvalid Move')
                continue
            
            start_piece = self.board.get_piece_at_position(start_row, start_col)
            if not start_piece:
                print('\nInvalid Move')
                continue
            
            if (white_player_turn and start_piece.get_color() == 'black') or (start_piece.get_color() == 'white' and not white_player_turn):
                print('\nInvalid Move')
                continue
                
            end_piece = self.board.get_piece_at_position(end_row, end_col)
            if end_piece and ((white_player_turn and end_piece.get_color() == 'white') or (end_piece.get_color() == 'black' and not white_player_turn)):
                print('\nInvalid Move')
                continue
            
            if not self.board.move_piece(start_piece, start_row, start_col, end_row, end_col, 'white' if white_player_turn else 'black'):
                print('\nInvalid move')
                continue
                

            white_player_turn = not white_player_turn