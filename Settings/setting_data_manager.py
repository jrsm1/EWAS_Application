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

            writer.writerow(self.daq_config.testing_configs.keys())
            writer.writerow(self.daq_config.testing_configs.values())

            writer.writerow(self.daq_config.data_handling_configs.keys())
            writer.writerow(self.daq_config.data_handling_configs.values())

            """
                Loads setting data from settings file. 

                :param filename : the path and name of the file.

                :return list of DAQ Configs 
                """

    def load_daq_configs(self, filename: str):
        self.daq_config.signal_configs = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]
        self.daq_config.testing_configs = pd.read_csv(filename, header=2, nrows=1).to_dict('r')[0]
        self.daq_config.data_handling_configs = pd.read_csv(filename, header=4, nrows=1).to_dict('r')[0]

        return [self.daq_config.signal_configs, self.daq_config.testing_configs, self.daq_config.data_handling_configs]

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


# TESTING
cc = Channel_Individual.Channel('mName')
sc = Sensor_Individual.Sensor('Name', 'fds', 'fdrfre', 'fregeg')
daq = DAQ_Configuration.DAQconfigs(True)
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

# TODO create a method than does this and set it the correct path.
filename = r'../Data/Channel_Settings.csv'
sfm.store_channel_configs(filename)
d = sfm.load_channel_config(filename)
print(d)
