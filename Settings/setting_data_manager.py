"""
Class manages saving and loading Setting Profiles. As well as handling the structures
"""
import csv
from os import path

import pandas as pd
from PyQt5 import QtWidgets

import GUI_Handler
from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration

log = 0


def verify_file_exists(file_path: str):
    if file_path == None or file_path == '':
        exists = False
        return exists
    exists = path.isfile(file_path)
    if not exists and (file_path != ''):
        QtWidgets.QMessageBox().critical(GUI_Handler.main_window, 'WARNING', 'File does not exist')
    return exists


class Setting_File_Manager:
    def __init__(self, module_config: [], daq_config: DAQ_Configuration):
        self.module_configs = module_config
        # self.sensor_configs = sens_con
        self.daq_config = daq_config

    def set_filename(self, filename: str):
        """
        Sets an Object File Name for dealing with multiple loads and saves at a time.

        :param filename :  The path of the desired file.
        """
        self.filename = filename
        return filename

    def store_daq_configs(self, filename: str):
        """
        Stores Test Recording Configuration in specified File Name.

        :param filename : The The path of the desired file.
        """
        filename = 'Config/DAQ/' + filename

        # # Generate Test ID
        # if not self.daq_config.recording_configs["test_ID"]:
        #     self.daq_config.recording_configs["test_ID"] = DAQ_Configuration.generate_ID(
        #         self.daq_config.recording_configs['test_name'])

        # if verify_file_exists(filename):
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

            if log: print('Save Daq Configs : SUCCESSFUL')

            f.close()

    def load_daq_configs(self, filename: str):
        """
        Loads setting data from settings file.

        :param filename : the path and name of the file.

        :return list of DAQ Configs
        """
        if verify_file_exists(filename):
            self.daq_config.signal_configs = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]
            self.daq_config.recording_configs = pd.read_csv(filename, header=2, nrows=1).to_dict('r')[0]
            self.daq_config.data_handling_configs = pd.read_csv(filename, header=4, nrows=1).to_dict('r')[0]
            self.daq_config.location_configs = \
                pd.read_csv(filename, header=6, nrows=1, dtype={'longitude': str, 'latitude': str,
                                                                'hour': str, 'minute': str,
                                                                'second': str}).to_dict('r')[0]
            self.daq_config.specimen_location = pd.read_csv(filename, header=8, nrows=1).to_dict('r')[0]

            if log: print('Load Daq Configs : SUCCESSFUL')
        else:
            if log: print('File Error')

        return [self.daq_config.signal_configs, self.daq_config.recording_configs,
                self.daq_config.data_handling_configs,
                self.daq_config.location_configs, self.daq_config.specimen_location]

    def store_recording_configs(self, filename: str):
        """
        Store Only data for Recording.

        :param filename : the path and name of the file.
        """
        rec_file = 'Config/DAQ/Recording/' + filename

        # if verify_file_exists(rec_file):

        with open(rec_file, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.daq_config.recording_configs.keys())
            writer.writerow(self.daq_config.recording_configs.values())

            writer.writerow(self.daq_config.data_handling_configs.keys())
            writer.writerow(self.daq_config.data_handling_configs.values())

            if log: print('store Recording Config Successful')

        f.close()

        # else:
        #     if log: print('Storing Recording Configuration FAILED')

    def load_recording_configs(self, filename: str):
        if verify_file_exists(filename):
            self.daq_config.recording_configs = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]

            if log: print('Load Recording Settings Successful')
        else:
            if log: print('Load Recording Configuration FILE DOES NOT EXISTS')

        return self.daq_config.recording_configs

    def store_location_configs(self, filename: str):
        """
        Store Only data for Location.

        :param filename : the path and name of the file.
        """
        loc_file = 'Config/DAQ/Location/' + filename

        with open(loc_file, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.daq_config.location_configs.keys())
            writer.writerow(self.daq_config.location_configs.values())

            writer.writerow(self.daq_config.specimen_location.keys())
            writer.writerow(self.daq_config.specimen_location.values())

            if log: print('Storing Location Configuration Successful')

        f.close()

    def load_location_configs(self, filename: str):
        """
        Loads Location Configuration from settings file.

        :param filename : the path and name of the file.

        :return Location Configuration Dictionary
        """
        if verify_file_exists(filename):
            self.daq_config.location_configs = pd.read_csv(filename, header=0, nrows=1, dtype=str).to_dict('r')[0]
            self.daq_config.specimen_location = pd.read_csv(filename, header=2, nrows=1, dtype=str).to_dict('r')[0]

            if log: print('Load Location Configuration Successful')
        else:
            if log: print('Load Location Configuration FILE DOES NOT EXISTS')

        return [self.daq_config.location_configs, self.daq_config.specimen_location]

    def store_signal_params(self, filename):
        """
        Store Only Signal Parameters in CSV File.

        :param filename: The desires File Name.
        """
        sig_file = 'Config/DAQ/Signal/' + filename

        with open(sig_file, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(self.daq_config.signal_configs.keys())
            writer.writerow(self.daq_config.signal_configs.values())

            if log: print('Storing Signal Configuration Successful')

        f.close()

    def load_signal_params(self, filename):
        """
        Loads Signal Parameters from settings file.

        :param filename : the path and name of the file.

        :return Signal Parameter Dictionary
        """
        # sig_file = 'Config/DAQ/Signal/' + filename

        if verify_file_exists(filename):
            self.daq_config.signal_configs = pd.read_csv(filename).to_dict('r')[0]

            if log:
                print('Load Location Configuration Successful')
        else:
            if log: print('Load Signal Parameters FILE DOES NOT EXISTS')

        return self.daq_config.signal_configs

    def store_module_configs(self, filename: str, module: Module_Individual):
        """
        Store Only Module Configurations in CSV File.

        :param filename: The desires File Name.
        """
        module_file = 'Config/Module/' + filename
        if verify_file_exists(module_file):
            with open(module_file, 'w+', newline='') as f:
                writer = csv.writer(f)

                # for x in range(0, 1000000, 1):  # TESTING to make sure it is the same always. [PASSED]
                if log: print(list(module.module_info.keys())[0])
                if log: print(type(module.module_info.keys()))

                # Marroneo -  Store values in temp dict so that it will be stored like a word in csv.
                temp_dict = {list(module.module_info.keys())[0]: module.module_info['channel_name']}
                if log: print('WRITE Channel Settings: ' + str(temp_dict))
                writer.writerow(temp_dict.keys())
                writer.writerow(temp_dict.values())

                writer.writerow(module.module_info['Sensor 1'].sensor_info.keys())
                writer.writerow(module.module_info['Sensor 1'].sensor_info.values())

                writer.writerow(module.module_info['Sensor 2'].sensor_info.keys())
                writer.writerow(module.module_info['Sensor 2'].sensor_info.values())

                writer.writerow(module.module_info['Sensor 3'].sensor_info.keys())
                writer.writerow(module.module_info['Sensor 3'].sensor_info.values())

                writer.writerow(module.module_info['Sensor 4'].sensor_info.keys())
                writer.writerow(module.module_info['Sensor 4'].sensor_info.values())

                if log: print('Save Module Configs : SUCCESSFUL')

            f.close()
        else:
            if log: print('File Error')

    def load_module_config(self, filename: str):
        """
        Loads Module Configuration from settings file.

        :param filename : the path and name of the file.

        :return Module Individual Dictionary
        """
        # module_file = 'Config/Module/' + filename
        if verify_file_exists(filename):
            name_dict = pd.read_csv(filename, header=0, nrows=1).to_dict('r')[0]
            sensor_1 = pd.read_csv(filename, header=2, nrows=1).to_dict('r')[0]
            sensor_2 = pd.read_csv(filename, header=4, nrows=1).to_dict('r')[0]
            sensor_3 = pd.read_csv(filename, header=6, nrows=1).to_dict('r')[0]
            sensor_4 = pd.read_csv(filename, header=8, nrows=1).to_dict('r')[0]

            if log: print(name_dict)
            if log: print(sensor_1)
            if log: print(sensor_2)
            if log: print(sensor_3)
            if log: print(sensor_4)

            self.channel_config = Module_Individual.Module(name_dict['channel_name'], sensor_1, sensor_2, sensor_3,
                                                           sensor_4)

            if log: print('Load Module Configs : SUCCESSFUL')

        else:
            if log: print('File Error')

        return self.channel_config

    def settings_to_string(self):
        """
        Reads Data from CSV file and converts it to comma and semi-colon separated STRING

        :return: comma and semi-colon separated STRING
        """
        new_line = ';'
        string = 'Test ID:' + new_line + DAQ_Configuration.generate_ID(
            self.daq_config.recording_configs['test_name']) + new_line

        string += ','.join(self.daq_config.recording_configs.keys()) + new_line
        string += ','.join(str(elem) for elem in self.daq_config.recording_configs.values()) + new_line

        string += ','.join(self.daq_config.signal_configs.keys()) + new_line
        string += ','.join(self.daq_config.signal_configs.values()) + new_line

        string += ','.join(self.daq_config.location_configs.keys()) + new_line
        string += ','.join(self.daq_config.location_configs.values()) + new_line

        string += ','.join(self.daq_config.specimen_location.keys()) + new_line
        string += ','.join(str(elem) for elem in self.daq_config.specimen_location.values()) + new_line

        # Modules information
        for module in self.module_configs:
            string += 'Module Name' + new_line
            string += module.module_info['channel_name'] + new_line

            string += ','.join(module.module_info['Sensor 1'].sensor_info.keys()) + new_line
            string += ','.join(module.module_info['Sensor 1'].sensor_info.values()) + new_line

            string += ','.join(module.module_info['Sensor 2'].sensor_info.keys()) + new_line
            string += ','.join(module.module_info['Sensor 2'].sensor_info.values()) + new_line

            string += ','.join(module.module_info['Sensor 3'].sensor_info.keys()) + new_line
            string += ','.join(module.module_info['Sensor 3'].sensor_info.values()) + new_line

            string += ','.join(module.module_info['Sensor 4'].sensor_info.keys()) + new_line
            string += ','.join(module.module_info['Sensor 4'].sensor_info.values()) + new_line

        if log: print(string)
        return string
