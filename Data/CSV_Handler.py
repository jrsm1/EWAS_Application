from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
import csv
from os import path
import pandas as pd

class Data_Handler():
    """
    Class in charge of handling data files.
    """

    def __init__(self, mod_con: [], daq_con: DAQ_Configuration):
        self.module_list = mod_con
        self.daq_config = daq_con

    def store_data(self, filename: str, data: str):
        """
        Stores Metadata as Header and Data bellow on a CSV file.

        :param filename: the file name/path of the desired output file.
        :param data: Comma delimited string containing sensor name and sample data.

        :return: CSV file with metadata header and data body.
        """
        datapath = r'Data/' + filename

        with open(datapath, 'w', newline='') as f:
            writer = csv.writer(f)

            # Test ID
            writer.writerow(DAQ_Configuration.generate_ID(self.daq_config.recording_configs['test_name']))

            # DAQ Configs
            writer.writerow(self.daq_config.recording_configs.keys())
            writer.writerow(self.daq_config.recording_configs.values())

            writer.writerow(self.daq_config.signal_configs.keys())
            writer.writerow(self.daq_config.signal_configs.values())

            writer.writerow(self.daq_config.location_configs.keys())
            writer.writerow(self.daq_config.location_configs.values())

            writer.writerow(self.daq_config.specimen_location.keys())
            writer.writerow(self.daq_config.specimen_location.values())

            # Modules information
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

            dataFrame = self.string_to_dataframe(data)
            # dataFrame.to_csv(datapath)


        f.close()


    def string_to_dataframe(self, string: str):
        """
        Convets Comma delimited string into pandas DataFrame.

        :return:
        :param string: Contains the comma delimited data string.

        :return: Pandas DataFrame with the data from the input string.
        """

        return pd.DataFrame([x.split(',') for x in string.split(';')])


# TESTING
sc1 = Sensor_Individual.Sensor('S1', 0)
sc2 = Sensor_Individual.Sensor('S2', 0)
sc3 = Sensor_Individual.Sensor('S3', 0)
sc4 = Sensor_Individual.Sensor('S4', 0)
dc = DAQ_Configuration.DAQconfigs()
cc = Module_Individual.Module('mName', sc1, sc2, sc3, sc4)
dh = Data_Handler([cc,cc,cc,cc,cc,cc,cc,cc], dc)

data = 'name,param1,param2;mName,mParam,yParam'
dh.store_data('Testing.csv', data)
