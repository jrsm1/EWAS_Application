import GUI_Handler
from Window import Window
from Data_Processing import CSV_Handler
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
import Exceptions
from time import sleep
import sys
import serial

from Data_Processing import CSV_Handler as csv_handler
from Control_Module_Comm import instruction_manager as ins_man
from Control_Module_Comm.Structures import Module_Individual as Chan, Sensor_Individual as sens
from Data_Processing import Plot_Data
from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Settings import setting_data_manager as set_dat_man
from regex import regex

# Global Variables.

# Testing
log =1

class ModuleInformationWindow(Window):
    def __init__(self, module: Module_Individual.Module):
        super().__init__()
        self.module_info_win = uic.loadUi("GUI/Qt_Files/module_1_info_window.ui")
        self.module_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
        # self.init_objects()

        self.module = module

        # Objects
        self.chan_mod_name = self.module_info_win.channel_info_module_name
        # Ch 1
        self.sensor_1_sensitivity = self.module_info_win.channel_info_sensor1_Sensitivity_LineEdit
        self.sensor_1_damping = self.module_info_win.channel_info_sensor1_dampingLineEdit
        self.sensor_1_bandwidth = self.module_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
        self.sensor_1_fullscale = self.module_info_win.channel_info_sensor1_full_Scale_LineEdit
        self.sensor_1_location = self.module_info_win.channel_info_sensor1_location_Edit
        self.sensor_1_name = self.module_info_win.channel_info_sensor1_nameLineEdit
        self.module_info_win.channel_info_sensor1_TITLE.setText(module.channel_info['Sensor 1'].sensor_info['sensor_name'])
        self.sensor_1_type = self.module_info_win.channel_info_sensor1_type_DropDown
        # Ch 2
        self.sensor_2_damping = self.module_info_win.channel_info_sensor2_dampingLineEdit
        self.sensor_2_bandwidth = self.module_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
        self.sensor_2_sensitivity = self.module_info_win.channel_info_sensor2_Sensitivity_LineEdit
        self.sensor_2_name = self.module_info_win.channel_info_sensor2_nameLineEdit
        self.sensor_2_type = self.module_info_win.channel_info_sensor2_type_DropDown
        self.module_info_win.channel_info_sensor2_TITLE.setText(module.channel_info['Sensor 2'].sensor_info['sensor_name'])
        self.sensor_2_location = self.module_info_win.channel_info_sensor2_location_Edit
        self.sensor_2_fullscale = self.module_info_win.channel_info_sensor2_full_Scale_LineEdit
        # Ch 3
        self.sensor_3_name = self.module_info_win.channel_info_sensor3_nameLineEdit
        self.sensor_3_type = self.module_info_win.channel_info_sensor3_type_DropDown
        self.sensor_3_sensitivity = self.module_info_win.channel_info_sensor3_Sensitivity_LineEdit
        self.sensor_3_bandwidth = self.module_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
        self.sensor_3_fullscale = self.module_info_win.channel_info_sensor3_full_scale_LineEdit
        self.sensor_3_damping = self.module_info_win.channel_info_sensor3_dampingLineEdit
        self.sensor_3_location = self.module_info_win.channel_info_sensor3_location_Edit
        self.module_info_win.channel_info_sensor3_TITLE.setText(module.channel_info['Sensor 3'].sensor_info['sensor_name'])
        # Ch 4
        self.sensor_4_name = self.module_info_win.channel_info_sensor4_nameLineEdit
        self.sensor_4_type = self.module_info_win.channel_info_sensor4_type_DropDown
        self.sensor_4_sensitivity = self.module_info_win.channel_info_sensor4_Sensitivity_LineEdit
        self.sensor_4_bandwidth = self.module_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
        self.sensor_4_fullscale = self.module_info_win.channel_info_senson4_full_Scale_LineEdit
        self.sensor_4_location = self.module_info_win.channel_info_sensor4_location_Edit
        self.sensor_4_damping = self.module_info_win.channel_info_sensor4_dampingLineEdit
        self.module_info_win.channel_info_sensor4_TITLE.setText(module.channel_info['Sensor 4'].sensor_info['sensor_name'])

        # Signals
        self.module_info_win.channel_info_SAVE_Button.clicked.connect(lambda: self.save_module_info(self.module))

        pass

    def open(self):
        """

        :return:
        """
        super().open()
        self.module_info_win.show()

        pass

    def close(self):
        """

        :return:
        """
        super().close()
        self.module_info_win.close()

        pass

    def save_module_info(self, module: Module_Individual.Module):
        """
        
        :return: New Module with window info. 
        """
        # Get info from GUI.
        try:
            if log: print("entered enable start")
            sensor_1 = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                sensor_type=self.sensor_1_type.currentIndex(),
                                                sensor_sensitivity=str(self.sensor_1_sensitivity.text()),
                                                sensor_bandwidth=str(self.sensor_1_bandwidth.text()),
                                                sensor_full_scale=str(self.sensor_1_fullscale.text()),
                                                sensor_damping=str(self.sensor_1_damping.text()),
                                                sensor_localization=str(self.sensor_1_location.toPlainText()))
            sensor_2 = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                sensor_type=self.sensor_2_type.currentIndex(),
                                                sensor_sensitivity=str(self.sensor_2_sensitivity.text()),
                                                sensor_bandwidth=str(self.sensor_2_bandwidth.text()),
                                                sensor_full_scale=str(self.sensor_2_fullscale.text()),
                                                sensor_damping=str(self.sensor_2_damping.text()),
                                                sensor_localization=str(self.sensor_2_location.toPlainText()))

            sensor_3 = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                sensor_type=self.sensor_3_type.currentIndex(),
                                                sensor_sensitivity=str(self.sensor_3_sensitivity.text()),
                                                sensor_bandwidth=str(self.sensor_3_bandwidth.text()),
                                                sensor_full_scale=str(self.sensor_3_fullscale.text()),
                                                sensor_damping=str(self.sensor_3_damping.text()),
                                                sensor_localization=str(self.sensor_3_location.toPlainText()))

            sensor_4 = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                sensor_type=self.sensor_4_type.currentIndex(),
                                                sensor_sensitivity=str(self.sensor_4_sensitivity.text()),
                                                sensor_bandwidth=str(self.sensor_4_bandwidth.text()),
                                                sensor_full_scale=str(self.sensor_4_fullscale.text()),
                                                sensor_damping=str(self.sensor_4_damping.text()),
                                                sensor_localization=str(self.sensor_4_location.toPlainText()))

            self.module.channel_info['Sensor 1'] = sensor_1
            self.module.channel_info['Sensor 2'] = sensor_2
            self.module.channel_info['Sensor 3'] = sensor_3
            self.module.channel_info['Sensor 4'] = sensor_4
            if log: print("got out of enable start connected sensors")
        except serial.SerialException:
            self.not_connected_error(self)
            
        return self.module

    def action_store_module_info(self, module: Module_Individual.Module):
        """

        :return:
        """

        pass

    def action_load_module_info(self):
        """

        :return:
        """

        pass

    # def init_objects(self):
    #     """
    #     Abstract Class that every child MUST Implement.
    #
    #     :return:
    #     """
    #     self.module_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
    #
    #     # Objects
    #     self.chan_mod_name = self.module_info_win.channel_info_module_name
    #     # Ch 1
    #     self.sensor_1_sensitivity = self.module_info_win.channel_info_sensor1_Sensitivity_LineEdit
    #     self.sensor_1_damping = self.module_info_win.channel_info_sensor1_dampingLineEdit
    #     self.sensor_1_bandwidth = self.module_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
    #     self.sensor_1_fullscale = self.module_info_win.channel_info_sensor1_full_Scale_LineEdit
    #     self.sensor_1_location = self.module_info_win.channel_info_sensor1_location_Edit
    #     self.sensor_1_name = self.module_info_win.channel_info_sensor1_nameLineEdit
    #     self.module_info_win.channel_info_sensor1_TITLE
    #     self.sensor_1_type = self.module_info_win.channel_info_sensor1_type_DropDown
    #     # Ch 2
    #     self.sensor_2_damping = self.module_info_win.channel_info_sensor2_dampingLineEdit
    #     self.sensor_2_bandwidth = self.module_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
    #     self.sensor_2_sensitivity = self.module_info_win.channel_info_sensor2_Sensitivity_LineEdit
    #     self.sensor_2_name = self.module_info_win.channel_info_sensor2_nameLineEdit
    #     self.sensor_2_type = self.module_info_win.channel_info_sensor2_type_DropDown
    #     self.module_info_win.channel_info_sensor2_TITLE
    #     self.sensor_2_location = self.module_info_win.channel_info_sensor2_location_Edit
    #     self.sensor_2_fullscale = self.module_info_win.channel_info_sensor2_full_Scale_LineEdit
    #     # Ch 3
    #     self.sensor_3_name = self.module_info_win.channel_info_sensor3_nameLineEdit
    #     self.sensor_3_type = self.module_info_win.channel_info_sensor3_type_DropDown
    #     self.sensor_3_sensitivity = self.module_info_win.channel_info_sensor3_Sensitivity_LineEdit
    #     self.sensor_3_bandwidth = self.module_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
    #     self.sensor_3_fullscale = self.module_info_win.channel_info_sensor3_full_scale_LineEdit
    #     self.sensor_3_damping = self.module_info_win.channel_info_sensor3_dampingLineEdit
    #     self.sensor_3_location = self.module_info_win.channel_info_sensor3_location_Edit
    #     self.module_info_win.channel_info_sensor3_TITLE
    #     # Ch 4
    #     self.sensor_4_name = self.module_info_win.channel_info_sensor4_nameLineEdit
    #     self.sensor_4_type = self.module_info_win.channel_info_sensor4_type_DropDown
    #     self.sensor_4_sensitivity = self.module_info_win.channel_info_sensor4_Sensitivity_LineEdit
    #     self.sensor_4_bandwidth = self.module_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
    #     self.sensor_4_fullscale = self.module_info_win.channel_info_senson4_full_Scale_LineEdit
    #     self.sensor_4_location = self.module_info_win.channel_info_sensor4_location_Edit
    #     self.sensor_4_damping = self.module_info_win.channel_info_sensor4_dampingLineEdit
    #     self.module_info_win.channel_info_sensor4_TITLE
    #
    #     # Signals
    #     self.module_info_win.channel_info_SAVE_Button.clicked.connect(lambda: self.save_module_info())
    #
    #     pass
