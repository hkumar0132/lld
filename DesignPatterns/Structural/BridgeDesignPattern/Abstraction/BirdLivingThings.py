from Implementor import BreatheImplementor
from .LivingThings import LivingThings

class BirdLivingThings(LivingThings):

    def __init__(self, implementor: BreatheImplementor) -> None:
        super().__init__(implementor)

    def breathe_process(self):
        self.implementor.breathe()