import random
import string
import uuid

SAMPLING_RATES = ['2 Hz', '4 Hz', '8 Hz', '16 Hz', '32 Hz', '64 Hz', '128 Hz', '256 Hz', '512 Hz',
                  '1024 Hz', '2048 Hz', '4096 Hz', '8192 Hz', '16384 Hz', '20000 Hz']
CUTOFF_FREQUENCIES = ['1 Hz', '2 Hz', '4 Hz', '8 Hz', '16 Hz', '32 Hz', '64 Hz', '128 Hz', '256 Hz', '512 Hz',
                      '1024 Hz', '2048 Hz', '4096 Hz', '8192 Hz', '10000 Hz']
GAINS = ['0.2 V/V', '1 V/V', '10 V/V', '20 V/V', '30 V/V', '40 V/V', '60 V/V', '80 V/V', '120 V/V', '157 V/V']
TEST_TYPES = ['Free-Field', 'Laboratory', 'Building']
ID_LIMIT = 10
NAME_LIMIT = 20


class DAQconfigs:
    def __init__(self,
                 sampling_rate=7, cutoff_frequency=7, signal_gain=1,
                 test_duration=15, test_name='Test' + uuid.uuid4().hex, record_type=0, test_delay=0,
                 loc_name='NoName', latitude='+0000.0000', longitude='-0000.0000', hour='00', minute='00', second='00',
                 specimen_1='Not Used', specimen_2='Not Used', specimen_3='Not Used', specimen_4='Not Used',
                 specimen_5='Not Used', specimen_6='Not Used', specimen_7='Not Used', specimen_8='Not Used',
                 store='1111'):

        self.signal_configs = {
            'sampling_rate': str,
            'cutoff_frequency': str,
            'signal_gain': str
        }

        self.recording_configs = {
            "test_name": str,
            "test_duration": int,  # In Seconds
            "test_type": str,  # get from list. Should be same as position in drop-down.
            'test_start_delay': int  # Number in Seconds.
        }

        self.data_handling_configs = {
            "store": str
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
            'Specimen 1': str,
            'Specimen 2': str,
            'Specimen 3': str,
            'Specimen 4': str,
            'Specimen 5': str,
            'Specimen 6': str,
            'Specimen 7': str,
            'Specimen 8': str,
        }

        if len(test_name) > NAME_LIMIT:
            test_name = test_name[0: NAME_LIMIT]

        self.test_id = {'Test ID': generate_ID(test_name)}

        self.sampling_rate_index = sampling_rate
        self.cutoff_freq_index = cutoff_frequency
        self.gain_index = signal_gain

        self.signal_configs["sampling_rate"] = SAMPLING_RATES[sampling_rate]
        self.signal_configs["cutoff_frequency"] = CUTOFF_FREQUENCIES[cutoff_frequency]
        self.signal_configs["signal_gain"] = GAINS[signal_gain]

        self.recording_configs["test_name"] = test_name
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

    def get_sampling_freq(self):
        return int(self.signal_configs['sampling_rate'].split()[0])

    def get_duration(self):
        return int(self.recording_configs['test_duration'])


def generate_ID(name: str):
    """
    Generates Test ID from Test Name
    
    :param name : Test Name to generate ID from.
    """
    answer = name[0: int(ID_LIMIT / 2)]

    answer = answer + '_'
    stop = len(answer)
    letters = string.ascii_lowercase
    for i in range(10 - stop):
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
# print(dq.get_sampling_freq())

