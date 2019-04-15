"""
Class manages saving and loading Setting Profiles. As well as handling the structures
"""
from Control_Module_Comm.Structures import Channel_Individual, DAQ_Configuration, Sensor_Individual
import csv
import pandas as pd


class Setting_File_Manager:
    def __init__(self, ch_con: Channel_Individual, sens_con: Sensor_Individual, daq_con: DAQ_Configuration):
        self.channel_config = ch_con
        self.sensor_config = sens_con
        self.daq_config = daq_con

    def set_filename(self, filename: str):
        self.filename = filename
        return filename

    def store_daq_configs(self, filename: str):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.daq_config.signal_configs.keys())
            writer.writerow(self.daq_config.signal_configs.values())

            writer.writerow(self.daq_config.recording_configs.keys())
            writer.writerow(self.daq_config.recording_configs.values())

            writer.writerow(self.daq_config.data_handling_configs.keys())
            writer.writerow(self.daq_config.data_handling_configs.values())

            writer.writerow(self.daq_config.location_configs.keys())
            writer.writerow(self.daq_config.location_configs.values())

            writer.writerow(self.daq_config.specimen_location.keys())
            writer.writerow(self.daq_config.specimen_location.values())

    """
    Loads setting data from settings file. 

    :param filename : the path and name of the file.

    :return list of DAQ Configs 
    """
    def load_daq_configs(self, filename: str):
        self.daq_config.signal_configs = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]
        self.daq_config.recording_configs = pd.read_csv(filename, header=2, nrows=1).to_dict('r')[0]
        self.daq_config.data_handling_configs = pd.read_csv(filename, header=4, nrows=1).to_dict('r')[0]
        self.daq_config.location_configs = pd.read_csv(filename, header=6, nrows=1).to_dict('r')[0]
        self.daq_config.specimen_location = pd.read_csv(filename, header=8, nrows=1).to_dict('r')[0]


        return [self.daq_config.signal_configs, self.daq_config.recording_configs, self.daq_config.data_handling_configs,
                self.daq_config.location_configs, self.daq_config.specimen_location]

    def store_channel_configs(self, filename: str):
        with open(filename, 'w+', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.channel_config.channel_info.keys())
            writer.writerow(self.channel_config.channel_info.values())

    def load_channel_config(self, filename: str):
        self.channel_config = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]

        return self.channel_config

    def store_sensor_config(self, filename: str):
        with open(filename, 'w+', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.sensor_config.sensor_info.keys())
            writer.writerow(self.sensor_config.sensor_info.values())

    def load_sensor_config(self, filename: str):
        self.sensor_config = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]

        return self.sensor_config

    # def store_ALL_channels(self, filename): # TODO Implement store all sensor data in columns.


# TESTING
sc = Sensor_Individual.Sensor('Name', 0)
cc = Channel_Individual.Channel('mName', sc, sc, sc, sc)
daq = DAQ_Configuration.DAQconfigs()
sfm = Setting_File_Manager(cc, sc, daq)
# print(cc.channel_info)
# print(sc.sensor_info)
# print(daq.signal_configs)
# print(daq.testing_configs)
# print(daq.data_handling_configs)

# print(sfm.channel_config.channel_info)
# print(sfm.Sensor_config.sensor_info)
# print(sfm.daq_config.signal_configs)
# print(sfm.daq_config.testing_configs)
# print(sfm.daq_config.data_handling_configs)

# TODO create a method that does this and set it the correct path.
# filename = r'../Data/Channel_Settings.csv'
# sfm.store_channel_configs(filename)
# d = sfm.load_channel_config(filename)
# print(d)

filename = r'../Data/writting_settings.csv'
# sfm.daq_config.specimen_location['1'] = 'Something ELse'

sfm.store_daq_configs(filename)
d = sfm.load_daq_configs(filename)
# print(len(d))

for x in range(0, len(d), 1):
    print(d[x])
# print('\n' + str(type(d[0])))
