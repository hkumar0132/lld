'''
    Class should depend on interfaces rather than concrete classes
'''

from abc import ABC, abstractmethod
class KeyboardI(ABC):
    pass

class WiredKeyboard(KeyboardI):
    pass

class BluetoothKeyboard(KeyboardI):
    pass

class MouseI(ABC):
    pass

class WiredMouse(MouseI):
    pass

class BluetoothMouse(MouseI):
    pass


class Macbook:

    '''
        If macbook wants to use bluetooth mouse instead of
        wired one, it becomes difficult
    '''
    def __init__(self):
        self.wiredMouse = WiredMouse()
        self.wiredKeyboard = WiredKeyboard()

m = Macbook()

'''
    Solution: constructor injuction
    Now my class Macbook depends on interfaces
    Keyboard and Mouse instead of concrete classes
    WiredMouse and WiredKeyboard
    This makes the code flexible
'''

class Macbook:
    def __init__(self, mouse: MouseI, keyboard: KeyboardI):
        self.mouse = mouse
        self.keyboard = keyboard

bluetoothMouseWiredKeyboard = Macbook(BluetoothMouse(), WiredKeyboard())
bluetoothMouseBluetoothKeyboard = Macbook(BluetoothMouse(), BluetoothKeyboard())