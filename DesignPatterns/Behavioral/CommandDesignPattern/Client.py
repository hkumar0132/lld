from RemoteController import RemoteController
from Command.impl import TurnOnAc, TurnOffAc
from AirConditioner import AirConditioner

class Client:

    ac = AirConditioner()

    remote = RemoteController()
    remote.set_command(TurnOnAc(ac))
    remote.press_button()

    remote.set_command(TurnOffAc(ac))
    remote.press_button()