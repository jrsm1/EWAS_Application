from Window import Window
from Module_Info_Window import ModuleInformationWindow
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

# Global Variables
MODULE_1 = 0
MODULE_2 = 1
MODULE_3 = 2
MODULE_4 = 3
MODULE_5 = 4
MODULE_6 = 5
MODULE_7 = 6
MODULE_8 = 7

class ModuleSelectionWindow(Window):
    def __init__(self, modules: []):
        super().__init__()
        self.module_selection_win = uic.loadUi('GUI/Qt_Files/module_selection_window.ui')
        self.module_selection_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
        # self.init_objects()

        self.modules = modules

        # Select Module for Channel Info.
        self.mod_1_button = self.module_selection_win.module_selection_Module1
        self.mod_1_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_1]))

        self.mod_2_button = self.module_selection_win.module_selection_Module2
        self.mod_2_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_2]))

        self.mod_3_button = self.module_selection_win.module_selection_Module3
        self.mod_3_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_3]))

        self.mod_4_button = self.module_selection_win.module_selection_Module4
        self.mod_4_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_4]))

        self.mod_5_button = self.module_selection_win.module_selection_Module5
        self.mod_5_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_5]))

        self.mod_6_button = self.module_selection_win.module_selection_Module6
        self.mod_6_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_6]))

        self.mod_7_button = self.module_selection_win.module_selection_Module7
        self.mod_7_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_7]))

        self.mod_8_button = self.module_selection_win.module_selection_Module8
        self.mod_8_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_8]))

        self.module_button_list = [self.mod_1_button, self.mod_2_button, self.mod_3_button, self.mod_4_button,
                                   self.mod_5_button, self.mod_6_button, self.mod_7_button, self.mod_8_button]

        pass

    def open(self):
        """
        Opens Module Selection Window.
        Done before Channel Selection.
        """
        # Disable not connected modules.
        try:
            connected_modules = [1, 0, 1, 0, 0, 0, 0, 0]
            # im = ins_man.instruction_manager(ins_port)
            # connected_modules = im.send_request_number_of_mods_connected() # FIXME ENABLE FOR REAL
            self.disable_buttons(connected_modules)
            self.module_selection_win.show()
        except serial.SerialException:
            self.not_connected_error()

        pass

    def close(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """
        super().close()
        self.module_selection_win.close()

        pass

    def disable_buttons(self, connected_modules: []):
        """
        Disables not connected sensor buttons from Module Selection Window.

        :param connected_modules: List Containing each module state.
        """

        for val in range(8):
            if not connected_modules[val]:
                self.module_button_list[val].setEnabled(False)
                self.module_button_list[val].setStyleSheet('background-color:rgb(244, 166, 142);'
                                                           'color: rgb(255, 255, 255);'
                                                           'font: 12pt "MS Shell Dlg 2";')
        pass

    def show_channel_info_window(self, module: Module_Individual.Module):
        """
        Opens Channel Information Window based on module selection button press.

        :param module: The module list index [MODULE NAME - 1]
        """

        # LATER TODO SAVE CORRECT VALUES FOR CHANNEL.
        # TODO Pass or Receive in ModuleInformationWindow() the Module Number and Channel Names.

        # Close Mosule Selection Window now as it will not do anything. --> Open after module settings are saved.
        self.close()

        # Decide which Module the user has selected and create intances for each one.
        ModuleInformationWindow(module).open()

# HOLD UNTILL ALL TEST PASSED. IN CASE SIGNAL METHOD NEEDS TO BE CHANGED BACK TO THIS.
#         self.mod_1_button.clicked.connect(lambda: show_channel_info_window(0))
#         self.mod_2_button.clicked.connect(lambda: show_channel_info_window(1))
#         self.mod_3_button.clicked.connect(lambda: show_channel_info_window(2))
#         self.mod_4_button.clicked.connect(lambda: show_channel_info_window(3))
#         self.mod_5_button.clicked.connect(lambda: show_channel_info_window(4))
#         self.mod_6_button.clicked.connect(lambda: show_channel_info_window(5))
#         self.mod_7_button.clicked.connect(lambda: show_channel_info_window(6))
#         self.mod_8_button.clicked.connect(lambda: show_channel_info_window(7))