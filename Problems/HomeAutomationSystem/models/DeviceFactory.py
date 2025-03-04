from .Device import Device
from .Light import Light
from .Fan import Fan
from .Thermostat import Thermostat
from .Enums.DeviceTypes import DeviceTypes

class DeviceFactory:

    def get_device(self, device_type: DeviceTypes, device_id, **args):
        if device_type == DeviceTypes.LIGHT:
            return Light(device_id, **args)
        elif device_type == DeviceTypes.FAN:
            return Fan(device_id, **args)
        elif device_type == DeviceTypes.THERMOSTAT:
            return Thermostat(device_id, **args)

        raise Exception('Device does not exist')
        