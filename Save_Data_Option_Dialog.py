from PyQt5 import uic
from PyQt5.QtGui import QIcon

from Control_Module_Comm.Structures import DAQ_Configuration
from Window import Window
import GUI_Handler


class SaveDataOptionDialog(Window):
    def __init__(self, daq_config: DAQ_Configuration):
        super().__init__()

        self.store_data_window = uic.loadUi("GUI/Qt_Files/store_data_dialog.ui")
        self.store_data_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
        # self.init_objects()

        self.daq_config = daq_config

        # Objects
        self.yes_button = self.store_data_window.store_data_yes_button.clicked.connect(lambda: GUI_Handler.sensor_matrix.open())
        self.no_button = self.store_data_window.store_data_no_button.clicked.connect(lambda: GUI_Handler.sensor_matrix.open())

        pass

    def open(self):
        """
        Opens Window offering the user the option os storing data in SD Card. [Does not create a new instance]
        """
        super().open()
        self.store_data_window.show()

        pass

    def close(self):
        """
        Opens Window offering the user the option os storing data in SD Card.
        """
        super().close()
        self.store_data_window.close()

        pass

    def set_store_data_SDcard(self, yes: str):
        """
        Sets Test Status to 'YES' save data or 'NO' do not store data in SD Card.
        :param yes: Decision made by user.
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
        GUI_Handler.sensor_matrix.open()

        pass
