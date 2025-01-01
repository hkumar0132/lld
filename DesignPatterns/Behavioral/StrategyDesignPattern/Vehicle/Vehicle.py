from Strategy import Drive

class Vehicle:
    def __init__(self, drive_strategy: Drive) -> None:
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()