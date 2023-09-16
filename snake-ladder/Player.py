class Player:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        
    def get_name(self):
        return self.name
    
    def set_position(self, row, col):
        self.row = row
        self.col = col
        
    def get_position(self):
        return [self.row, self.col]