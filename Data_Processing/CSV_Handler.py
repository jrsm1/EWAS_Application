from time import sleep

from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Control_Module_Comm import instruction_manager as ins_man
import numpy as np
import GUI_Handler
import serial
import csv
import pandas as pd

# Global Variables
TIMESTAMP = 'timestamp'

log = 1


class Data_Handler():
    """
    Class in charge of handling data files.
    """

    def __init__(self, mod_all, daq_con: DAQ_Configuration):
        self.module_list = mod_all
        self.daq_config = daq_con
        self.all_data = pd.DataFrame

    def store_data(self, filename: str, data: pd.DataFrame):
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
            # Marroneo -  Store values in temp dict so that it will be stored like a word in csv.
            temp_dict = {'Test ID:': DAQ_Configuration.generate_ID(self.daq_config.recording_configs['test_name'])}
            writer.writerow(temp_dict.keys())
            writer.writerow(temp_dict.values())

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
                temp_dict = {list(module.module_info.keys())[0]: module.module_info['channel_name']}
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

            # Empty Rows to separate Header from Data.
            writer.writerow('')
            writer.writerow('')

            f.close()

        with open(datapath, 'a', newline='') as f:
            data.to_csv(datapath, mode='a', index=False)
        f.close()

    def string_to_dataframe(self, string: str, timestamp=None):
        """
        Converts Comma delimited string into pandas DataFrame.

        :param string: Contains the comma delimited data string.
        :param timestamp: True if the string to convert has Timestamp data.

        :return: Pandas DataFrame with the data from the input string.
        """
        # Select Column Based on Selected Sensors.
        if timestamp:
            columns = [TIMESTAMP]
        else:
            columns = select_data_columns()
        return pd.DataFrame([x.split(',') for x in string.split(';')], columns=columns)

    def list_to_dataframe(self, list_of_lists: []):
        """
        Converts a list of module sensors containing list of its data.
        :param list_of_lists: containing list of sensor data.
        :return: Dataframe where the columns are sensor data.
        """
        columns = select_data_columns()
        dataframe = pd.DataFrame(list_of_lists)
        dataframe = dataframe.transpose()
        dataframe.columns = columns
        return dataframe

    def read_data(self, filename: str):
        """
        Reads Data from Data File in CSV format into a Pandas DataFrame.

        :param filename: The desired File Name.

        :return: Pandas DataFrame containing Sensor Names and Data.
        """
        filename = r'Data/' + filename
        data_read = pd.read_csv(filename, header=90, index_col=TIMESTAMP)  # TODO Test

        return data_read

    def data_to_string(self, filename):
        """
        Reads Data from CSV file and converts it to comma and semi-colon separated STRING

        :param filename: The desired File Name to read from.

        :return: comma and semi-colon separated STRING
        """
        string = self.read_data(filename).head().to_string().split('\n')

        result = ''
        for x in [','.join(ele.split()) for ele in string]:
            result += x + ';'

        return result

    def set_timestamp(self):
        """
        Generates timestamp based on sampling frequency and test duration and adds it to the test data DataFrame.
        """
        timestamp = ''
        time = 0
        sampling_freq = GUI_Handler.daq_config.get_sampling_freq()
        duration = GUI_Handler.daq_config.get_duration()
        time_step = 1 / sampling_freq
        samples = sampling_freq * duration

        for x in np.arange(samples-1):
            time += time_step
            timestamp += str(time) + ';'  # New line every timestamp calculated.

        # Do last value because otherwise it will let the last value NaN.  ## TODO VERIFY IF NEEDED TO FILTER.
        time += time_step
        timestamp += str(time)

        # store timestamp in DataFrame
        timedf = self.string_to_dataframe(timestamp, timestamp=True)
        timedf = timedf.astype(float)

        # Join Timestamp to all_data and set it as Index
        self.all_data = timedf.join(self.all_data)
        # self.all_data.set_index(TIMESTAMP)

    def request_all_data(self, connected_modules: set, ins: ins_man):
        """
        Gets data from Control Module and parses it into a single Pandas DataFrame.

        :param connected_modules: 1/0 List indicating connected modules.
        :param ins : Instruction Manager Instance for request data instructions.

        :return: Pandas DataFrame with joint module sensor data.
        """
        list = []
        self.all_data = pd.DataFrame()
        self.set_timestamp()

        for module in connected_modules:
            print(list)  # String necessary here to connect inner and outer variables apparently.
            try:
                # im = ins_man.instruction_manager(get_port())
                list = ins.send_request_data(module)
            except serial.SerialException:
                GUI_Handler.base_window.display_error('Device has been Disconnected. <br>'
                                                      ' Data Collection Aborted.')
                break

            self.all_data = self.all_data.join(self.list_to_dataframe(list))

        # Convert Data Values as float.
        self.all_data = self.all_data.dropna()
        self.all_data.astype(int)

        if log:
            print(self.all_data)
            print(self.all_data.info())

        return self.all_data

def read_sensor_headers(filename: str):
    """
    Reads Sensor Names from Data in _filename_  as a Pandas DataFrame.
    This method reads The columns, ignoring _Timestamp_, which are the sensor names for which
    data exists in the given File.

    :param filename: The Data File

    :return: Pandas Series with the Data.
    """
    return pd.read_csv(filename, header=90, nrows=0).columns.tolist()[1:]

def select_data_columns():
    """
    Selects Connected Sensors

    :return: List of connected Sensors.
    """
    connected_module_list = [1, 0, 0, 0, 0, 0, 0, 0]
    # try:
    #     connected_module_list = ins_man.instruction_manager(get_port()).send_request_number_of_mods_connected()
    # except serial.SerialException:
    #     # show_error('')
    #     print('Serial Error.')

    sensor_list = []
    if log: print("CSV_Handler - entered Select sensor Headers")
    if connected_module_list[0]:
        sensor_list.append('Sensor_1')
        sensor_list.append('Sensor_2')
        sensor_list.append('Sensor_3')
        sensor_list.append('Sensor_4')
    if connected_module_list[1]:
        sensor_list.append('Sensor_5')
        sensor_list.append('Sensor_6')
        sensor_list.append('Sensor_7')
        sensor_list.append('Sensor_8')
    if connected_module_list[2]:
        sensor_list.append('sensor_9')
        sensor_list.append('sensor_10')
        sensor_list.append('sensor_11')
        sensor_list.append('sensor_12')
    if connected_module_list[3]:
        sensor_list.append('sensor_13')
        sensor_list.append('sensor_14')
        sensor_list.append('sensor_15')
        sensor_list.append('sensor_16')
    if connected_module_list[4]:
        sensor_list.append('sensor_17')
        sensor_list.append('sensor_18')
        sensor_list.append('sensor_19')
        sensor_list.append('sensor_20')
    if connected_module_list[5]:
        sensor_list.append('sensor_21')
        sensor_list.append('sensor_22')
        sensor_list.append('sensor_23')
        sensor_list.append('sensor_24')
    if connected_module_list[6]:
        sensor_list.append('sensor_25')
        sensor_list.append('sensor_26')
        sensor_list.append('sensor_27')
        sensor_list.append('sensor_28')
    if connected_module_list[7]:
        sensor_list.append('sensor_29')
        sensor_list.append('sensor_30')
        sensor_list.append('sensor_31')
        sensor_list.append('sensor_32')
    if log: print("CSV_Handler - got out of Select sensor Headers")

    return sensor_list

def get_port():
    global ins_port
    port = 'COM-1'
    pid = "0403"
    hid = "6001"
    ports = list(serial.tools.list_ports.comports())

    for p in ports:
        if pid and hid in p.hwid:
            port = p.device
    ins_port = port
    return port

# ----------  TESTING  ------------------
# sc1 = Sensor_Individual.Sensor('S1', 0)
# sc2 = Sensor_Individual.Sensor('S2', 0)
# sc3 = Sensor_Individual.Sensor('S3', 0)
# sc4 = Sensor_Individual.Sensor('S4', 0)
# dc = DAQ_Configuration.DAQconfigs()
# cc = Module_Individual.Module('mName', sc1, sc2, sc3, sc4)
# dh = Data_Handler([cc,cc,cc,cc,cc,cc,cc,cc], dc)
#
# data = '1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4'
# # dh.store_data('Testing.csv', data)
# print(dh.data_to_string('Testing.csv'))
# dh.read_sensor_headers('Testing.csv')
