from Control_Module_Comm.Structures import Sensor_Individual as sens

class Module:
    def __init__(self, channel_name: str, sensor_1: sens, sensor_2: sens, sensor_3: sens, sensor_4: sens):

        self.channel_info = {
            'channel_name': channel_name,
            'Sensor 1': sensor_1,
            'Sensor 2': sensor_2,
            'Sensor 3': sensor_3,
            'Sensor 4': sensor_4
        }


# TESTING
# ch = Channel('mTestChannel')
# ch.channel_info['channel_name'] = 'mNewName'
# print(ch.channel_info['channel_name'])
