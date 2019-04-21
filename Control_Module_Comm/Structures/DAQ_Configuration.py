import string
import time
import uuid
import random

TEST_TYPES = ['Free-Field', 'Laboratory', 'Building']
ID_LIMIT = 10
NAME_LIMIT = 20

class DAQconfigs:
    def __init__(self,
                 sampling_rate=7, cutoff_frequency=7, signal_gain=1,
                 test_duration=15, test_name='Test' + uuid.uuid4().hex, record_type=0, test_delay=0,
                 loc_name='No Name', latitude='+0000.0000', longitude='-0000.0000', hour='00', minute='00', second='00',
                 specimen_1='Not Used', specimen_2='Not Used', specimen_3='Not Used', specimen_4='Not Used',
                 specimen_5='Not Used', specimen_6='Not Used', specimen_7='Not Used', specimen_8='Not Used',
                 visualize=True, store=False):

        self.signal_configs = {
            'sampling_rate': int,
            'cutoff_frequency': int,
            'signal_gain': int
        }

        self.recording_configs = {
            "test_name": str,
            # "test_ID": str,
            "test_duration": int,  # In Seconds
            "test_type": str,  # get from list. Should be same as position in drop-down.
            'test_start_delay': int  # Number in Seconds.
        }

        self.data_handling_configs = {
            "visualize": bool,
            "store": bool
        }

        self.location_configs = {
            'loc_name': str,
            'longitude': str,
            'latitude': str,
            'hour': str,
            'minute': str,
            'second': str,
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

        if len(test_name) > NAME_LIMIT:
            test_name = test_name[0: NAME_LIMIT]

        self.test_id = {'Test ID': generate_ID(test_name) }

        self.signal_configs["sampling_rate"] = sampling_rate
        self.signal_configs["cutoff_frequency"] = cutoff_frequency
        self.signal_configs["signal_gain"] = signal_gain

        self.recording_configs["test_name"] = test_name
        # self.recording_configs["test_ID"] = generate_ID(test_name)
        self.recording_configs["test_duration"] = test_duration
        self.recording_configs["test_type"] = TEST_TYPES[record_type]
        self.recording_configs['test_start_delay'] = test_delay

        self.location_configs['loc_name'] = loc_name
        self.location_configs['longitude'] = longitude
        self.location_configs['latitude'] = latitude
        self.location_configs['hour'] = hour
        self.location_configs['minute'] = minute
        self.location_configs['second'] = second

        self.specimen_location['Specimen 1'] = specimen_1
        self.specimen_location['Specimen 2'] = specimen_2
        self.specimen_location['Specimen 3'] = specimen_3
        self.specimen_location['Specimen 4'] = specimen_4
        self.specimen_location['Specimen 5'] = specimen_5
        self.specimen_location['Specimen 6'] = specimen_6
        self.specimen_location['Specimen 7'] = specimen_7
        self.specimen_location['Specimen 8'] = specimen_8

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


    def get_test_ID(self):
        """
        Getter Method for Test_ID.

        :return: Test ID String.
        """
        return self.test_id


    """
    Generates Test ID from Test Name
    
    :param name : Test Name to generate ID from.
    """
def generate_ID(name: str):
    answer = name[0: int(ID_LIMIT/2)]

    answer = answer + '_'
    stop = len(answer)
    letters = string.ascii_lowercase
    for i in range(10-stop):
        answer = answer + random.choice(letters)

    return answer

# Testing
# generate_ID('aqwsxcderfvvbhynmjhgyhgghn')
# dq = DAQconfigs()
# print(dq.data_handling_configs)
# print(dq.signal_configs['sampling_rate'])
# print(dq.recording_configs)
# print(dq.location_configs)
# print(dq.specimen_location)


