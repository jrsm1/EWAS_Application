import serial
from PyQt5 import uic
from PyQt5.QtGui import QIcon

import GUI_Handler
from Window import Window

# TESTING
log =1


class SensorSelectionMatrix(Window):
    def __init__(self):
        super().__init__()
        self.sensor_selection_matrix = uic.loadUi('GUI/Qt_Files/main_sensor_selection_matrix.ui')
        self.sensor_selection_matrix.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Objects
        self.sensor_selection_matrix.sensor_select_MAX_Label
        self.win_sens_1 = self.sensor_selection_matrix.Sensor_1
        self.win_sens_2 = self.sensor_selection_matrix.Sensor_2
        self.win_sens_3 = self.sensor_selection_matrix.Sensor_3
        self.win_sens_4 = self.sensor_selection_matrix.Sensor_4
        self.win_sens_5 = self.sensor_selection_matrix.Sensor_5
        self.win_sens_6 = self.sensor_selection_matrix.Sensor_6
        self.win_sens_7 = self.sensor_selection_matrix.Sensor_7
        self.win_sens_8 = self.sensor_selection_matrix.Sensor_8
        self.win_sens_9 = self.sensor_selection_matrix.Sensor_9
        self.win_sens_10 = self.sensor_selection_matrix.Sensor_10
        self.win_sens_11 = self.sensor_selection_matrix.Sensor_11
        self.win_sens_12 = self.sensor_selection_matrix.Sensor_12
        self.win_sens_13 = self.sensor_selection_matrix.Sensor_13
        self.win_sens_14 = self.sensor_selection_matrix.Sensor_14
        self.win_sens_15 = self.sensor_selection_matrix.Sensor_15
        self.win_sens_16 = self.sensor_selection_matrix.Sensor_16
        self.win_sens_17 = self.sensor_selection_matrix.Sensor_17
        self.win_sens_18 = self.sensor_selection_matrix.Sensor_18
        self.win_sens_19 = self.sensor_selection_matrix.Sensor_19
        self.win_sens_20 = self.sensor_selection_matrix.Sensor_20
        self.win_sens_21 = self.sensor_selection_matrix.Sensor_21
        self.win_sens_22 = self.sensor_selection_matrix.Sensor_22
        self.win_sens_23 = self.sensor_selection_matrix.Sensor_23
        self.win_sens_24 = self.sensor_selection_matrix.Sensor_24
        self.win_sens_25 = self.sensor_selection_matrix.Sensor_25
        self.win_sens_26 = self.sensor_selection_matrix.Sensor_26
        self.win_sens_27 = self.sensor_selection_matrix.Sensor_27
        self.win_sens_28 = self.sensor_selection_matrix.Sensor_28
        self.win_sens_29 = self.sensor_selection_matrix.Sensor_29
        self.win_sens_30 = self.sensor_selection_matrix.Sensor_30
        self.win_sens_31 = self.sensor_selection_matrix.Sensor_31
        self.win_sens_32 = self.sensor_selection_matrix.Sensor_32
        # List Used to get values easily (goes from 0 to 31)
        self.sensor_selection_list = [self.win_sens_1, self.win_sens_2, self.win_sens_3,
                                      self.win_sens_4, self.win_sens_5, self.win_sens_6,
                                      self.win_sens_7, self.win_sens_8, self.win_sens_9,
                                      self.win_sens_10, self.win_sens_11, self.win_sens_12,
                                      self.win_sens_13, self.win_sens_14, self.win_sens_15,
                                      self.win_sens_16, self.win_sens_17, self.win_sens_18,
                                      self.win_sens_19, self.win_sens_20, self.win_sens_21,
                                      self.win_sens_22, self.win_sens_23, self.win_sens_24,
                                      self.win_sens_25, self.win_sens_26, self.win_sens_27,
                                      self.win_sens_28, self.win_sens_29,  self.win_sens_30,
                                      self.win_sens_31, self.win_sens_32]

        # Signals
        self.sensor_selection_matrix.sensor_selection_DONE_Button.clicked.connect(
            lambda: GUI_Handler.action_begin_recording(GUI_Handler.start_diagnose_decision))

        pass

    def open(self):
        """
        Opens Sensor Selection Matrix Window for Recording and Diagnostics.

        :return:
        """
        try:
            if self.enable_connected_sensors():
                self.sensor_selection_matrix.show()
            else:
                self.display_error('No Modules Connected.')
        except serial.SerialException:
            self.not_connected_error()
        pass

    def close(self):
        """
        Closes Sensor Selection Matrix Window

        :return:
        """
        super().close()
        self.sensor_selection_matrix.close()
        pass

    def get_modules_and_sensors_selected(self):
        """
        Gets Sensors selected by user from sensor selection matrix.
        Also calculates the modules from the selected sensors.

        :return: '0000' # TODO Find out what this return is.
        """
        if log: print("entered get_module_and_sensors_selected()")
        sensors_sel = []
        if log: print("created empty sensor selected array")
        sensors_sel.append(self.sensor_selection_matrix.Sensor_1)
        if log:
            print("print sensors array created correctly")
        sensors_selected = "0000"
        correct = 1
        index = 0
        modules_selected = set()
        for i in self.sensor_selection_list:
            index += 1
            if i.checkState() == 2:
                module = str(int((index - 1) / 4) + 1)
                sensor = str(((index - 1) % 4) + 1)
                sensors_selected = module + sensor + sensors_selected
                modules_selected.add(module)

        if log: print("sensors selected are: ", sensors_selected)

        for i in self.sensor_selection_list:
            i.setCheckState(False)
        if correct:
            sensors_selected = sensors_selected[0:4]
            return sensors_selected
        return "0000"

        pass
    
    def enable_connected_sensors(self):
        """
        Enables CheckBoxes on window after asking Control Module for connected modules.
        This Method ASUMES device connection is made and/or handled before calling enable_connected_sensors.

        :return: False if there are no sensors connected.
        """
        # TODO TEST
        continuar = False
        connected_module_list = [1, 0, 0, 0, 0, 0, 0, 0]
        # ins = ins_man.instruction_manager(ins_port)  # TODO UNCOMMENT FOR REAL
        # connected_module_list = connected_module_listins.send_request_number_of_mods_connected()
        if log: print("entered enable start, array is " + str(connected_module_list))
        if connected_module_list[0]:
            self.win_sens_1.setEnabled(True)
            self.win_sens_2.setEnabled(True)
            self.win_sens_3.setEnabled(True)
            self.win_sens_4.setEnabled(True)
            continuar = True
        if connected_module_list[1]:
            self.win_sens_5.setEnabled(True)
            self.win_sens_6.setEnabled(True)
            self.win_sens_7.setEnabled(True)
            self.win_sens_8.setEnabled(True)
            continuar = True
        if connected_module_list[2]:
            self.win_sens_9.setEnabled(True)
            self.win_sens_10.setEnabled(True)
            self.win_sens_11.setEnabled(True)
            self.win_sens_12.setEnabled(True)
            continuar = True
        if connected_module_list[3]:
            self.win_sens_13.setEnabled(True)
            self.win_sens_14.setEnabled(True)
            self.win_sens_15.setEnabled(True)
            self.win_sens_16.setEnabled(True)
            continuar = True
        if connected_module_list[4]:
            self.win_sens_17.setEnabled(True)
            self.win_sens_18.setEnabled(True)
            self.win_sens_19.setEnabled(True)
            self.win_sens_20.setEnabled(True)
            continuar = True
        if connected_module_list[5]:
            self.win_sens_21.setEnabled(True)
            self.win_sens_22.setEnabled(True)
            self.win_sens_23.setEnabled(True)
            self.win_sens_24.setEnabled(True)
            continuar = True
        if connected_module_list[6]:
            self.win_sens_25.setEnabled(True)
            self.win_sens_26.setEnabled(True)
            self.win_sens_27.setEnabled(True)
            self.win_sens_28.setEnabled(True)
            continuar = True
        if connected_module_list[7]:
            self.win_sens_29.setEnabled(True)
            self.win_sens_30.setEnabled(True)
            self.win_sens_31.setEnabled(True)
            self.win_sens_32.setEnabled(True)
            continuar = True
        if log: print("got out of enable start connected sensors")

        # If not Connected to not continue.
        return continuar
