from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon

from Window import Window

class VizSensorSelector(Window):
    def __init__(self, main_window_parent: QtWidgets, visualization_values):
        super().__init__()

        self.viz_sensor_sel_win = uic.loadUi('GUI/Qt_Files/visualize_sensor_selection_dropdown.ui')
        self.viz_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        self.visualization_values = visualization_values
        self.parent = main_window_parent
        self.number_of_sensors = 0

        # Objects
        self.viz_name_label = self.viz_sensor_sel_win.plot_name_label
        self.viz_sens_1_dropdown = self.viz_sensor_sel_win.sensor_1_DropDown
        self.viz_sens_2_dropdown = self.viz_sensor_sel_win.sensor_2_DropDown

        # Signals
        self.viz_next_btn = self.viz_sensor_sel_win.NEXT_button.clicked.connect(lambda: self.parent.begin_visualization())

        pass

    def open(self):
        """
        Opens Visualization Window Selection if do_plot has been called before. [Does not create a new instance]
        If it happens raise an error. (SHOULD NEVER BE THE CASE. REDUNDANCY)
        """
        super().open()
        if (self.visualization_values['requested_plot'] != 0) and (self.visualization_values['plot_filename'] != ''):
            self.viz_sensor_sel_win.show()
        else:
            self.display_error('Requested Plot Error. <br> ErrorCode: 0000')  # TODO do not hardcode Error Codes.

        pass

    def close(self):
        """
        Closes Sensor Selection Matrix Window.
        """
        self.viz_sensor_sel_win.close()

        pass

    def validate_visualize_sensor_selection(self, max_sensors: int):
        """
        Validates the user has selected a sensor to visualize.

        :param max_sensors: (1 or 2) Determines the validation Process.

        :return: True if User has selected al proper sensors.
        """
        validated = True
        if max_sensors == 2:
            if self.viz_sens_1_dropdown.currentIndex() == 0:  # if Default Value --> Not Validated.
                validated = False
            if self.viz_sens_2_dropdown.currentIndex() == 0:
                validated = False

        if max_sensors == 1:
            if self.viz_sens_1_dropdown.currentIndex() == 0:  # if Default Value --> Not Validated.
                validated = False
        self.close()
        return validated

    def set_number_sensors(self, amount: int):
        self.number_of_sensors = amount

    def get_number_sensors(self):
        return self.number_of_sensors
