class Board:
    def __init__(self, board_size, white_player, black_player):
        self.board_size = board_size
        self.white_player = white_player
        self.black_player = black_player
        self.board = []
        self.initialize_board()
        
    def initialize_board(self):
        for i in range(0, self.board_size):
            row = []
            for j in range(0, self.board_size):
                row.append(None)
            self.board.append(row)
        
    def set_player_position(self, piece, row, col):
        self.board[row][col] = piece
        
    def kill_piece_at_position(self, row, col):
        self.board[row][col] = None
        
    def print_board(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                print('--' if self.board[i][j] == None else self.board[i][j].get_name(), end=" ")
                
            print()
                
    def get_piece_at_position(self, row, col):
        return self.board[row][col]
    
    def move_piece(self, start_row, start_col, end_row, end_col, color):
        
        # ROOK
        start_piece = self.get_piece_at_position(start_row, start_col)
        if not start_piece.is_valid_move():
            return False
            
        if start_piece.get_name().includes('R'):
            if start_row == end_row:
                for col in range(start_row+1, end_row):
                    if self.get_piece_at_position(start_row, col) != None:
                        return False
                    
            if start_col == end_col:
                for row in range(start_col+1, end_col):
                    if self.get_piece_at_position(row, start_col)!= None:
                        return False
        # KNIGHT
        if start_piece.get_name().includes('N'):
            pass
        
        #PAWN
        if start_piece.get_name().includes('P'):
            pass
        
        # BISHOP
        if start_piece.get_name().includes('B'):
            pass
        
        # QUEEN
        if start_piece.get_name().includes('B'):
            pass
            
        # KING
        if start_piece.get_name().includes('K'):
            pass
            
        end_piece = self.get_piece_at_position(end_row, end_col)
        if end_piece != None:
            if end_piece.get_color() == color:
                return False
            self.kill_piece_at_position(end_row, end_col)
                
            
            