from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QDesktopWidget

import GUI_Handler
import Window
from Control_Module_Comm.Structures import DAQ_Configuration
from Data_Processing import CSV_Handler
from Data_Processing import Plot_Data
from FileName_Input_Window import FileInputWindow
from Module_Selection_Window import ModuleSelectionWindow as ModuleSelect
from Settings import setting_data_manager as set_dat_man
from Visualization_Sensor_Selection_Dialog import VizSensorSelector
from Window import Window as windowClass


# Global Variables.
app = QtWidgets.QApplication([])
STORE_LOAD_RECORDING_SETTINGS = 1
STORE_LOAD_LOCATION = 2
STORE_LOAD_DAQ_PARAMS = 3
STORE_LOAD_MODULE_INFO = 4
ACTION_LOAD = 'load'
ACTION_SAVE = 'save'
MAX_DURATION = {  # Max allowed Duration in seconds
    '2 Hz': 1800,
    '4 Hz': 1800,
    '8 Hz': 1800,
    '16 Hz': 1800,
    '32 Hz': 1800,
    '64 Hz': 1800,
    '128 Hz': 1365,
    '256 Hz': 682,
    '512 Hz': 341,
    '1024 Hz': 170,
    '2048 Hz': 85,
    '4096 Hz': 42,
    '8192 Hz': 21,
    '16384 Hz': 10,
    '20000 Hz': 8,
    'Please Select': -1}
MIN_DURATION = 5  # Min allowed Duration in seconds
TIME_PLOT = 1
FREQ_PLOT = 2
APS_PLOT = 3
CPS_PLOT = 4
COHERENCE_PLOT = 5
PHASE_PLOT = 6
visualization_values = {'requested_plot': 0,
                        'plot_filename': ''} # Variable to know which method called the plot signal after Visualization Sensor Selection Window NEXT called.

# Regex expressions
regex_description = QRegExpValidator(QRegExp('[a-zA-Z0-9-]+'))
regex_duration = QIntValidator(5, 1800)
regex_hour = QIntValidator(0, 23)
regex_delay = QIntValidator(0, 3600)
regex_minute_second = QIntValidator(0, 59)
regex_longitude = QRegExpValidator(QRegExp('^(\+|-)\d{5}(\.)\d{5}$'))
regex_latitude = QRegExpValidator(QRegExp('^(\+|-)\d{4}(\.)\d{5}$'))

# ToolTip Messages
toolTip_description = 'Restricted to lower-case letters, upper-case letters, numbers and dashes'
toolTip_duration = 'Restricted to positive integers with a minimum of 5 seconds up to 1800 seconds'
toolTip_Delay = 'Restricted to positive integers including 0 up to a maximum of 3600 seconds(1 hour)'
toolTip_Longitude = 'Restricted to NMEA format of (+/-)Dddmm.mmmmm'
toolTip_Latitude = 'Restricted to NMEA format of (+/-)ddmm.mmmmm'
toolTip_time = 'Restricted to 24-hour format'

# Testing
log = 1


class MainWindow(windowClass):
    def __init__(self, setting_manager: set_dat_man, daq_configuration: DAQ_Configuration, modules: []):
        super().__init__()
        self.main_window = uic.loadUi("GUI/Qt_Files/main_window.ui")
        self.main_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Init Window Object
        self.filename_input_win = FileInputWindow(self)
        self.setting_manager = setting_manager
        self.center()
        # Instance Parameters
        self.load_save_instructions = {
            'action': '',
            'who_to_save': 0,
            'who_to_load': 0
        }
        self.daq_config = daq_configuration

        # -------------------------------------------  Objects  --------------------------------------------------------
        # RECORDING  Settings
        self.rec_name_edit = self.main_window.main_tab_RecordingSettings_name_LineEdit
        self.rec_duration_edit = self.main_window.main_tab_RecordingSettings_durationLineEdit
        self.rec_type_dropdown = self.main_window.main_tab_RecordingSettings_type_DropDown
        self.delay_edit = self.main_window.main_tab_RecordingSettings_delay_LineEdit

        # Localization Settings
        self.loc_type_dropdown = self.main_window.main_tab_LocalizationSettings_type_DropBox
        self.loc_name_edit = self.main_window.main_tab_LocalizationSettings_Name_lineEdit
        self.loc_longitude_edit = self.main_window.main_tab_LocalizationSettings_longitudLineEdit
        self.loc_latitude_edit = self.main_window.main_tab_LocalizationSettings_latitudLineEdit
        self.loc_hour_edit = self.main_window.main_tab_LocalizationSettings_hourLineEdit
        self.loc_minute_edit = self.main_window.main_tab_LocalizationSettings_minutesLineEdit
        self.loc_seconds_edit = self.main_window.main_tab_LocalizationSettings_secondsLineEdit

        # Localization Frames
        self.loc_gps_frame = self.main_window.main_tab_location_gps_frame
        self.loc_specimen_frame = self.main_window.specimen_location_frame

        # Module Loc. Settings
        self.specimen_loc_1 = self.main_window.main_tab_module_loc_LineEdit_1
        self.specimen_loc_2 = self.main_window.main_tab_module_loc_LineEdit_2
        self.specimen_loc_3 = self.main_window.main_tab_module_loc_LineEdit_3
        self.specimen_loc_4 = self.main_window.main_tab_module_loc_LineEdit_4
        self.specimen_loc_5 = self.main_window.main_tab_module_loc_LineEdit_5
        self.specimen_loc_6 = self.main_window.main_tab_module_loc_LineEdit_6
        self.specimen_loc_7 = self.main_window.main_tab_module_loc_LineEdit_7
        self.specimen_loc_8 = self.main_window.main_tab_module_loc_LineEdit_8

        # Data Acquisition Settings
        self.samfreq_dropdown = self.main_window.main_tab_DAQParams_samplingRate_DropDown
        self.cutfreq_drodown = self.main_window.main_tab_DAQParams_Cutoff_Frequency_DropDown
        self.gain_dropdown = self.main_window.main_tab_DAQParams_gain_DropDown

        # -------------------------------------------------------- Signals ---------------------------------------------
        # Menu Bar
        self.main_window.action_Help.triggered.connect(lambda: self.open_documentation())
        self.main_window.actionDiagnose.triggered.connect(lambda: GUI_Handler.check_for_port('DIAGNOSE'))  # TODO VErify if this is part of Start Logic

        # Recording Settings
        self.rec_duration_edit.textEdited.connect(lambda: self.check_sampling_rate())
        self.main_window.main_tab_RecordingSettings_LOAD_SETTINGS_Button.clicked.connect(lambda: self.handle_storing_loading(ACTION_LOAD, 1))
        self.main_window.main_tab_RecordingSettings__SAVE_button.clicked.connect(lambda: self.handle_storing_loading(ACTION_SAVE, STORE_LOAD_RECORDING_SETTINGS))

        # Localization
        self.loc_type_dropdown.currentIndexChanged.connect(lambda: self.change_local_allowed())
        self.main_window.main_tab_LocalizationSettings_acquire_GPS_Button.clicked.connect(lambda: GUI_Handler.check_for_port('GPS'))
        self.main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button.clicked.connect(lambda: self.handle_storing_loading(ACTION_LOAD, STORE_LOAD_LOCATION))
        self.main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button.clicked.connect(lambda: self.handle_storing_loading(ACTION_SAVE, STORE_LOAD_LOCATION))

        # DAQ Params
        self.main_window.main_tab_DAQParams_LOAD_PARAMS_button.clicked.connect(lambda: self.handle_storing_loading(ACTION_LOAD, STORE_LOAD_DAQ_PARAMS))
        self.main_window.main_tab_DAQParams_SAVE_PARAMS_button.clicked.connect(lambda: self.handle_storing_loading(ACTION_SAVE, STORE_LOAD_DAQ_PARAMS))  # TODO
        self.cutfreq_drodown.currentIndexChanged.connect(lambda: self.suggest_sampling_rate())
        self.samfreq_dropdown.currentIndexChanged.connect(lambda: self.check_duration())

        # START
        self.main_window.main_tab_CHANNEL_INFO_button.clicked.connect(lambda: ModuleSelect(modules).open())
        self.main_window.main_tab_START_button.clicked.connect(lambda: GUI_Handler.check_for_port('START'))

        # Visualization
        self.main_window.actionTime.triggered.connect(lambda: self.do_plot(TIME_PLOT))
        self.main_window.actionFrequency.triggered.connect(lambda: self.do_plot(FREQ_PLOT))
        self.main_window.actionAuto_Power.triggered.connect(lambda: self.do_plot(APS_PLOT))
        self.main_window.actionCross_Power.triggered.connect(lambda: self.do_plot(CPS_PLOT))
        self.main_window.actionCoherence.triggered.connect(lambda: self.do_plot(COHERENCE_PLOT))

        # Regex Validation
        self.rec_name_edit.setValidator(regex_description)
        self.rec_duration_edit.setValidator(regex_duration)
        self.delay_edit.setValidator(regex_delay)
        self.loc_name_edit.setValidator(regex_description)
        self.loc_longitude_edit.setValidator(regex_longitude)
        self.loc_latitude_edit.setValidator(regex_latitude)
        self.loc_hour_edit.setValidator(regex_hour)
        self.loc_minute_edit.setValidator(regex_minute_second)
        self.loc_seconds_edit.setValidator(regex_minute_second)
        self.specimen_loc_1.setValidator(regex_description)
        self.specimen_loc_2.setValidator(regex_description)
        self.specimen_loc_3.setValidator(regex_description)
        self.specimen_loc_4.setValidator(regex_description)
        self.specimen_loc_5.setValidator(regex_description)
        self.specimen_loc_6.setValidator(regex_description)
        self.specimen_loc_7.setValidator(regex_description)
        self.specimen_loc_8.setValidator(regex_description)

        # Tool Tips
        self.rec_name_edit.setToolTip(toolTip_description)
        self.rec_duration_edit.setToolTip(toolTip_duration)
        self.delay_edit.setToolTip(toolTip_Delay)
        self.loc_name_edit.setToolTip(toolTip_description)
        self.loc_longitude_edit.setToolTip(toolTip_Longitude)
        self.loc_latitude_edit.setToolTip(toolTip_Latitude)
        self.loc_hour_edit.setToolTip(toolTip_time)
        self.loc_minute_edit.setToolTip(toolTip_time)
        self.loc_seconds_edit.setToolTip(toolTip_time)
        self.specimen_loc_1.setToolTip(toolTip_description)
        self.specimen_loc_2.setToolTip(toolTip_description)
        self.specimen_loc_3.setToolTip(toolTip_description)
        self.specimen_loc_4.setToolTip(toolTip_description)
        self.specimen_loc_5.setToolTip(toolTip_description)
        self.specimen_loc_6.setToolTip(toolTip_description)
        self.specimen_loc_7.setToolTip(toolTip_description)
        self.specimen_loc_8.setToolTip(toolTip_description)

        pass

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def open(self):
        """
        Opens Main Window. [Does not create a new instance]
        """
        self.main_window.show()
        pass

    def close(self):
        """
        Closes Main Window
        """
        self.main_window.close()
        pass

    def open_documentation(self):
        """
        Opens documentation web page in default browser.
        """
        url = QtCore.QUrl('https://github.com/jrsm1/EWAS_Application/blob/master/README.md')
        if not QtGui.QDesktopServices.openUrl(url):
            super().display_error('Could not open Help URL')

        pass


    # ********************************************* LOCATION ***********************************************************

    # ********************************* ACTIONS STORE/LOAD **************************************
    def handle_storing_loading(self, what: str, who: int):
        """
        Handles Logic for Storing/Loading Test Parameters.
        Prepares the logic that decides the desired loading/saving action.
        This Method contains information gathered from the user button press.

        :param what: Storing or loading?
        :param who: Desired Window parameters to Store/Load
        """

        self.load_save_instructions['action'] = what
        if (who == 0) or (what == ''):
            self.display_error('There has been an ERROR knowing what you want to do. Please Try Again.')
            if log: print('Loading Error.')
        else:
            if what == ACTION_SAVE:
                self.load_save_instructions['who_to_save'] = who
                self.filename_input_win.open()
            elif what == ACTION_LOAD:
                self.load_save_instructions['who_to_load'] = who
                self.do_saving_loading_action()

    def do_saving_loading_action(self):
        """
        Function continues to correct method depending on saving/loading and option combinations.
        """
        if self.load_save_instructions['action'] == ACTION_SAVE:
            self.decide_who_to_save(self.load_save_instructions['who_to_save'])
        elif self.load_save_instructions['action'] == ACTION_LOAD:
            self.decide_who_to_load(self.load_save_instructions['who_to_load'])

    def decide_who_to_save(self, instruction: int):
        """
        Based on Button Pressed, decides what to save.
        """
        if instruction == STORE_LOAD_RECORDING_SETTINGS:  # Save Recording Settings
            self.action_store_rec_setts()
        elif instruction == STORE_LOAD_LOCATION:
            self.action_store_location()
        elif instruction == STORE_LOAD_DAQ_PARAMS:
            self.action_store_DAQ_params()
            pass

    def decide_who_to_load(self, instruction: int):
        """
        Based on Button Pressed, decides what to load.
        """
        if instruction == STORE_LOAD_RECORDING_SETTINGS:  # Save Recording Settings
            self.action_load_rec_setts()
        elif instruction == STORE_LOAD_LOCATION:
            self.action_load_location()
        elif instruction == STORE_LOAD_DAQ_PARAMS:
            self.action_load_DAQ_params()

    def action_store_DAQ_params(self):
        """

        :return:
        """
        # Get filename from User
        self.filename_input_win.open()
        filename = self.filename_input_win.fn_in.text()  # TODO FIXME May cause error. --> verify if method .text()
        if Window.validate_filename(filename):
            if self.validate_daq_params():
                self.setting_manager.store_signal_params(filename)
            else:
                self.display_error('Error: Invalid Signal Parameters. '
                                   'Please select a valid option from the Drop Downs.<br>')
            self.filename_input_win.close()

        pass

    def action_load_DAQ_params(self):
        """

        :return:
        """
        relative_path = 'Config/DAQ/Signal'
        # Get filename from User
        filename = self.file_system(relative_path)
        # Load Params from File
        self.setting_manager.load_signal_params(filename)

        if set_dat_man.verify_file_exists(filename):
            # Set Params into GUI.
            self.set_DAQ_params_into_gui()
            # Close Window
            self.filename_input_win.close()

        pass

    def action_store_location(self):
        """

        :return:
        """
        # Get filename from User
        self.filename_input_win.open()
        filename = self.filename_input_win.fn_in.text()  # TODO FIXME if error --> Verify .text() method
        if Window.validate_filename(filename):
            # Get info from GUI.
            # get_location_from_gui()
            loc_type = self.loc_type_dropdown.currentIndex()
            if not loc_type:
                if not self.validate_gps_location_settings():
                    # Save to File.
                    self.setting_manager.store_location_configs(filename)
                    # Close Window
                    self.filename_input_win.close()
                else:
                    self.display_error(self.validate_gps_location_settings())
            else:
                if not self.validate_module_location_settings():
                    # Save to File.
                    self.setting_manager.store_location_configs(filename)
                    # Close Window
                    self.filename_input_win.close()
                else:
                    self.display_error(self.validate_module_location_settings())
            self.filename_input_win.close()

        pass

    def action_load_location(self):
        """

        :return:
        """
        relative_path = 'Config/DAQ/Location'
        # Get filename from User
        filename = self.file_system(relative_path)

        self.change_local_allowed()

        # Load Params from File
        self.setting_manager.load_location_configs(filename)
        if set_dat_man.verify_file_exists(filename):
            # Set Params into GUI.
            self.load_local_settings_to_gui()
            # Close Window
            # self.filename_input_win.close()

    def action_store_rec_setts(self):
        """

        :return:
        """
        # Get filename from User
        filename = self.filename_input_win.fn_in.text()
        if Window.validate_filename(filename):
            if not self.validate_rec_settings():  # Validation calls get_rec_setts_from_gui()
                # Save to File.
                self.setting_manager.store_recording_configs(filename)
            else:
                self.display_error(self.validate_rec_settings())

            # Close Window
            self.filename_input_win.close()

        pass

    def action_load_rec_setts(self):
        """

        :return:
        """
        relative_path = 'Config/DAQ/Recording'
        # Get filename from User
        filename = self.file_system(relative_path)

        if set_dat_man.verify_file_exists(filename):
            # Load Params from File
            self.setting_manager.load_recording_configs(filename)
            # Set Params into GUI.
            self.set_recording_into_gui()
            # Close Window
            self.filename_input_win.close()
            
        pass

    def load_local_settings_to_gui(self):
        """
        Loads Settings already in the program to GUi components depending on location type selected by user.
        The fields for the types not selected will be disabled.
        """
        if log: print(self.loc_type_dropdown.currentIndex())

        if self.loc_type_dropdown.currentIndex() == 0:  # GPS
            self.loc_gps_frame.setEnabled(True)
            self.loc_specimen_frame.setEnabled(False)
            self.set_GPS_into_gui()

        elif self.loc_type_dropdown.currentIndex() == 1:  # Specimen
            self.loc_gps_frame.setEnabled(False)
            self.loc_specimen_frame.setEnabled(True)
            self.set_specimen_location_into_gui()

    # *********************************** GUI FIELDS ****************************************
    def set_recording_into_gui(self):
        """
        Sets Recording settings to GUI Fields.
        """
        self.rec_name_edit.setText(str(self.daq_config.recording_configs['test_name']))
        self.rec_duration_edit.setText(str(self.daq_config.recording_configs['test_duration']))
        self.rec_type_dropdown.setCurrentText(str(self.daq_config.recording_configs['test_type']))
        self.delay_edit.setText(str(self.daq_config.recording_configs['test_start_delay']))

        pass

    def set_GPS_into_gui(self):
        """
        Sets GPS information on current settings into GUI fields.
        """
        self.loc_type_dropdown.setCurrentIndex(0)  # Set to GPS in Drop Down.
        self.loc_name_edit.setText(str(self.daq_config.location_configs['loc_name']))
        self.loc_longitude_edit.setText(str(self.daq_config.location_configs['longitude']))
        self.loc_latitude_edit.setText(str(self.daq_config.location_configs['latitude']))
        self.loc_hour_edit.setText(str(self.daq_config.location_configs['hour']))
        self.loc_minute_edit.setText(str(self.daq_config.location_configs['minute']))
        self.loc_seconds_edit.setText(str(self.daq_config.location_configs['second']))

    def set_specimen_location_into_gui(self):
        """
        Sets Specimen Location information on current settings into GUI fields.
        """
        self.specimen_loc_1.setText(self.daq_config.specimen_location['Specimen 1'])
        self.specimen_loc_2.setText(self.daq_config.specimen_location['Specimen 2'])
        self.specimen_loc_3.setText(self.daq_config.specimen_location['Specimen 3'])
        self.specimen_loc_4.setText(self.daq_config.specimen_location['Specimen 4'])
        self.specimen_loc_5.setText(self.daq_config.specimen_location['Specimen 5'])
        self.specimen_loc_6.setText(self.daq_config.specimen_location['Specimen 6'])
        self.specimen_loc_7.setText(self.daq_config.specimen_location['Specimen 7'])
        self.specimen_loc_8.setText(self.daq_config.specimen_location['Specimen 8'])

        pass

    def set_DAQ_params_into_gui(self):
        """
        Sets Data Acquisition Parameters to GUI Fields.
        """
        self.samfreq_dropdown.setCurrentText(self.daq_config.signal_configs['sampling_rate'])
        self.cutfreq_drodown.setCurrentText(self.daq_config.signal_configs['cutoff_frequency'])
        self.gain_dropdown.setCurrentText(self.daq_config.signal_configs['signal_gain'])

        pass

    def get_recording_from_gui(self):
        """
        Gets information on GUI into DAQ Parameters Data Structures.
        """
        # try:  # This should NEVER happen when validating
        self.daq_config.recording_configs['test_name'] = str(self.rec_name_edit.text())
        self.daq_config.recording_configs['test_duration'] = int(self.rec_duration_edit.text())
        self.daq_config.recording_configs['test_start_delay'] = int(self.delay_edit.text())
        self.daq_config.recording_configs['test_type'] = str(self.rec_type_dropdown.currentText())

        pass

    def get_GPS_from_gui(self):
        """

        :return:
        """
        self.daq_config.location_configs['loc_name'] = str(self.loc_name_edit.text())
        self.daq_config.location_configs['longitude'] = str(self.loc_longitude_edit.text())
        self.daq_config.location_configs['latitude'] = str(self.loc_latitude_edit.text())
        self.daq_config.location_configs['hour'] = str(self.loc_hour_edit.text())
        self.daq_config.location_configs['minute'] = str(self.loc_minute_edit.text())
        self.daq_config.location_configs['second'] = str(self.loc_seconds_edit.text())

        pass

    def get_specimen_location_from_gui(self):
        """

        :return:
        """
        self.daq_config.specimen_location['Specimen 1'] = str(self.specimen_loc_1.text())
        self.daq_config.specimen_location['Specimen 2'] = str(self.specimen_loc_2.text())
        self.daq_config.specimen_location['Specimen 3'] = str(self.specimen_loc_3.text())
        self.daq_config.specimen_location['Specimen 4'] = str(self.specimen_loc_4.text())
        self.daq_config.specimen_location['Specimen 5'] = str(self.specimen_loc_5.text())
        self.daq_config.specimen_location['Specimen 6'] = str(self.specimen_loc_6.text())
        self.daq_config.specimen_location['Specimen 7'] = str(self.specimen_loc_7.text())
        self.daq_config.specimen_location['Specimen 8'] = str(self.specimen_loc_8.text())

        pass

    def get_location_all_from_gui(self):
        """
        Gets information on GUI into Location Data Structures.
        """
        self.get_specimen_location_from_gui()
        self.get_GPS_from_gui()

        pass

    def get_DAQ_params_from_gui(self):
        """
        Gets information on GUI into DAQ Parameters Data Structures.
        """
        self.daq_config.signal_configs['sampling_rate'] = self.samfreq_dropdown.currentText()
        self.daq_config.signal_configs['cutoff_frequency'] = self.cutfreq_drodown.currentText()
        self.daq_config.signal_configs['signal_gain'] = self.gain_dropdown.currentText()

        self.daq_config.sampling_rate_index = self.samfreq_dropdown.currentIndex()
        self.daq_config.cutoff_freq_index = self.cutfreq_drodown.currentIndex()
        self.daq_config.gain_index = self.gain_dropdown.currentIndex()

        pass

    def suggest_sampling_rate(self):
        """
        Suggest user a sampling rate based on selected cutoff frequency and Nyquist Theorem.
        Only if sampling rate has not been selected previously.

        :return:
        """
        if self.samfreq_dropdown.currentText() == 'Please Select':
            self.samfreq_dropdown.setCurrentIndex(self.cutfreq_drodown.currentIndex())

        pass

    # *********************************** VALIDATION ****************************************
    def validate_daq_params(self):
        """
        Validates User has selected all DAQ Parameters.

        :return: True if fields validated.
        """
        validated = True
        sampling_rate = self.samfreq_dropdown.currentText()
        cutoff = self.cutfreq_drodown.currentText()
        gain = self.gain_dropdown.currentText()
        if sampling_rate == 'Please Select' or cutoff == 'Please Select' or gain == 'Please Select':
            validated = False
        else:
            self.get_DAQ_params_from_gui()
        return validated

    def check_sampling_rate(self):
        """
        When Duration LineEdit is modified, verify that it does not exceed the
        the maximum duration allowed by the sampling rate if one is already selected.
        :return:
        """
        test_duration = self.rec_duration_edit.text()
        print(test_duration)
        if not test_duration == '':
            if int(test_duration) < 5:
                self.display_error('Must be higher than 5 seconds and less than 1800 seconds')
            else:
                if not self.samfreq_dropdown.currentText() == 'Please Select':
                    max_duration = MAX_DURATION[self.samfreq_dropdown.currentText()]
                    if not max_duration == 'Please Select':
                        if int(test_duration) > max_duration:
                            self.display_error('Durations higher than ' + str(max_duration) +
                                               ' seconds at this sampling rate will exceed DAQ memory and rewrite samples.')

    def check_duration(self):
        """
        When Sampling Rate drop-down combobox is modified, verify that the current
        duration does not exceed the maximum duration allowed by the new sampling rate.
        """
        test_duration = self.rec_duration_edit.text()
        if test_duration:
            if not self.main_window.main_tab_DAQParams_samplingRate_DropDown.currentText() == 'Please Select':
                max_duration = MAX_DURATION[self.samfreq_dropdown.currentText()]
                if int(test_duration) > max_duration:
                    self.display_error('Durations higher than ' + str(max_duration) +
                                       ' seconds at this sampling rate will exceed DAQ memory and rewrite samples.')

    def validate_rec_settings(self):
        there_is_no_error = True
        error_string = ''
        if self.rec_name_edit.text() == '':
            there_is_no_error = False
            error_string += 'Test Name Field is empty.<br>'
        if self.rec_duration_edit.text() == '':
            there_is_no_error = False
            error_string += 'Duration Field is empty.<br>'
        else:
            if int(self.rec_duration_edit.text()) < 5:
                there_is_no_error = False
                error_string += 'Duration Field is less than 5 seconds.<br>'
        if self.delay_edit.text() == '':
            there_is_no_error = False
            error_string += 'Start Delay Field is empty.<br>'
        if there_is_no_error:
            self.get_recording_from_gui()
            return error_string
        else:
            return error_string

    def validate_gps_location_settings(self):
        there_is_no_error = True
        error_string = ''
        if self.loc_name_edit.text() == '':
            there_is_no_error = False
            error_string += 'Location Name Field is empty.<br>'
        if self.loc_longitude_edit.text() == '':
            there_is_no_error = False
            error_string += 'Longitude Field is empty.<br>'
        if self.loc_latitude_edit.text() == '':
            there_is_no_error = False
            error_string += 'Latitude Field is empty.<br>'
        if self.loc_hour_edit.text() == '':
            there_is_no_error = False
            error_string += 'Hour Field is empty.<br>'
        if self.loc_minute_edit.text() == '':
            there_is_no_error = False
            error_string += 'Minute Field is empty.<br>'
        if self.loc_seconds_edit.text() == '':
            there_is_no_error = False
            error_string += 'Seconds Field is empty.<br>'
        if there_is_no_error:
            self.get_GPS_from_gui()
            return error_string
        else:
            return error_string

    def validate_module_location_settings(self):
        there_is_no_error = True
        error_string = ''
        if self.specimen_loc_1.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 1 Location Field is empty.<br>'
        if self.specimen_loc_2.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 2 Location Field is empty.<br>'
        if self.specimen_loc_3.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 3 Location Field is empty.<br>'
        if self.specimen_loc_4.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 4 Location Field is empty.<br>'
        if self.specimen_loc_5.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 5 Location Field is empty.<br>'
        if self.specimen_loc_6.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 6 Location Field is empty.<br>'
        if self.specimen_loc_7.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 7 Location Field is empty.<br>'
        if self.specimen_loc_8.text() == '':
            there_is_no_error = False
            error_string += 'Specimen 8 Location Field is empty.<br>'
        if there_is_no_error:
            self.get_specimen_location_from_gui()
            return error_string
        else:
            return error_string

    def validate_empty_fields(self):
        """
        Validates User has filled all fields.

        :return: True if fields validated.
        """
        valid = True
        if self.rec_name_edit.text() == '' or \
                self.rec_duration_edit.text() == '' or \
                self.delay_edit.text() == '' or \
                self.loc_name_edit.text() == '' or \
                self.loc_longitude_edit.text() == '' or \
                self.loc_latitude_edit.text() == '' or \
                self.loc_hour_edit.text() == '' or \
                self.loc_minute_edit.text() == '' or \
                self.loc_seconds_edit.text() == '':
            valid = False

        return valid

    # ======================================= MISCELLANEOUS ==================================
    def display_error(self, message: str):
        """
        Displays Error Message with self Main Window as Parent.

        :param message: Error Message to display in Error Dialog.
        :param parent: DOES NOTHING. COMPLY WITH SUPER METHOD.

        :return: a Qt StandardButton
        """
        return super().display_error(message)

    def change_local_allowed(self):
        if log: print(self.loc_type_dropdown.currentIndex())

        if self.loc_type_dropdown.currentIndex() == 0:  # GPS
            self.enable_gps_disable_spec()

        elif self.loc_type_dropdown.currentIndex() == 1:  # Specimen
            self.disable_gps_enable_spec()

    def enable_gps_disable_spec(self):
        """
        Enables all GPS location fields of self Window (main window)
        """
        # Enable Frame
        self.loc_gps_frame.setEnabled(True)

        # Enable GPS Fields
        self.enable_field(self.loc_name_edit)
        self.enable_field(self.loc_latitude_edit)
        self.enable_field(self.loc_longitude_edit)
        self.enable_field(self.loc_hour_edit)
        self.enable_field(self.loc_minute_edit)
        self.enable_field(self.loc_seconds_edit)
        # Disable Specimen Location Fields.
        self.disable_field(self.specimen_loc_1)
        self.disable_field(self.specimen_loc_2)
        self.disable_field(self.specimen_loc_3)
        self.disable_field(self.specimen_loc_4)
        self.disable_field(self.specimen_loc_5)
        self.disable_field(self.specimen_loc_6)
        self.disable_field(self.specimen_loc_7)
        self.disable_field(self.specimen_loc_8)

    def disable_gps_enable_spec(self):
        """
        Enables all GPS location fields of self Window (main window)
        """
        # Enable Frame
        self.loc_specimen_frame.setEnabled(True)

        # Enable Specimen Location Fields.
        self.enable_field(self.specimen_loc_1)
        self.enable_field(self.specimen_loc_2)
        self.enable_field(self.specimen_loc_3)
        self.enable_field(self.specimen_loc_4)
        self.enable_field(self.specimen_loc_5)
        self.enable_field(self.specimen_loc_6)
        self.enable_field(self.specimen_loc_7)
        self.enable_field(self.specimen_loc_8)
        # Disable GPS Fields
        self.disable_field(self.loc_name_edit)
        self.disable_field(self.loc_latitude_edit)
        self.disable_field(self.loc_longitude_edit)
        self.disable_field(self.loc_hour_edit)
        self.disable_field(self.loc_minute_edit)
        self.disable_field(self.loc_seconds_edit)

    def enable_field(self, gui_field: QtWidgets):
        """
        Enables QtWidgets and sets corresponding styleSheet.

        :param gui_field: QtWidget to Enable.
        """
        gui_field.setEnabled(True)
        gui_field.setStyleSheet('background-color:rgb(255, 255, 255);'
                                'font: 12pt "MS Shell Dlg 2";'
                                'color: rgb(0, 0, 0)')

    def disable_field(self, gui_field: QtWidgets):
        """
        Enables QtWidgets and sets corresponding styleSheet.

        :param gui_field: QtWidget to Enable.
        """
        gui_field.setEnabled(False)
        gui_field.setStyleSheet('background-color:rgb(221, 221, 221);'
                                'font: 12pt "MS Shell Dlg 2";'
                                'color: rgb(0, 0, 0)')

    def do_plot(self, plot: int):
        filename = self.file_system('Data')
        if not Window.validate_path(filename):
            visualization_values['plot_filename'] = filename  # TODO FIXME POSSIBLE ERROR
            visualization_values['requested_plot'] = plot

            sensors = CSV_Handler.read_sensor_headers(visualization_values['plot_filename'])
            self.selection_dialog = VizSensorSelector(self, visualization_values)
            # Clear DropDown to prepare for new plot option.
            #   Clear everything but Placeholder [Index 0].
            for item in range(1, self.selection_dialog.viz_sens_1_dropdown.count(), 1):
                self.selection_dialog.viz_sens_1_dropdown.removeItem(1)
            for item in range(1, self.selection_dialog.viz_sens_2_dropdown.count(), 1):
                self.selection_dialog.viz_sens_2_dropdown.removeItem(1)

            # Set DropDown Values
            self.selection_dialog.viz_sens_1_dropdown.addItems(sensors)
            self.selection_dialog.viz_sens_2_dropdown.addItems(sensors)

            # Update Label and Enabled Dropdown for correct plot window
            if plot == TIME_PLOT:
                self.selection_dialog.viz_name_label.setText('Plot Raw Data Against Time. <br>'
                                                             'Please Select Only one Sensor.')
                self.selection_dialog.viz_sens_2_dropdown.setCurrentIndex(0)
                self.disable_viz_2_dropdown()
                self.selection_dialog.number_of_sensors = 1

            elif plot == FREQ_PLOT:
                self.selection_dialog.viz_name_label.setText('Plot Frequency Spectrum. <br>'
                                                             'Please Select Only one Sensor.')
                self.selection_dialog.viz_sens_2_dropdown.setCurrentIndex(0)
                self.disable_viz_2_dropdown()
                self.selection_dialog.number_of_sensors = 1

            elif plot == APS_PLOT:
                self.selection_dialog.viz_name_label.setText('Plot Auto-Power Spectrum. <br>'
                                                             'Please Select Only one Sensor.')
                self.selection_dialog.viz_sens_2_dropdown.setCurrentIndex(0)
                self.disable_viz_2_dropdown()
                self.selection_dialog.number_of_sensors = 1

            elif plot == CPS_PLOT:
                self.selection_dialog.viz_name_label.setText('Plot Cross-Power Spectrum. <br>'
                                                             'Please Select Two Sensors.')
                self.enable_viz_2_dropdown()
                self.selection_dialog.number_of_sensors = 2

            elif plot == COHERENCE_PLOT:
                self.selection_dialog.viz_name_label.setText('Plot Coherence Function. <br>'
                                                             'Please Select Two Sensors.')
                self.enable_viz_2_dropdown()
                self.selection_dialog.number_of_sensors = 2

            self.selection_dialog.open()

    def disable_viz_2_dropdown(self):
        self.selection_dialog.viz_sens_2_dropdown.setCurrentIndex(0)
        self.selection_dialog.viz_sens_2_dropdown.setEnabled(False)
        self.selection_dialog.viz_sens_2_dropdown.setStyleSheet('background-color: rgb(255, 255, 255);'
                                                                'font: 14pt "MS Shell Dlg 2";'
                                                                'color: rgb(162, 162, 162);')

    def enable_viz_2_dropdown(self):
        self.selection_dialog.viz_sens_2_dropdown.setCurrentIndex(0)
        self.selection_dialog.viz_sens_2_dropdown.setEnabled(True)
        self.selection_dialog.viz_sens_2_dropdown.setStyleSheet('background-color: rgb(255, 255, 255);'
                                                                'font: 14pt "MS Shell Dlg 2";'
                                                                'color: rgb(0, 0, 0);')

    def begin_visualization(self):
        """
        Begins Visualization Analysis for user selected plots.
        """
        filename = visualization_values['plot_filename']
        if not Window.validate_path(filename):

            plot = visualization_values['requested_plot']

            if self.selection_dialog.get_number_sensors() == 2:  # Requires 2 Sensors.
                if self.selection_dialog.validate_visualize_sensor_selection(2):
                    if plot == CPS_PLOT:
                        self.plot_cps(filename)
                    elif plot == PHASE_PLOT:
                        self.plot_phase(filename)
                    elif plot == COHERENCE_PLOT:
                        self.plot_cohere(filename)
                else:
                    self.display_error('Sensor not selected.')

            elif self.selection_dialog.get_number_sensors() == 1:  # Only have to Validate One Sensor.
                if self.selection_dialog.validate_visualize_sensor_selection(1):
                    # Choose which Plot.
                    if plot == TIME_PLOT:
                        self.plot_time(filename)
                    elif plot == FREQ_PLOT:
                        self.plot_fft(filename)
                    elif plot == APS_PLOT:
                        self.plot_aps(filename)
                else:
                    self.display_error('Sensor not selected.')

        else:
            self.display_error('File name or Path incorrect.1 <br> <br>'
                                       'Choose a File from: C://[USER PATH]/EWAS_Applocation/Data/')

    def plot_time(self, filename: str):
        """
        [1]
        Creates and Opens Window with Time plot using user information from file.
        """
        sensor = self.selection_dialog.viz_sens_1_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plt_time(sensor)

    def plot_fft(self, filename: str):
        """
        [2]
        Creats and Opens Window with Time plot using user information from file.
        """
        sensor = self.selection_dialog.viz_sens_1_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plot_fft(sensor)

    def plot_aps(self, filename: str):
        """
        [3]
        Creates and Opens Window with Time plot using user information from file.
        """
        sensor = self.selection_dialog.viz_sens_1_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plot_PSD(sensor)

    def plot_cps(self, filename: str):
        """
        [4]
        Creates and Opens Window with Time plot using user information from file.
        """
        sensor_1 = self.selection_dialog.viz_sens_1_dropdown.currentText()
        sensor_2 = self.selection_dialog.viz_sens_2_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plot_CSD(sensor_1=sensor_1, sensor_2=sensor_2)

    def plot_phase(self, filename: str):
        """
        [5]
        Creates and Opens Window with Time plot using user information from file.
        """
        sensor = self.selection_dialog.viz_sens_1_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plot_Phase(sensor)

    def plot_cohere(self, filename: str):
        """
        [6]
        Creates and Opens Window with Time plot using user information from file.
        """
        sensor_1 = self.selection_dialog.viz_sens_1_dropdown.currentText()
        sensor_2 = self.selection_dialog.viz_sens_2_dropdown.currentText()

        Plot_Data.Plot_Data(filename).plot_coherence(sensor_1=sensor_1, sensor_2=sensor_2)

    def get_visualization_values(self):
        """
        :return: visualization_values Dictionary for instance.
        """
        return visualization_values
