from models.PlayingPieceEmpty import PlayingPieceEmpty

class Board:
    def __init__(self):
        self.size = 3
        self.board = []
        self.playing_piece_empty = PlayingPieceEmpty()
        for i in range(0, self.size):
            row = []
            for j in range(0, self.size):
                row.append(self.playing_piece_empty)
            self.board.append(row)
            
    def get_free_cells(self):
        free_cells = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] == self.playing_piece_empty:
                    free_cells.append([i,j])
        return free_cells
    
    def print_board(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
               print('_' if self.board[i][j] == self.playing_piece_empty else self.board[i][j].piece_type, end=", ")
            print()
        print('\n\n')
    
    def add_piece(self, i, j, playing_piece):
        if self.board[i][j] == self.playing_piece_empty:
            self.board[i][j] = playing_piece
            return True
        
        return False
    
    def _check_if_row_contains_same_piece_type(self, row):
        for j in range(1, self.size):
            if self.board[row][j].piece_type != self.board[row][j-1].piece_type or self.board[row][j] == self.playing_piece_empty:
                return False
        return True
            
    def _check_if_col_contains_same_piece_type(self, col):
        for j in range(1, self.size):
            if self.board[j][col].piece_type != self.board[j-1][col].piece_type or self.board[j][col] == self.playing_piece_empty:
                return False
        return True
    

    # [(0,0),(0,1),(0,2),
    #  (1,0),(1,1),(1,0),
    #  (2,0),(2,1),(2,2),
    # ]

    def _check_if_diagonals_contains_same_piece_type(self):
        diagonal1 = True
        for j in range(1, self.size):
            # print(f"DIAGONAL {j} : {self.board[j][j].piece_type} and {self.board[j-1][j-1].piece_type}")
            if self.board[j][j].piece_type != self.board[j-1][j-1].piece_type or self.board[j][j] == self.playing_piece_empty:
                diagonal1 = False 
                break
        if diagonal1:
            return True
        r = 1
        c = 1
        for j in range(1, self.size):
            # print(f"DIAGONAL {r},{c} : {self.board[r][c].piece_type} and {self.board[r-1][c+1].piece_type}")
            if self.board[r][c].piece_type != self.board[r-1][c+1].piece_type or self.board[r][c] == self.playing_piece_empty:
                return False
            r += 1
            c -= 1
        return True
        
    def check_if_winner(self):
        
        if self._check_if_diagonals_contains_same_piece_type():
            return True
        for i in range(0, self.size):
            if (
                self._check_if_row_contains_same_piece_type(i) or
                self._check_if_col_contains_same_piece_type(i)
            ):
                return True
        return False
        