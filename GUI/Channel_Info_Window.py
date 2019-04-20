from Control_Module_Comm.Structures import Module_Individual as chan, Sensor_Individual as sens


def save_info():
    # Get info from GUI.
    # Set info to correct Data Structure.
    # Set sensor info (4)
    sens_1 = sens.Sensor('NAME', 'Sensor_1 description', 'sensitivity', 'where am i?')
    sens_2 = sens.Sensor('NAME', 'Sensor_2 description', 'sensitivity', 'where am i?')
    sens_3 = sens.Sensor('NAME', 'Sensor_3 description', 'sensitivity', 'where am i?')
    sens_4 = sens.Sensor('NAME', 'Sensor_4 description', 'sensitivity', 'where am i?')

    # Set channel sensors.
    channel = chan.Module('NAME', sens_1, sens_2, sens_3, sens_4)
