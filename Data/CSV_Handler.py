from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Control_Module_Comm import instruction_manager as ins_man
import serial
import csv
import pandas as pd

log = 1
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

        datapath = r'../Data/' + filename

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

            # Empty Rows to separate Header from Data.
            writer.writerow('')
            writer.writerow('')

            f.close()

        with open(datapath, 'a', newline='') as f:
            dataFrame = self.string_to_dataframe(data)
            dataFrame.to_csv(datapath, mode='a', index=False)
        f.close()

    def string_to_dataframe(self, string: str):
        """
        Converts Comma delimited string into pandas DataFrame.

        :param string: Contains the comma delimited data string.

        :return: Pandas DataFrame with the data from the input string.
        """

        # Select Column Based on Selected Sensors.
        columns = select_data_columns()
        return pd.DataFrame([x.split(',') for x in string.split(';')], columns=columns)

    def read_data(self, filename: str):
        """
        Reads Data from Data File in CSV format into a Pandas DataFrame.

        :param filename: The desired File Name.

        :return: Pandas DataFrame containing Sensor Names and Data.
        """
        filename = r'Data/' + filename
        data_read = pd.read_csv(filename, header=90, index_col=0)

        return data_read

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

    sensor_list = ['Timestamp']
    if log: print("CSV_Handler - entered Select sensor Headers")
    if connected_module_list[0]:
        sensor_list.append('Sensor 1')
        sensor_list.append('Sensor 2')
        sensor_list.append('Sensor 3')
        sensor_list.append('Sensor 4')
    if connected_module_list[1]:
        sensor_list.append('Sensor 5')
        sensor_list.append('Sensor 6')
        sensor_list.append('Sensor 7')
        sensor_list.append('Sensor 8')
    if connected_module_list[2]:
        sensor_list.append('Sensor 9')
        sensor_list.append('Sensor 10')
        sensor_list.append('Sensor 11')
        sensor_list.append('Sensor 12')
    if connected_module_list[3]:
        sensor_list.append('Sensor 13')
        sensor_list.append('Sensor 14')
        sensor_list.append('Sensor 15')
        sensor_list.append('Sensor 16')
    if connected_module_list[4]:
        sensor_list.append('Sensor 17')
        sensor_list.append('Sensor 18')
        sensor_list.append('Sensor 19')
        sensor_list.append('Sensor 20')
    if connected_module_list[5]:
        sensor_list.append('Sensor 21')
        sensor_list.append('Sensor 22')
        sensor_list.append('Sensor 23')
        sensor_list.append('Sensor 24')
    if connected_module_list[6]:
        sensor_list.append('Sensor 25')
        sensor_list.append('Sensor 26')
        sensor_list.append('Sensor 27')
        sensor_list.append('Sensor 28')
    if connected_module_list[7]:
        sensor_list.append('Sensor 29')
        sensor_list.append('Sensor 30')
        sensor_list.append('Sensor 31')
        sensor_list.append('Sensor 32')
    if log: print("CSV_Handler - got out of Select sensor Headers")

    return sensor_list


def get_port():
    port = 'COM'
    for i in range(1, 20, 1):
        try:
            port = port[0:3] + str(i)
            if log: print("before port = ", port)
            ins = ins_man.instruction_manager(port)
            if log: print("port = ", port)
            del ins
            break
        except serial.serialutil.SerialException:
            port = 'COM-1'
            continue
    port = port.strip(' ')
    instruction_manager_port = port
    if log: print('com port connected is = ' + instruction_manager_port)

    return instruction_manager_port

# TESTING
sc1 = Sensor_Individual.Sensor('S1', 0)
sc2 = Sensor_Individual.Sensor('S2', 0)
sc3 = Sensor_Individual.Sensor('S3', 0)
sc4 = Sensor_Individual.Sensor('S4', 0)
dc = DAQ_Configuration.DAQconfigs()
cc = Module_Individual.Module('mName', sc1, sc2, sc3, sc4)
dh = Data_Handler([cc,cc,cc,cc,cc,cc,cc,cc], dc)

data = '1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4'
dh.store_data('Testing.csv', data)
