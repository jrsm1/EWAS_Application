channel_info = {
    "sensor_given_name",
    "sensor_parameters",
    "channel_description"
}


class Channel():

    def __init__(self, sensor_name: str, channel_description: str, sensor_parameters: str ):
        channel_info["sensor_given_name"] = sensor_name
        channel_info["sensor_parameters"] = sensor_parameters
        channel_info["channel_description"] = channel_description
