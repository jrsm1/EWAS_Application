SENSOR_TYPES = ['Acceleration', 'Geophone', 'Velocity']


class Sensor:
    def __init__(self, sensor_name: str, sensor_type=0, sensor_sensitivity='Not Specified', sensor_localization='Not Specified',
                 sensor_bandwidth='Not Specified', sensor_full_scale='Not Specified', sensor_damping='Not Specified'):
        self.sensor_info = {
            "sensor_name": sensor_name,
            "type": SENSOR_TYPES[sensor_type],
            "sensitivity": sensor_sensitivity,
            'bandwidth': sensor_bandwidth,
            'full_scale': sensor_full_scale,
            'damping': sensor_damping,
            'localization': sensor_localization
        }
        self.connected = False  # False by default because most of the time 32 sensors are not connected.
        # self.checkmark = False

    def set_Connected(self, connected: bool):
        self.connected = connected
        return connected

    def get_Connected(self):
        return self.connected

    # def set_checkmark(self, checkmark: bool):
    #     self.checkmark = checkmark
    #     return  checkmark
    #
    # def is_checkmark(self):
    #     return self.checkmark


# TESTING
# sens = Sensor('My Sensor', 0, '45 mV/g', "location Null")
# sens.sensor_info['sensor_name'] = 'mNewName'
# sens.sensor_info['sensitivity'] = 'mNewSensitivity'
# print(sens.sensor_info)
#
# print(sens.connected)
# print(sens.get_Connected())
# print(sens.set_Connected(True))
# print(sens.get_Connected())
# print(sens.connected)
