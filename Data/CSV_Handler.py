from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
import csv
from os import path
import pandas as pd

class Data_Handler():
    """
    Class in charge of handling data files.
    """

    def __init__(self, filename: str, mod_con: [], sens_con: Sensor_Individual, daq_con: DAQ_Configuration):
        self.filename = filename
        self.module_list = mod_con
        self.sensor_config = sens_con
        self.daq_config = daq_con

    def store_data(self, filename: str):
        datapath = r'Data/' + filename

        with open(datapath, 'w', newline='') as f:
            writer = csv.writer(f)

            # DAQ Configs
            writer.writerow(self.daq_config.recording_configs.keys())
            writer.writerow(self.daq_config.recording_configs.values())

            writer.writerow(self.daq_config.signal_configs.keys())
            writer.writerow(self.daq_config.signal_configs.values())

            writer.writerow(self.daq_config.location_configs.keys())
            writer.writerow(self.daq_config.location_configs.values())

            writer.writerow(self.daq_config.specimen_location.keys())
            writer.writerow(self.daq_config.specimen_location.values())

            for module in self.module_list:
                # Marroneo -  Store values in temp dict so that it will be stored like a word in csv.
                temp_dict = {list(module.channel_info.keys())[0]: module.channel_info['channel_name']}
                writer.writerow(temp_dict.keys())
                writer.writerow(temp_dict.values())

                writer.writerow(module.channel_info['Sensor 1'].sensor_info.keys())
                writer.writerow(module.channel_info['Sensor 1'].sensor_info.values())

                writer.writerow(module.channel_info['Sensor 2'].sensor_info.keys())
                writer.writerow(module.channel_info['Sensor 2'].sensor_info.values())

                writer.writerow(module.channel_info['Sensor 3'].sensor_info.keys())
                writer.writerow(module.channel_info['Sensor 3'].sensor_info.values())

                writer.writerow(module.channel_info['Sensor 4'].sensor_info.keys())
                writer.writerow(module.channel_info['Sensor 4'].sensor_info.values())


