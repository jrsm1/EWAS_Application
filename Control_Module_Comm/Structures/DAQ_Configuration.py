import time
import uuid

TEST_TYPES = ['Free-Field', 'Laboratory', 'Building']

class DAQconfigs:
    """
    IF default=False --> MUST PROVIDE ALL PARAMETERS FIXME
    """

    def __init__(self,
                 sampling_rate=0, cutoff_frequency=0, signal_gain=0,
                 test_duration=15, test_name='Test_' + uuid.uuid4().hex, record_type=0,
                 loc_name='No Name', latitude='0:00:0000', longitude='0:00:0000', hour='00', minute='00', second='00',
                 specimen_1='Not Used', specimen_2='Not Used', specimen_3='Not Used', specimen_4='Not Used',
                 specimen_5='Not Used', specimen_6='Not Used', specimen_7='Not Used', specimen_8='Not Used',
                 visualize=True, store=False):

        self.signal_configs = {
            "sampling_rate": int,
            "cutoff_frequency": int,
            "signal_gain": int
        }

        self.recording_configs = {
            "test_name": uuid,  # Random at first FIXME --> Now doing in __init__ method.
            "test_ID": time,  # TODO AUTO-GENERATE ID.
            "test_duration": int,  # In Seconds
            "test_type": int  # Number in list. Should be same as position in drop-down.
        }

        self.data_handling_configs = {
            "visualize": bool,
            "store": bool
        }

        self.location_configs = {
            'loc_name': str,
            'longitude': str,
            'latitude': str,
            'hour': int,
            'minute': int,
            'second': int,
        }

        self.specimen_location = {
            '1': str,
            '2': str,
            '3': str,
            '4': str,
            '5': str,
            '6': str,
            '7': str,
            '8': str,
        }

        if len(test_name) > 20:
            test_name = test_name[0: 20]

        # if default:  # FIXME Does not store default given values. MUST INPUT ALL.
        self.signal_configs["sampling_rate"] = sampling_rate
        self.signal_configs["cutoff_frequency"] = cutoff_frequency
        self.signal_configs["signal_gain"] = signal_gain

        self.recording_configs["test_name"] = test_name
        self.recording_configs["test_ID"] = self.generate_ID(test_name)
        self.recording_configs["test_duration"] = test_duration
        self.recording_configs["test_type"] = record_type

        self.location_configs['loc_name'] = loc_name
        self.location_configs['longitude'] = longitude
        self.location_configs['latitude'] = latitude
        self.location_configs['hour'] = hour
        self.location_configs['minute'] = minute
        self.location_configs['second'] = second

        self.specimen_location['1'] = specimen_1
        self.specimen_location['2'] = specimen_2
        self.specimen_location['3'] = specimen_3
        self.specimen_location['4'] = specimen_4
        self.specimen_location['5'] = specimen_5
        self.specimen_location['6'] = specimen_6
        self.specimen_location['7'] = specimen_7
        self.specimen_location['8'] = specimen_8

        self.data_handling_configs["visualize"] = visualize
        self.data_handling_configs["store"] = store

        # else:
        # try:
        #     test_name_default = str(self.recording_configs["start_time_requested"]) + str(
        #         self.recording_configs["sensor_localization"])
        # except:
        #     test_name_default = str(time.localtime(time.time())) + '-' + str(uuid.uuid4().hex)
        #
        # self.recording_configs["test_name"] = test_name_default

    """
    Generates Test ID from Test Name
    
    :param name : Test Name to generate ID from.
    """
    def generate_ID(self, name: str):  # TODO IMPLEMENT BETTER.
        if len(name) > 10:
            name = name[0: 10]
        return name

# Testing
# dq = DAQconfigs()
# print(dq.data_handling_configs)
# print(dq.signal_configs['sampling_rate'])
# print(dq.recording_configs)
# print(dq.location_configs)
# print(dq.specimen_location)


