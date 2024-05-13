'''
(0,0)





(9,0)

'''

class Board:
    def __init__(self):
        self.size = 10
        self.board = []
        self.snakes = []
        self.ladders = []
        self.initialize_board()
        
    def initialize_board(self):
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                row.append([i, j])
            self.board.append(row)
        
    def add_snake(self, snake):
        position = snake.get_head_tail_position()
        self.board[position[0][0]][position[0][1]] = position[1] #move to tail
    
    def add_ladder(self, ladder):
        position = ladder.get_start_end_position()
        self.board[position[0][0]][position[0][1]] = position[1]

    def move_player_position(self, row, col, move):
        new_row = row 
        new_col = col
        if row%2 == 0:
            if col + move <= 9:
                new_col += move
            else:
                new_row += 1
                new_col = 19 - (col + move)
        else:
            if col - move >= 0:
                new_col -= move
            else:
                new_row += 1
                new_col += -(col - move + 1)

        #position didn't change
        if new_row > 9 or new_col > 9 or new_col < 0 or new_row < 0:
            return [row, col]
                
        # print(f'SNAKE OR LADDER ENCOUNTERED: MOVING FROM {new_row}, {new_col} -> {self.board[new_row][new_col]}')
        return self.board[new_row][new_col]