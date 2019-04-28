from Window import Window
from Sensor_Selection_Matrix import SensorSelectionMatrix
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


class SaveDataOptionDialog(Window):
    def __init__(self, daq_config: DAQ_Configuration):
        super().__init__()

        self.store_data_window = uic.loadUi("GUI/Qt_Files/store_data_dialog.ui")
        self.store_data_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
        # self.init_objects()

        self.daq_config = daq_config

        # Objects
        self.yes_button = self.store_data_window.store_data_yes_button.clicked.connect(lambda: self.store_data('yes'))
        self.no_button = self.store_data_window.store_data_no_button.clicked.connect(lambda: self.store_data('no'))

        pass

    def open(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """

        pass

    def close(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """

        pass

    def store_data(self, yes: str):
        """

        :param yes:
        :return:
        """
        self.store_data_window.close()
        if yes:
            self.daq_config.data_handling_configs["store"] = '1111'
        else:
            self.daq_config.data_handling_configs["store"] = '0000'
        self.ask_for_sensors()

        pass

    def ask_for_sensors(self):
        """
        Asks user for desired sensors to "turn on" based on connected Modules

        CALL BEFORE SENDING REQUEST TO START.
        """
        # User Select which sensors it wants.
        sensor_selection = SensorSelectionMatrix()
        sensor_selection.open()
        # When Done pressed --> begin recording. | this is handled from UI

        pass

    def save_into_dictionaries(self):
        """

        :return:
        """

        pass

    def init_object(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """
        self.store_data_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Objects
        self.yes_button = self.store_data_window.store_data_yes_button.clicked.connect(lambda: self.store_data('yes'))
        self.no_button = self.store_data_window.store_data_no_button.clicked.connect(lambda: self.store_data('no'))

        pass

