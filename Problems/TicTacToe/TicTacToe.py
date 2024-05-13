from models.Board import Board
from models.PieceType import PieceType
from models.Player import Player
from models.PlayingPiece import PlayingPiece


class TicTacToe:
    def __init__(self):
        self.initialize_game()
    
    def initialize_game(self):
        self.board = Board()
        self.player1 = Player(PlayingPiece(PieceType.PieceTypeX))
        self.player2 = Player(PlayingPiece(PieceType.PieceTypeY))
        
    def start_game(self):
        no_winner = True
        player_turn = True
        while no_winner and len(self.board.get_free_cells()) > 0:
            print(f'Player {1 if player_turn else 2}\'s turn: \n\n')
            self.board.print_board()
            player_input = input().split(',')
            row = int(player_input[0])
            col = int(player_input[1])
            
            if not self.board.add_piece(row, col, self.player1.playing_piece if player_turn else self.player2.playing_piece):
                print("\n\ninvalid input")
                continue
            
            # self.board.print_board()
            
            if self.board.check_if_winner():
                print(f'Player {1 if player_turn else 2} is winner')
                no_winner = False
            else:
                player_turn = not player_turn
        if no_winner:
            print('TIE')