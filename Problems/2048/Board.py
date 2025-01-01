from config import WIN_VALUE, INSERT_VALUE

class Board:
    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.initialize_board()
    
    def initialize_board(self):
        self.board = []
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size):
                temp.append(None)
            self.board.append(temp)
        # print('initialize board: ', self.board)
    
    def slide_left(self):
        movement = False
        # Shift 
        for i in range(0, self.board_size):
            new_list = []
            for j in range(0, self.board_size):
                if self.board[i][j] != None:
                    new_list.append(self.board[i][j])
            for j in range(self.board_size-len(new_list)):
                new_list.append(None)
            if self.board[i] != new_list:
                movement = True
                self.board[i] = new_list
        
        # Merge & Shift Once at max.
        for i in range(0, self.board_size):
            for j in range(0, self.board_size-1):
                if self.board[i][j] != None and self.board[i][j] == self.board[i][j+1]:
                    movement = True
                    self.board[i][j] *= 2
                    self.board[i][j+1] = None 
            for j in range(0, self.board_size-1):
                if self.board[i][j] == None and self.board[i][j+1] != None:
                    self.board[i][j], self.board[i][j+1] = self.board[i][j+1], None
        return movement
            
    def slide_right(self):
        movement = False
        # Shift 
        for i in range(0, self.board_size):
            new_list = []
            for j in range(0, self.board_size):
                if self.board[i][j] != None:
                    new_list.append(self.board[i][j])
            for j in range(self.board_size-len(new_list)):
                new_list = [None] + new_list
            if self.board[i] != new_list:
                movement = True
                self.board[i] = new_list
        
        # Merge & Shift Once at max.
        for i in range(0, self.board_size):
            for j in range(self.board_size-1, -1, -1):
                if self.board[i][j] != None and self.board[i][j] == self.board[i][j-1]:
                    movement = True
                    self.board[i][j] *= 2
                    self.board[i][j-1] = None 
            for j in range(self.board_size-1,0, -1):
                if self.board[i][j] == None and self.board[i][j-1] != None:
                    self.board[i][j], self.board[i][j-1] = self.board[i][j-1], None
        return movement
        
    # @TODO
    def slide_top(self):
        movement = False
        # Shift 
        for i in range(0, self.board_size):
            new_list = []
            for j in range(0, self.board_size):
                if self.board[j][i] != None:
                    new_list.append(self.board[j][i])
            for j in range(self.board_size-len(new_list)):
                new_list.append(None)
            for j in range(0, self.board_size):
                if self.board[j][i] != new_list[j]:
                    self.board[j][i] = new_list[j]
                    movement = True
        
        # Merge & Shift Once at max.
        for i in range(0, self.board_size):
            for j in range(0, self.board_size-1):
                if self.board[j][i] != None and self.board[j][i] == self.board[j+1][i]:
                    movement = True
                    self.board[j][i] *= 2
                    self.board[j+1][i] = None 
            for j in range(0, self.board_size-1):
                if self.board[j][i] == None and self.board[j+1][i] != None:
                    self.board[j][i], self.board[j+1][i] = self.board[j+1][i], None
        return movement

    # @TODO
    def slide_bottom(self):
        movement = False
        # Shift 
        for i in range(0, self.board_size):
            new_list = []
            for j in range(self.board_size-1, -1, -1):
                if self.board[j][i] != None:
                    new_list.append(self.board[j][i])
            for j in range(self.board_size-len(new_list)):
                new_list = [None] + new_list
            for j in range(self.board_size-1, -1, -1):
                if self.board[j][i] != new_list[j]:
                    self.board[j][i] = new_list[j]
                    movement = True
        
        # Merge & Shift Once at max.
        for i in range(0, self.board_size):
            for j in range(self.board_size-1, -1, -1):
                if self.board[j][i] != None and self.board[j][i] == self.board[j-1][i]:
                    movement = True
                    self.board[j][i] *= 2
                    self.board[j-1][i] = None 
            for j in range(self.board_size-1, 0, -1):
                if self.board[j][i] == None and self.board[j-1][i] != None:
                    self.board[j][i], self.board[j-1][i] = self.board[j-1][i], None
        return movement

    def check_if_game_won(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if self.board[i][j] == WIN_VALUE:
                    return True
                
        return False
        
    def add_random_tile(self, row, col):
        if self.board[row][col] != None:
            # print('\nInvalid cell')
            return
        # print(f'add_random_tile ADDING VALUE TO {row} {col} {self.board}')
        self.board[row][col] = INSERT_VALUE
        # print(f'add_random_tile ADDED VALUE TO {row} {col} {self.board}')
    
    def get_empty_cells(self):
        result = []
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if not self.board[i][j]:
                    result.append([i, j])
                    
        return result
    
    def print_board(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                print('_' if self.board[i][j] == None else self.board[i][j], end=" ")
            print()
        