channel_info = {
    "sensor_given_name",
    "sensor_parameters",
    "channel_description"
}


class Sensor:
    # TODO VERIFY IS CASE WHERE SOMETHING IS EMPTY IS POSSIBLE. --> SET DEFAULT VALUES.
    # TODO add default case.
    def __init__(self, sensor_name: str, sensor_description: str, sensor_sensitivity: str, sensor_localization: str):
        self.sensor_info = {
            "sensor_name": sensor_name,
            "description": sensor_description,
            "sensitivity": sensor_sensitivity,
            'localization': sensor_localization
        }


# TESTING
# sens = Sensor('My Sensor', 'No Description', '45 mV/g', "location Null")
# sens.sensor_info['sensor_name'] = 'mNewName'
# sens.sensor_info['sensitivity'] = 'mNewSensi'
# print(sens.sensor_info)
