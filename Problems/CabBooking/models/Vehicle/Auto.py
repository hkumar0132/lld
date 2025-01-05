from .Vehicle import Vehicle
class Auto(Vehicle):
    def __init__(self, model, reg_no) -> None:
        super().__init__(model, reg_no)