import time
import uuid


class DAQconfigs:

    """
    IF default=False --> MUST PROVIDE ALL PARAMETERS FIXME
    """
    def __init__(self, default,
                 sampling_rate=2000, cutoff_frequency=1000, signal_gain=1,
                 start_time=time.localtime(time.time()), test_duration=15, test_name='Test_'+uuid.uuid4().hex,
                 sensor_localization='No Location Specified',
                 visualize=False, store=True):

        self.signal_configs = {
            "sampling_rate": int,
            "cutoff_frequency": int,
            "signal_gain": int
        }

        self.testing_configs = {
            "start_time_requested": time,  # Get current time in epoch seconds and convert to local struct_time.
            "test_duration": int,  # In Seconds
            "test_name": uuid,  # Random at first FIXME --> Now doing in __init__ method.
            "sensor_localization": str
        }

        self.data_handling_configs = {
            "visualize": False,
            "store": False
        }


        if default: # FIXME Does not store default given values. MUST INPUT ALL.
            self.signal_configs["sampling_rate"] = sampling_rate
            self.signal_configs["cutoff_frequency"] = cutoff_frequency
            self.signal_configs["signal_gain"] = signal_gain


            self.testing_configs["start_time_requested"] = start_time
            self.testing_configs["test_duration"] = test_duration
            self.testing_configs["test_name"] = test_name
            self.testing_configs["sensor_localization"] = sensor_localization

            self.data_handling_configs["visualize"] = visualize
            self.data_handling_configs["store"] = store

        else:
            try:
                test_name_default = str(self.testing_configs["start_time_requested"]) + str(self.testing_configs["sensor_localization"])
            except:
                test_name_default = str(time.localtime(time.time())) + '-' + str(uuid.uuid4().hex)


            self.testing_configs["test_name"] = test_name_default


dq = DAQconfigs(default=True)
print(dq.data_handling_configs)
print(dq.signal_configs['sampling_rate'])
print(dq.testing_configs)
