class AirConditioner:

    def __init__(self) -> None:
        self.is_on = False
        self.temperature = None

    def turn_on_ac(self):
        self.is_on = True
        print("AC IS ON")

    def turn_off_ac(self):
        self.is_on = False
        print("AC IS OFF")

    def set_temperature(self, temp):
        self.temperature = temp