channel_info = {
    "sensor_given_name",
    "sensor_parameters",
    "channel_description"
}


class Sensor:
    # TODO VERIFY IS CASE WHERE SOMETHING IS EMPTY IS POSSIBLE. --> SET DEFAULT VALUES.
    def __init__(self, sensor_name: str, sensor_description: str, sensor_sensitivity: str, sensor_localization: str):
        self.sensor_info = {
            "given_name": sensor_name,
            "sensitivity": sensor_sensitivity,
            "description": sensor_description,
            'localization': sensor_localization
        }


# TESTING
sens = Sensor('My Sensor', 'No Description', '45 mV/g', "location Null")
print(sens.sensor_info)
