from PyQt5 import uic
from PyQt5.QtGui import QIcon

from Window import Window

class VizSensorSelector(Window):
    def __init__(self, visualization_values):
        super().__init__()

        self.viz_sensor_sel_win = uic.loadUi('GUI/Qt_Files/visualize_sensor_selection_dropdown.ui')
        self.viz_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
        # self.init_objects()

        self.visualization_values = visualization_values

        # Objects
        self.viz_name_label = self.viz_sensor_sel_win.plot_name_label
        self.viz_sens_1_dropdown = self.viz_sensor_sel_win.sensor_1_DropDown
        self.viz_sens_2_dropdown = self.viz_sensor_sel_win.sensor_2_DropDown

        # Signals
        self.viz_next_btn = self.viz_sensor_sel_win.NEXT_button.clicked.connect(lambda: self.viz.begin_visualization())

        pass

    def open(self):
        """
        Opens Visualization Window Selection if do_plot has been called before.
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

        :return:
        """

        pass

    def validate_visualize_sensor_selection(self, max_sensors: int):
        """
        Validates the user has selected a sensor to visualize.

        :param max_sensors: (1 or 2) Determines the validation Process.

        :return: True if User has selected al proper sensors.
        """
        validated = True
        if max_sensors == 1:
            if self.viz_sens_1_dropdown.currentIndex() == 0:  # if Default Value --> Not Validated.
                self.close()
                validated = False

        if max_sensors == 2:
            if self.viz_sens_1_dropdown.currentIndex() == 0:  # if Default Value --> Not Validated.
                self.close()
                validated = False
            if self.viz_sens_2_dropdown.currentIndex() != 0:
                self.close()
                validated = False

        return validated


    def init_object(self):
        """
        Abstract Class that every child MUST Implement.

        :return:
        """
        self.viz_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Objects
        self.viz_name_label = self.viz_sensor_sel_win.plot_name_label
        self.viz_sens_1_dropdown = self.viz_sensor_sel_win.sensor_1_DropDown
        self.viz_sens_2_dropdown = self.viz_sensor_sel_win.sensor_2_DropDown

        # Signals
        self.viz_next_btn = self.viz_sensor_sel_win.NEXT_button.clicked.connect(lambda: self.viz.begin_visualization())

        pass
