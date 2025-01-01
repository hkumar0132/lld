from IExternalButton import IExternalButton
from IExternalButtonDispatcher import IExternalButtonDispatcher

class ExternalButton(IExternalButton):

    def __init__(self, button_dispatcher: IExternalButtonDispatcher) -> None:
        self.button_dispatcher = button_dispatcher

    def press_button(self, floor_no, direction):
        self.button_dispatcher.dispatch(floor_no, direction)