class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        
    def get_head_tail_position(self):
        return [self.head, self.tail]