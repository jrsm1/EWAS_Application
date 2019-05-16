import serial
from PyQt5 import uic
from PyQt5.QtGui import QIcon

import GUI_Handler
from Window import Window
from Control_Module_Comm import instruction_manager as ins_man


# TESTING
log =1


class SensorSelectionMatrix(Window):
    def __init__(self):
        super().__init__()
        self.sensor_selection_matrix = uic.loadUi('GUI/Qt_Files/main_sensor_selection_matrix.ui')
        self.sensor_selection_matrix.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Instance Variables.
        self.all_selected = False

        # Objects
        # Sensor Checkboxes
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
        # self.sensor_selection_matrix.sensor_selection_DONE_Button.clicked.connect(lambda: GUI_Handler.action_begin_recording(self, GUI_Handler.start_diagnose_decision))
        self.sensor_selection_matrix.sensor_selection_DONE_Button.clicked.connect(lambda: self.validate_sensors_selected())
        self.sensor_selection_matrix.Select_all_sensors_button.clicked.connect(lambda: self.selection_all())
        # Uncheck Signals.
        self.win_sens_1.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_2.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_3.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_4.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_5.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_6.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_7.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_8.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_9.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_10.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_11.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_12.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_13.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_14.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_15.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_16.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_17.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_18.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_19.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_20.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_21.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_22.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_23.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_24.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_25.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_26.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_27.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_28.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_29.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_30.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_31.stateChanged.connect(lambda: self.set_select_all_false())
        self.win_sens_32.stateChanged.connect(lambda: self.set_select_all_false())

        pass

    def open(self):
        """
        Opens Sensor Selection Matrix Window for Recording and Diagnostics. [Does not create a new instance]
        """
        try:
            if self.enable_connected_sensors():
                self.sensor_selection_matrix.show()
            else:
                self.display_error('No Modules Connected.')
        except serial.SerialException:
            self.not_connected_error()

    def close(self):
        """
        Closes Sensor Selection Matrix Window
        """
        super().close()
        self.sensor_selection_matrix.close()
        pass

    def set_select_all_false(self):
        self.all_selected = False
        pass

    # TODO Implement. (called in line 72 (this is line 97 at moment of writing.))
    def validate_sensors_selected(self):
        """
        Validates user has selected at least one sensor before running experiment.

        :return: True if Validated
        """
        sensors, xmodules = self.get_modules_and_sensors_selected()
        # # Reset all Checkboxes.
        # for sensor_checkbox in self.sensor_selection_list:
        #     sensor_checkbox.setChecked(False)

        for sensor in sensors:
            if sensor == 1: # Any sensor has been selected --> Validate.
                GUI_Handler.action_begin_recording(self, GUI_Handler.start_diagnose_decision)
                return True

        return False

    def get_modules_and_sensors_selected(self):
        """
        Gets Sensors selected by user from sensor selection matrix.
        Also calculates the modules from the selected sensors.

        :return: '0000' # TODO Find out what this return is.
        """
        if log: print("Entered - get_modules_and_sensors_selected")

        sensors_selected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        modules_selected = set()

        index = 0
        for sensor_checkbox in self.sensor_selection_list:
            # Check if User has selected each checkBox.
            if sensor_checkbox.isChecked():
                sensors_selected[index] = 1
                module = int(index / 4) + 1
                modules_selected.add(module)
            # Increment Index
            index += 1

        if log: print("sensors selected are: ", sensors_selected)

        return sensors_selected, modules_selected

    def enable_connected_sensors(self):
        """
        Enables CheckBoxes on window after asking Control Module for connected modules.
        This Method ASUMES device connection is made and/or handled before calling enable_connected_sensors.

        :return: False if there are no sensors connected.
        """
        continuar = False

        # Get Connected Modules
        # connected_module_list = [1, 0, 0, 0, 0, 0, 0, 0]
        ins = ins_man.instruction_manager(GUI_Handler.ins_port)
        connected_module_list = ins.send_request_number_of_mods_connected()

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
        return continuar, connected_module_list

    def selection_all(self): # TODO TEST
        """
        Checks all enabled sensors.
        """
        if not self.all_selected:  # if not all sensors are selected.
            # Check All Enabled Sensors.
            for checkbox in self.sensor_selection_list:
                if checkbox.isEnabled():
                    checkbox.setChecked(True)
                # Change all selected status.
                self.all_selected = not self.all_selected
        else:
            # Un-Check All Sensors.
            for checkbox in self.sensor_selection_list:  # if all sensors are selected.
                checkbox.setChecked(False)

        pass
