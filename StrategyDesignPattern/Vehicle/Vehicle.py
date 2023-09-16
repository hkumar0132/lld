class Vehicle:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def drive(self):
        self.strategy.drive()