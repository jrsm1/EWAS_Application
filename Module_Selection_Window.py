from PyQt5 import uic
from PyQt5.QtGui import QIcon

from Control_Module_Comm.Structures import Module_Individual
from Module_Info_Window import ModuleInformationWindow
from Window import Window
import GUI_Handler
from Control_Module_Comm import instruction_manager as ins_man

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
        # Module 1
        self.mod_1_button = self.module_selection_win.module_selection_Module1
        self.mod_1_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_1]))
        # Module 2
        self.mod_2_button = self.module_selection_win.module_selection_Module2
        self.mod_2_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_2]))
        # Module 3
        self.mod_3_button = self.module_selection_win.module_selection_Module3
        self.mod_3_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_3]))
        # Module 4
        self.mod_4_button = self.module_selection_win.module_selection_Module4
        self.mod_4_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_4]))
        # Module 5
        self.mod_5_button = self.module_selection_win.module_selection_Module5
        self.mod_5_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_5]))
        # Module 6
        self.mod_6_button = self.module_selection_win.module_selection_Module6
        self.mod_6_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_6]))
        # Module 7
        self.mod_7_button = self.module_selection_win.module_selection_Module7
        self.mod_7_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_7]))
        # Module 8
        self.mod_8_button = self.module_selection_win.module_selection_Module8
        self.mod_8_button.clicked.connect(lambda: self.show_channel_info_window(modules[MODULE_8]))

        self.module_button_list = [self.mod_1_button, self.mod_2_button, self.mod_3_button, self.mod_4_button,
                                   self.mod_5_button, self.mod_6_button, self.mod_7_button, self.mod_8_button]

        pass

    def open(self):
        """
        Opens Module Selection Window. [Does not create a new instance]
        Done before Channel Selection.
        """
        # Disable not connected modules.
        # connected_modules = [1, 0, 0, 0, 0, 0, 0, 0]
        im = ins_man.instruction_manager(GUI_Handler.ins_port)  # TODO TEST
        connected_modules = im.send_request_number_of_mods_connected()  # FIXME ENABLE FOR REAL
        self.disable_buttons(connected_modules)
        self.module_selection_win.show()

        pass

    def close(self):
        """
        Closes Module Selection Window.
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

        # Close Module Selection Window now as it will not do anything. --> Open after module settings are saved.
        self.close()

        # Decide which Module the user has selected and create intances for each one.
        ModuleInformationWindow(module).open()
