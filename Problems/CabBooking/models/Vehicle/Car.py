from .Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, model, reg_no) -> None:
        super().__init__(model, reg_no)