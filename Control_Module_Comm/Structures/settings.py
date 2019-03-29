import time
import uuid

signal_settings = {
    "sampling_rate": 2000,
    "cutoff_frequency": 1000,
    "signal_gain": 1
}

testing_settings = {
    "start_time_requested": time.localtime(time.time()), # Get current time in epoch seconds and convert to local struct_time.
    "test_duration": 15,  # In Seconds
    "test_name": uuid.uuid4().hex,  # Random at first FIXME --> Now doing in __init__ method.
    "sensor_localization": "No Location Specified"
}

data_handling_settings = {
    "visualize": False,
    "store": False
}


class DAQsettings:

    def __init__(self, default,
                 sampling_rate: int, cutoff_frequency: int, signal_gain: int,
                 start_time: time, test_duration: int, test_name: str, sensor_localization: str,
                 visualize: bool, store: bool):

        if (default != True):
            signal_settings["sampling_rate"] = sampling_rate
            signal_settings["cutoff_frequency"] = cutoff_frequency
            signal_settings["signal_gain"] = signal_gain

            testing_settings["start_time_requested"] = start_time
            testing_settings["test_duration"] = test_duration
            testing_settings["test_name"] = test_name
            testing_settings["sensor_localization"] = sensor_localization

            data_handling_settings["visualize"] = visualize
            data_handling_settings["store"] = store

        else:
            test_name_default = testing_settings["start_time"] + testing_settings["sensor_location"]

            testing_settings["test_name"] = test_name_default
