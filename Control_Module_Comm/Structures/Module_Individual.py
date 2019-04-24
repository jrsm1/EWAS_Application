from Control_Module_Comm.Structures import Sensor_Individual as sens

class Module:
    def __init__(self, module_name: str, sensor_1: sens, sensor_2: sens, sensor_3: sens, sensor_4: sens):

        self.channel_info = {
            'channel_name': module_name,
            'Sensor 1': sensor_1,
            'Sensor 2': sensor_2,
            'Sensor 3': sensor_3,
            'Sensor 4': sensor_4
        }

        self.channel_gui_checkboxes = {

        }

        self.connected = False

    def set_Connected(self, connected: bool):
        self.connected = connected
        return connected

    def get_Connected(self):
        return self.connected


# TESTING
# ch = Channel('mTestChannel')
# ch.channel_info['channel_name'] = 'mNewName'
# print(ch.channel_info['channel_name'])
