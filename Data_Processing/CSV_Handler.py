from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Control_Module_Comm import instruction_manager as ins_man
import GUI_Handler
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
            data.to_csv(datapath, mode='a', index=False)
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
        data_read = pd.read_csv(filename, header=90, index_col='Timestamp') # FIXME 'Timestamp' DOES NOT EXISTS IN STORE DATA YET.

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

    def request_all_data(self, connected_modules: []):
        """
        Gets data from Control Module and parses it into a single Pandas DataFrame.

        :param connected_modules: 1/0 List indicating connected modules.

        :return: Pandas DataFrame with joint module sensor data.
        """
        string = ''
        self.all_data = pd.DataFrame()
        for i in range(len(connected_modules)):
            if connected_modules[i]:
                string += ''  # String necessary here to connect inner and outer variables apperently.
                try:
                    im = ins_man.instruction_manager()
                    string = im.send_request_data(i)  # FIXME wait for Juan's Method Merge.
                except serial.SerialException:
                    GUI_Handler.show_error('Device has been Disconnected. <br>'
                                           ' Data Collection Aborted.')
                    break

                self.all_data.join(self.string_to_dataframe(string))

        # DataFrame to hold index and simulate timestamp. TODO
        timestamp = ''
        time = 0
        time_step = 1/GUI_Handler.daq_config.get_sampling_freq()
        for x in range(len(self.all_data.index)):
            time += time_step
            timestamp += str(time) + ';' # New line every timestamp calculated.

        timedf = self.string_to_dataframe(timestamp)

        return self.all_data

    def read_sensor_headers(self, filename: str):
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

    sensor_list = ['Timestamp']
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
# sc1 = Sensor_Individual.Sensor('S1', 0)
# sc2 = Sensor_Individual.Sensor('S2', 0)
# sc3 = Sensor_Individual.Sensor('S3', 0)
# sc4 = Sensor_Individual.Sensor('S4', 0)
# dc = DAQ_Configuration.DAQconfigs()
# cc = Module_Individual.Module('mName', sc1, sc2, sc3, sc4)
# dh = Data_Handler([cc,cc,cc,cc,cc,cc,cc,cc], dc)
# #
# # data = '1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4;1555879810,sens1,sens2,sens3,sens4'
# # # dh.store_data('Testing.csv', data)
# # print(dh.data_to_string('Testing.csv'))
# dh.read_sensor_headers('Testing.csv')