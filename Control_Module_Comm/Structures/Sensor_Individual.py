SENSOR_TYPES = ['Acceleration', 'Geophone', 'Velocity']


class Sensor:
    # TODO VERIFY IS CASE WHERE SOMETHING IS EMPTY IS POSSIBLE. --> SET DEFAULT VALUES.
    # TODO add default case.
    def __init__(self, sensor_name: str, sensor_type: int, sensor_sensitivity='Not Specified', sensor_localization='Not Specified',
                 sensor_bandwidth='Not Specified', sensor_full_scale='Not Specified', sensor_damping='Not Specified'):
        self.sensor_info = {
            "sensor_name": sensor_name,
            "type": sensor_type,
            "sensitivity": sensor_sensitivity,
            'bandwidth': sensor_bandwidth,
            'full_scale': sensor_full_scale,
            'damping': sensor_damping,
            'localization': sensor_localization
        }


# TESTING
# sens = Sensor('My Sensor', 'No Description', '45 mV/g', "location Null")
# sens.sensor_info['sensor_name'] = 'mNewName'
# sens.sensor_info['sensitivity'] = 'mNewSensi'
# print(sens.sensor_info)
