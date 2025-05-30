class PieceType(Enum):
    BLACK='BLACK'
    WHITE='WHITE'
    EMPTY='EMPTY'

class Move:
    def __init__(self, piece: Piece, dest_row, dest_col):
        self.piece = piece
        self.dest_row = dest_row
        self.dest_col = dest_col

from abc import ABC, abstractmethod
class Piece(ABC):

    def __init__(self, row, col, piece_type: PieceType):
        self.row = row
        self.col = col
        self.piece_type = piece_type

    @abstractmethod
    def can_move(move: Move):
        pass

class Bishop(Piece):

    def __init__(self, piece_type: PieceType):
        super().__init__(piece_type)

    def can_move(move: Move):
        return abs(move.source_col - move.dest_col) == abs(move.source_row - move.dest_row)
    
class King(Piece):
    def can_move(move: Move):
        diff_col = abs(move.source_col - move.dest_col)
        diff_row = abs(move.source_row - move.dest_row)
        return diff_col == 1 or diff_row == 1 or diff_col + diff_row == 1 

class Knight(Piece):
    def can_move(move: Move):
        diff_col = abs(move.source_col - move.dest_col)
        diff_row = abs(move.source_row - move.dest_row)
        return (diff_col == 1 and diff_row == 2) or (diff_col == 2 and diff_row == 1)

class Rook(Piece):
    def can_move(move: Move):
        diff_col = abs(move.source_col - move.dest_col)
        diff_row = abs(move.source_row - move.dest_row)
        return diff_col == 0 or diff_row == 0   
    
class Queen(Piece):
    def can_move(move: Move):
        diff_col = abs(move.source_col - move.dest_col)
        diff_row = abs(move.source_row - move.dest_row)
        return diff_col == diff_row or (diff_col == 1 and diff_row == 2) or (diff_col == 2 and diff_row == 1)
    
class Pawn(Piece):
    def can_move(self, move: Move):
        diff_col = abs(move.source_col - move.dest_col)
        diff_row = move.dest_row - move.source_row

        if diff_col > 0:
            return False
        
        if self.piece_type == PieceType.WHITE:
            if self.row == 1:
                return diff_row == 2 or diff_row == 1
            else:
                return diff_row == 1
        else:
            if self.row == 6:
                return diff_row == -2 or diff_row == -1
            else:
                return diff_row == -1

import uuid
class Player:
    def __init__(self, name, piece_type: PieceType):
        self.id = uuid.uuid4()

    def make_move(self, move: Move, board: Board):
        piece = move.piece

        piece.row = move.dest_row
        piece.col = move.dest_col

        board.set_piece(move.source_row, move.source_col, None)
        board.set_piece(move.dest_row, move.dest_col, move.piece)


class Board:
    def __init__(self):
        self.cell = [

        ]

        for i in range(8):
            rows = []
            for j in range(8):
                rows.append(PieceType.EMPTY)
            self.cell.append(rows)

    def is_valid_move(self, player: Player, move: Move):
        if not move.piece.can_move():
            raise Exception("")
        
        return move.dest_row >= 0 and move.dest_col >= 0 and move.dest_row <= 8 and move.dest_row <= 8

    def set_piece(self, row, col, piece):
        self.cell[row][col] = piece

    def is_checkmate(self):
        pass

    def is_stalemate(self):
        pass


class Game:

    def __init__(self):
        self.board = Board()
        self.players = []

    def __get_player_move(player: Player):
        pass

    def start_game(self):
        # console input

        is_checkmate = False
        is_stalemate = False
        white_turn = True

        while(True):
            for player in self.players:
                
                is_checkmate = self.board.is_checkmate()
                is_stalemate = self.board.is_stalemate()

                if is_checkmate or is_stalemate:
                    print("Game over")
                    break

                move = self.__get_player_move(player)
                if self.board.is_valid_move(move):
                    player.make_move(move)

                white_turn = not white_turn            
    