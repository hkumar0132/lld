class Floor:
    def __init__(self, floor_no, external_button) -> None:
        self.floor_no = floor_no
        self.external_button = external_button

    def request_elevator(self, direction):
        self.external_button.press_button(self.floor_no, direction)