from IInternalButton import IInternalButton

class InternalButton(IInternalButton):

    def __init__(self, button_dispatcher) -> None:
        self.button_dispatcher = button_dispatcher

    def press_button(self):
        self.button_dispatcher.dispatch()