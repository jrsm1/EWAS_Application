from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
from time import sleep
import sys
import serial

from Control_Module_Comm import instruction_manager as ins_man
from Control_Module_Comm.Structures import Module_Individual as chan, Sensor_Individual as sens
from Data_Processing import Plot_Data
from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Settings import setting_data_manager as set_dat_man
from regex import regex


def show_error(message: str):
    """
        Creates an Error Message dialog

        :param message: String - The Desired Message Output.
    """
    QtWidgets.QMessageBox().critical(main_window, 'WARNING', message)


def show_not_connected_error():
    show_error(not_connected_error_string)


app = QtWidgets.QApplication([])
main_window = uic.loadUi("GUI/Qt_Files/main_window.ui")
prog_dlg = uic.loadUi("GUI/Qt_Files/progress_dialog_v1.ui")
viz_sensor_sel_win = uic.loadUi('GUI/Qt_Files/visualize_sensor_selection_matrix.ui')
main_sensor_sel_win = uic.loadUi('GUI/Qt_Files/main_sensor_selection_matrix.ui')
mod_sel_win = uic.loadUi('GUI/Qt_Files/module_selection_window.ui')
file_sys_win = uic.loadUi('GUI/Qt_Files/file_system_window.ui')
filename_input_win = uic.loadUi('GUI/Qt_Files/filename_editor_window.ui')
module_1_info_win = uic.loadUi("GUI/Qt_Files/module_1_info_window.ui")
module_2_info_win = uic.loadUi("GUI/Qt_Files/module_2_info_window.ui")
module_3_info_win = uic.loadUi("GUI/Qt_Files/module_3_info_window.ui")
module_4_info_win = uic.loadUi("GUI/Qt_Files/module_4_info_window.ui")
module_5_info_win = uic.loadUi("GUI/Qt_Files/module_5_info_window.ui")
module_6_info_win = uic.loadUi("GUI/Qt_Files/module_6_info_window.ui")
module_7_info_win = uic.loadUi("GUI/Qt_Files/module_7_info_window.ui")
module_8_info_win = uic.loadUi("GUI/Qt_Files/module_8_info_window.ui")

main_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
prog_dlg.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
viz_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
main_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
mod_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
file_sys_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
filename_input_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_1_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_2_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_3_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_4_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_5_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_6_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_7_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_8_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

# Init Instances of all classes for reference
sens_1 = Sensor_Individual.Sensor('Sensor 1', 0)
sens_2 = Sensor_Individual.Sensor('Sensor 2', 0)
sens_3 = Sensor_Individual.Sensor('Sensor 3', 0)
sens_4 = Sensor_Individual.Sensor('Sensor 4', 0)
sens_5 = Sensor_Individual.Sensor('Sensor 5', 0)
sens_6 = Sensor_Individual.Sensor('Sensor 6', 0)
sens_7 = Sensor_Individual.Sensor('Sensor 7', 0)
sens_8 = Sensor_Individual.Sensor('Sensor 8', 0)
sens_9 = Sensor_Individual.Sensor('Sensor 9', 0)
sens_10 = Sensor_Individual.Sensor('Sensor 10', 0)
sens_11 = Sensor_Individual.Sensor('Sensor 11', 0)
sens_12 = Sensor_Individual.Sensor('Sensor 12', 0)
sens_13 = Sensor_Individual.Sensor('Sensor 13', 0)
sens_14 = Sensor_Individual.Sensor('Sensor 14', 0)
sens_15 = Sensor_Individual.Sensor('Sensor 15', 0)
sens_16 = Sensor_Individual.Sensor('Sensor 16', 0)
sens_17 = Sensor_Individual.Sensor('Sensor 17', 0)
sens_18 = Sensor_Individual.Sensor('Sensor 18', 0)
sens_19 = Sensor_Individual.Sensor('Sensor 19', 0)
sens_20 = Sensor_Individual.Sensor('Sensor 20', 0)
sens_21 = Sensor_Individual.Sensor('Sensor 21', 0)
sens_22 = Sensor_Individual.Sensor('Sensor 22', 0)
sens_23 = Sensor_Individual.Sensor('Sensor 23', 0)
sens_24 = Sensor_Individual.Sensor('Sensor 24', 0)
sens_25 = Sensor_Individual.Sensor('Sensor 25', 0)
sens_26 = Sensor_Individual.Sensor('Sensor 26', 0)
sens_27 = Sensor_Individual.Sensor('Sensor 27', 0)
sens_28 = Sensor_Individual.Sensor('Sensor 28', 0)
sens_29 = Sensor_Individual.Sensor('Sensor 29', 0)
sens_30 = Sensor_Individual.Sensor('Sensor 30', 0)
sens_31 = Sensor_Individual.Sensor('Sensor 31', 0)
sens_32 = Sensor_Individual.Sensor('Sensor 32', 0)
sensors_all = [sens_1, sens_2, sens_3, sens_4, sens_5, sens_6, sens_7, sens_8, sens_9, sens_10,
               sens_11, sens_12, sens_13, sens_14, sens_15, sens_16, sens_17, sens_18, sens_19, sens_20,
               sens_21, sens_22, sens_23, sens_24, sens_25, sens_26, sens_27, sens_28, sens_29, sens_30,
               sens_31, sens_32]  # Used to get sensors easily (goes from 0 to 31)
mod_1 = Module_Individual.Module('Channel 1', sens_1, sens_2, sens_3, sens_4)
mod_2 = Module_Individual.Module('Channel 2', sens_5, sens_6, sens_7, sens_8)
mod_3 = Module_Individual.Module('Channel 3', sens_9, sens_10, sens_11, sens_12)
mod_4 = Module_Individual.Module('Channel 4', sens_13, sens_14, sens_15, sens_16)
mod_5 = Module_Individual.Module('Channel 5', sens_17, sens_18, sens_19, sens_20)
mod_6 = Module_Individual.Module('Channel 6', sens_21, sens_22, sens_23, sens_24)
mod_7 = Module_Individual.Module('Channel 7', sens_25, sens_26, sens_27, sens_28)
mod_8 = Module_Individual.Module('Channel 8', sens_29, sens_30, sens_31, sens_32)
modules_all = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6, mod_7,
               mod_8]  # Used to get channels easily (goes from 0 to 7)

# ----------- CONFIGS ----------
daq_config = DAQ_Configuration.DAQconfigs()

setting_data_manager = set_dat_man.Setting_File_Manager(daq_con=daq_config, mod_con=modules_all, sens_con=sensors_all)

# TESTING purposes
log = 1
log_working = 0

# Global Variables.
not_connected_error_string = 'Device is not Connected. <br> Please Try Again.'
# status global variables
recorded = 0
stored = 0
gps_sync = 0
ins_port = 'COM-1'


def show_main_window():
    """
    Displays Main Window on Computer's Screen.
    """
    main_window.show()


def disable_main_window():
    """
        Disables Input for every Widget inside Main Window.
    """
    main_window.setEnabled(False)


def enable_main_window():
    """
        Disables Input for every Widget inside Main Window.
    """
    main_window.setEnabled(True)


def open_module_selection_window():
    """
    Opens Module Selection Window.
    Done before Channel Selection.
    """

    # Diable not connected modules.
    connected_modules = [1, 0, 0, 0, 0, 0, 0, 0]
    try:
        im = ins_man.instruction_manager(ins_port)
        connected_modules = im.send_request_number_of_mods_connected()
        disable_module_selection_buttons(connected_modules)
        mod_sel_win.show()
    except serial.SerialException:
        show_not_connected_error()

    disable_module_selection_buttons(connected_modules)

    mod_sel_win.show()


def disable_module_selection_buttons(connected_modules: []):
    """
    Disales not connected sensor buttons from Module Selection Window.

    :param connected_modules: List Containing each module state.
    """

    for val in range(8):
        if not connected_modules[val]:
            module_button_list[val].setEnabled(False)
            module_button_list[val].setStyleSheet('background-color:rgb(244, 166, 142);'
                                                  'color: rgb(255, 255, 255);'
                                                  'font: 12pt "MS Shell Dlg 2";')


def show_channel_info_window(module: int):
    """
    Opens Channel Information Window based on module selection button press.

    :param module: The module list index [MODULE NAME - 1]
    """

    # LATER TODO SAVE CORRECT VALUES FOR CHANNEL.

    # Close Mosule Selection Window now as it will not do anything. --> Open after module settings are saved.
    mod_sel_win.close()

    # Decide which Module the user has selected.
    if module == 0:
        module_1_info_win.show()
    elif module == 1:
        module_2_info_win.show()
    elif module == 2:
        module_3_info_win.show()
    elif module == 3:
        module_4_info_win.show()
    elif module == 4:
        module_5_info_win.show()
    elif module == 5:
        module_6_info_win.show()
    elif module == 6:
        module_7_info_win.show()
    elif module == 7:
        module_8_info_win.show()


def show_main_sens_sel_window():
    """
        Opens Sensor Selection Window for Recording
    """
    # disable_main_window()  # NOT Going to do. --> failed to re-enable correctly in all cases.
    if enable_main_start_connected_sensors():
        main_sensor_sel_win.show()


def show_progress_dialog(message: str):
    """
    Creates and Opens Progress Dialog.
    Default is to 'undetermined' infinite progress.
    To change default behaviour use { void QProgressBar::setRange(int minimum, int maximum) }

    :param message : Custom message to show on Dialog.
    """
    dlg_title.setText(message)
    prog_dlg.show()


def show_visualization_sensor_selector_window(plot: int):  # TODO
    # TODO REQUEST CONTROL MODULE FOR CONNECTED MODULES.
    viz_sensor_sel_win.show()
    # Pass info on who called me to know which plot to display.
    begin_visualization(plot)


def show_filename_editor_window():
    filename_input_win.show()


# TODO get selected sensors.
def begin_visualization(plot: int):
    """
    Begins Visualization Analysis for user selected plots.
    """
    # Choose which Plot.
    if plot == 1:
        plot_time()
    elif plot == 2:
        plot_fft()
    elif plot == 3:
        plot_aps()
    elif plot == 4:
        plot_cps()
    elif plot == 5:
        plot_phase()
    elif plot == 6:
        plot_cohere()

    # Show Progress Dialog. # TODO VERIFY IF REMOVE
    show_progress_dialog('Plotting ' + 'What you wanna plot')


def set_gps_into_gui():
    """
    Sets GPS information on current settings into GUI fields.
    """
    loc_type_dropdown.setCurrentIndex(0)  # Set to GPS in Drop Down.
    main_window.main_tab_LocalizationSettings_Name_lineEdit.setText(str(daq_config.location_configs['loc_name']))
    main_window.main_tab_LocalizationSettings_longitudLineEdit.setText(str(daq_config.location_configs['longitude']))
    main_window.main_tab_LocalizationSettings_latitudLineEdit.setText(str(daq_config.location_configs['latitude']))
    main_window.main_tab_LocalizationSettings_hourLineEdit.setText(str(daq_config.location_configs['hour']))
    main_window.main_tab_LocalizationSettings_minutesLineEdit.setText(str(daq_config.location_configs['minute']))
    main_window.main_tab_LocalizationSettings_secondsLineEdit.setText(str(daq_config.location_configs['second']))


def set_specimen_location_into_gui():
    """
    Sets Specimen Location information on current settings into GUI fields.
    """
    specimen_loc_1.setText(daq_config.specimen_location['Specimen 1'])
    specimen_loc_2.setText(daq_config.specimen_location['Specimen 2'])
    specimen_loc_3.setText(daq_config.specimen_location['Specimen 3'])
    specimen_loc_4.setText(daq_config.specimen_location['Specimen 4'])
    specimen_loc_5.setText(daq_config.specimen_location['Specimen 5'])
    specimen_loc_6.setText(daq_config.specimen_location['Specimen 6'])
    specimen_loc_7.setText(daq_config.specimen_location['Specimen 7'])
    specimen_loc_8.setText(daq_config.specimen_location['Specimen 8'])


def set_recording_into_gui():
    """
    Sets Recording settings to GUI Fields.
    """
    rec_name_edit.setText(str(daq_config.recording_configs['test_name']))
    # rec_id_edit.setText(daq_config.recording_configs['test_ID'])
    rec_duration_edit.setText(
        str(daq_config.recording_configs['test_duration']))  # Convert int to String for compatibility.
    rec_type_dropdown.setCurrentText(str(daq_config.recording_configs['test_type']))
    delay_edit.setText(str(daq_config.recording_configs['test_start_delay']))

    # if daq_config.data_handling_configs['visualize']:
    #     rec_viz_checkbox.setCheckState(2)  # Qt::Checked	2
    # else:
    #     rec_viz_checkbox.setCheckState(0)
    #
    # if daq_config.data_handling_configs['store']:
    #     rec_store_checkbox.setCheckState(2)
    # else:
    #     rec_store_checkbox.setCheckState(0)  # Qt::Unchecked	0


def set_daq_params_to_gui():
    """
    Sets Data Acquisition Parameters to GUI Fields.
    """
    samfreq_dropdown.setCurrentIndex(daq_config.signal_configs['sampling_rate'])
    cutfreq_drodown.setCurrentIndex(daq_config.signal_configs['cutoff_frequency'])
    gain_dropdown.setCurrentIndex(daq_config.signal_configs['signal_gain'])


def check_boxes(text_box: str, pattern: str):
    result = regex.match(pattern, text_box)
    return result


def get_rec_setts_from_gui():
    """
    Gets information on GUI into DAQ Parameters Data Structures.
    """
    # try:  # This should NEVER happen when validating
    daq_config.recording_configs['test_name'] = str(main_window.main_tab_RecordingSettings_name_LineEdit.text())
    daq_config.recording_configs['test_duration'] = int(main_window.main_tab_RecordingSettings_durationLineEdit.text())
    daq_config.recording_configs['test_start_delay'] = int(main_window.main_tab_RecordingSettings_delay_LineEdit.text())
    daq_config.recording_configs['test_type'] = str(main_window.main_tab_RecordingSettings_type_DropDown.currentText())
    """
    QCheckbox, needs checkState() to get the state.
    There are two states.
    2 = checked
    0 = unchecked
    """
    daq_config.recording_configs['visualize'] = main_window.main_tab_RecordingSettings_visualize_checkBox.isChecked()  # isChecked() returns
    # BOOLEAN
    daq_config.recording_configs['store'] = main_window.main_tab_RecordingSettings_store_checkBox.isChecked()  # isChecked() returns BOOLEAN
    if log: print(daq_config.recording_configs['visualize'], daq_config.recording_configs['store'])


def get_daq_params_from_gui():
    """
    Gets information on GUI into DAQ Parameters Data Structures.
    """
    daq_config.signal_configs['sampling_rate'] = main_window.main_tab_DAQParams_samplingRate_DropDown.currentText()
    daq_config.signal_configs['cutoff_frequency'] = main_window.main_tab_DAQParams_Cutoff_Frequency_DropDown.currentText()
    daq_config.signal_configs['signal_gain'] = main_window.main_tab_DAQParams_gain_DropDown.currentText()

    daq_config.sampling_rate_index = main_window.main_tab_DAQParams_samplingRate_DropDown.currentIndex()
    daq_config.cutoff_freq_index = main_window.main_tab_DAQParams_Cutoff_Frequency_DropDown.currentIndex()
    daq_config.gain_index = main_window.main_tab_DAQParams_gain_DropDown.currentIndex()


def get_location_from_gui():
    """
    Gets information on GUI into Location Data Structures.
    """
    daq_config.location_configs['loc_name'] = str(main_window.main_tab_LocalizationSettings_Name_lineEdit.text())
    daq_config.location_configs['longitude'] = str(main_window.main_tab_LocalizationSettings_longitudLineEdit.text())
    daq_config.location_configs['latitude'] = str(main_window.main_tab_LocalizationSettings_latitudLineEdit.text())
    daq_config.location_configs['hour'] = str(main_window.main_tab_LocalizationSettings_hourLineEdit.text())
    daq_config.location_configs['minute'] = str(main_window.main_tab_LocalizationSettings_minutesLineEdit.text())
    daq_config.location_configs['second'] = str(main_window.main_tab_LocalizationSettings_secondsLineEdit.text())
    daq_config.specimen_location['1'] = str(main_window.main_tab_module_loc_LineEdit_1.text())
    daq_config.specimen_location['2'] = str(main_window.main_tab_module_loc_LineEdit_2.text())
    daq_config.specimen_location['3'] = str(main_window.main_tab_module_loc_LineEdit_3.text())
    daq_config.specimen_location['4'] = str(main_window.main_tab_module_loc_LineEdit_4.text())
    daq_config.specimen_location['5'] = str(main_window.main_tab_module_loc_LineEdit_5.text())
    daq_config.specimen_location['6'] = str(main_window.main_tab_module_loc_LineEdit_6.text())
    daq_config.specimen_location['7'] = str(main_window.main_tab_module_loc_LineEdit_7.text())
    daq_config.specimen_location['8'] = str(main_window.main_tab_module_loc_LineEdit_8.text())


def get_gps_location_from_gui():
    daq_config.location_configs['loc_name'] = str(main_window.main_tab_LocalizationSettings_Name_lineEdit.text())
    daq_config.location_configs['longitude'] = str(main_window.main_tab_LocalizationSettings_longitudLineEdit.text())
    daq_config.location_configs['latitude'] = str(main_window.main_tab_LocalizationSettings_latitudLineEdit.text())
    daq_config.location_configs['hour'] = str(main_window.main_tab_LocalizationSettings_hourLineEdit.text())
    daq_config.location_configs['minute'] = str(main_window.main_tab_LocalizationSettings_minutesLineEdit.text())
    daq_config.location_configs['second'] = str(main_window.main_tab_LocalizationSettings_secondsLineEdit.text())


def get_modules_location_from_gui():
    daq_config.specimen_location['1'] = str(main_window.main_tab_module_loc_LineEdit_1.text())
    daq_config.specimen_location['2'] = str(main_window.main_tab_module_loc_LineEdit_2.text())
    daq_config.specimen_location['3'] = str(main_window.main_tab_module_loc_LineEdit_3.text())
    daq_config.specimen_location['4'] = str(main_window.main_tab_module_loc_LineEdit_4.text())
    daq_config.specimen_location['5'] = str(main_window.main_tab_module_loc_LineEdit_5.text())
    daq_config.specimen_location['6'] = str(main_window.main_tab_module_loc_LineEdit_6.text())
    daq_config.specimen_location['7'] = str(main_window.main_tab_module_loc_LineEdit_7.text())
    daq_config.specimen_location['8'] = str(main_window.main_tab_module_loc_LineEdit_8.text())


def validate_rec_settings():
    there_is_no_error = True
    error_string = ""
    name = main_window.main_tab_RecordingSettings_name_LineEdit.text()
    validate_box = check_boxes(name, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Name. Restricted to uppercase and lowercase letters, and numbers only.<br>'
        there_is_no_error = False
    test_duration = main_window.main_tab_RecordingSettings_durationLineEdit.text()
    validate_box = check_boxes(test_duration, '^[0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Duration. Restricted to numbers only.<br>'
        there_is_no_error = False
    start_delay = main_window.main_tab_RecordingSettings_delay_LineEdit.text()
    validate_box = check_boxes(start_delay, '^\d+$')
    if not validate_box:
        error_string += 'Error: Invalid Start Delay. Restricted to numbers only.<br>'
        there_is_no_error = False
    if there_is_no_error:
        get_rec_setts_from_gui()
        return error_string
    else:
        return error_string


def validate_gps_location_settings():
    there_is_no_error = True
    error_string = ""
    loc_name = main_window.main_tab_LocalizationSettings_Name_lineEdit.text()
    validate_box = check_boxes(loc_name, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Name format. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    loc_longitude = main_window.main_tab_LocalizationSettings_longitudLineEdit.text()
    validate_box = check_boxes(loc_longitude, '^(\+|-)?\d{5}.\d{5}$')
    if not validate_box:
        error_string += 'Error: Invalid Longitude format. Restricted to +/-Dddmm.mmmmm.<br>'
        there_is_no_error = False
    loc_latitude = main_window.main_tab_LocalizationSettings_latitudLineEdit.text()
    validate_box = check_boxes(loc_latitude, '^(\+|-)?\d{4}.\d{5}$')
    if not validate_box:
        error_string += 'Error: Invalid Latitude format. Restricted to +/-ddmm.mmmmm.<br>'
        there_is_no_error = False
    loc_hour = main_window.main_tab_LocalizationSettings_hourLineEdit.text()
    validate_box = check_boxes(loc_hour, '^\d{2}$')
    if not validate_box:
        error_string += 'Error: Invalid hour format. Restricted to two digits.<br>'
        there_is_no_error = False
    loc_minutes = main_window.main_tab_LocalizationSettings_minutesLineEdit.text()
    validate_box = check_boxes(loc_minutes, '^\d{2}$')
    if not validate_box:
        error_string += 'Error: Invalid minute format. Restricted to two digits.<br>'
        there_is_no_error = False
    loc_seconds = main_window.main_tab_LocalizationSettings_secondsLineEdit.text()
    validate_box = check_boxes(loc_seconds, '^\d{2}$')
    if not validate_box:
        error_string += 'Error: Invalid second format. Restricted to two digits.<br>'
        there_is_no_error = False
    if there_is_no_error:
        get_gps_location_from_gui()
        return error_string
    else:
        return error_string


def validate_module_location_settings():
    there_is_no_error = True
    error_string = ""
    module_loc1 = main_window.main_tab_module_loc_LineEdit_1.text()
    validate_box = check_boxes(module_loc1, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 1. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc2 = main_window.main_tab_module_loc_LineEdit_2.text()
    validate_box = check_boxes(module_loc2, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 2. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False

    module_loc3 = main_window.main_tab_module_loc_LineEdit_3.text()
    validate_box = check_boxes(module_loc3, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 3. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc4 = main_window.main_tab_module_loc_LineEdit_4.text()
    validate_box = check_boxes(module_loc4, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 4. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc5 = main_window.main_tab_module_loc_LineEdit_5.text()
    validate_box = check_boxes(module_loc5, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 5. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc6 = main_window.main_tab_module_loc_LineEdit_6.text()
    validate_box = check_boxes(module_loc6, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 6. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc7 = main_window.main_tab_module_loc_LineEdit_7.text()
    validate_box = check_boxes(module_loc7, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 7. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    module_loc8 = main_window.main_tab_module_loc_LineEdit_8.text()
    validate_box = check_boxes(module_loc8, '^[a-zA-Z0-9]+$')
    if not validate_box:
        error_string += 'Error: Invalid Location Specimen 8. Restricted to numbers, ' \
                        'uppercase and lowercase letters only.<br>'
        there_is_no_error = False
    if there_is_no_error:
        get_modules_location_from_gui()
        return error_string
    else:
        return error_string


def snapshot_data():
    """
    Gets all the data from fields in Main Window
    """
    # we have to change everything to string, because that's how it's going to get passed
    # main tab recording settings
    there_is_no_error = True
    error_string = ""
    if not validate_rec_settings() == '':
        error_string += validate_rec_settings()
        there_is_no_error = False
    # main tab localization settings
    loc_type = main_window.main_tab_LocalizationSettings_type_DropBox.currentIndex()
    if not loc_type:
        if not validate_gps_location_settings() == '':
            error_string += validate_gps_location_settings()
            there_is_no_error = False
    else:
        # specimen by module
        if not validate_module_location_settings() == '':
            error_string += validate_module_location_settings()
            there_is_no_error = False

    if there_is_no_error:
        get_rec_setts_from_gui()
        get_location_from_gui()
        get_daq_params_from_gui()
        return True
    else:
        show_error(error_string)
        return False


def get_module_and_sensors_selected():
    if log: print("entered get_module_and_sensors_selected()")
    count = 0
    sensors_sel = []
    if log: print("created empy sensor selected array")
    sensors_sel.append(main_sensor_sel_win.Sensor_1)
    if log:
        print("print sensors array created correctly")
    sensors_selected = "0000"
    correct = 1
    index = 0
    for i in main_sensor_selection_list:
        index += 1
        if i.checkState() == 2:
            count = count + 1
            module = str(int((index - 1) / 4) + 1)
            sensor = str(((index - 1) % 4) + 1)
            sensors_selected = module + sensor + sensors_selected
        if count > 2: #limit
            correct = 0
            break

    if log: print("sensors selected are: ", sensors_selected)

    for i in main_sensor_selection_list:
        i.setCheckState(False)
    if correct:
        sensors_selected = sensors_selected[0:4]
        return sensors_selected
    return "0000"

def get_sensor_enabled():
    sensor_enable = []
    if log: print("entered get_module_and_sensors_selected()")
    if log: print("created empy sensor selected array")

    for i in main_sensor_selection_list:
        sensor_enable.append(i.checkState())

    return sensor_enable


def start_acquisition():
    """
    Begin Acquisition Process
    """
    if snapshot_data():
        show_main_sens_sel_window()


def sensor_sel_start():
    sens = get_module_and_sensors_selected()
    if log: print("sensors selected are ", sens)
    sensors_enabled = get_sensor_enabled()

    main_sensor_sel_win.close()
    try:
        ins = ins_man.instruction_manager(ins_port)
        ins.send_recording_parameters(daq_config.sampling_rate_index, daq_config.cutoff_freq_index, daq_config.gain_index,
                                      "0100", "0100", "0102", sensors_enabled, "test name", "test location")
        enable_main_window()
        if log:
            print("came back to sensor_sel_start")
    except serial.SerialException:
        show_not_connected_error()


def save_port():
    port = 'COM-1'
    global ins_port
    pid = "0403"
    hid = "6001"
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if pid and hid in p.hwid:
            port = p.device
    ins_port = port
    return port


def enable_main_start_connected_sensors():
    # TODO TEST
    continuar = True
    try:
        ins = ins_man.instruction_manager(ins_port)
        connected_module_list = ins.send_request_number_of_mods_connected()
        if log: print("entered enable start")
        if connected_module_list[0]:
            win_sens_1.setEnabled(True)
            win_sens_2.setEnabled(True)
            win_sens_3.setEnabled(True)
            win_sens_4.setEnabled(True)
        if connected_module_list[1]:
            win_sens_5.setEnabled(True)
            win_sens_6.setEnabled(True)
            win_sens_7.setEnabled(True)
            win_sens_8.setEnabled(True)
        if connected_module_list[2]:
            win_sens_9.setEnabled(True)
            win_sens_10.setEnabled(True)
            win_sens_11.setEnabled(True)
            win_sens_12.setEnabled(True)
        if connected_module_list[3]:
            win_sens_13.setEnabled(True)
            win_sens_14.setEnabled(True)
            win_sens_15.setEnabled(True)
            win_sens_16.setEnabled(True)
        if connected_module_list[4]:
            win_sens_17.setEnabled(True)
            win_sens_18.setEnabled(True)
            win_sens_19.setEnabled(True)
            win_sens_20.setEnabled(True)
        if connected_module_list[5]:
            win_sens_21.setEnabled(True)
            win_sens_22.setEnabled(True)
            win_sens_23.setEnabled(True)
            win_sens_24.setEnabled(True)
        if connected_module_list[6]:
            win_sens_25.setEnabled(True)
            win_sens_26.setEnabled(True)
            win_sens_27.setEnabled(True)
            win_sens_28.setEnabled(True)
        if connected_module_list[7]:
            win_sens_29.setEnabled(True)
            win_sens_30.setEnabled(True)
            win_sens_31.setEnabled(True)
            win_sens_32.setEnabled(True)
        if log: print("got out of enable start connected sensors")
        # If not Connected to not continue.
    except serial.SerialException:
        continuar = False
        show_not_connected_error()

    return continuar


def check_status():
    global recorded, stored, gps_sync
    try:
        ins = ins_man.instruction_manager(ins_port)
        status = ins.send_request_status()
        recorded = status[0]
        stored = status[1]
        gps_sync = status[2]
        if log:
            print("status = " + str(status))
        return status
    except serial.SerialException:
        show_not_connected_error()
        return False

# trying a close event function
def close_event(event):
    if log: print("entered main window close")
    if log: print(
        "final status recorded=" + str(recorded) + ", stored=" + str(stored) + ", gps_synched=" + str(gps_sync))
    main_window.close()

def file_choose(rootPath: str):
    return str(QFileDialog.getOpenFileName(None, 'Open CSV File', rootPath, 'CSV Files (*.csv)')[0])



"""
Add default functionality here
"""
# Module 1 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(1))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_1_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_1_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_1_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_1_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_1_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_1_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_1_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_1_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_1_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_1_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_1_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_1_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_1_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_1_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_1_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_1_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_1_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_1_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_1_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_1_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_1_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_1_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_1_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_1_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_1_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_1_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_1_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_1_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 2 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(2))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_2_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_2_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_2_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_2_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_2_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_2_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_2_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_2_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_2_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_2_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_2_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_2_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_2_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_2_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_2_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_2_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_2_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_2_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_2_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_2_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_2_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_2_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_2_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_2_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_2_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_2_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_2_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_2_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 3 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(3))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_3_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_3_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_3_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_3_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_3_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_3_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_3_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_3_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_3_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_3_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_3_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_3_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_3_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_3_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_3_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_3_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_3_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_3_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_3_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_3_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_3_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_3_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_3_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_3_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_3_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_3_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_3_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_3_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 4 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(4))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_4_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_4_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_4_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_4_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_4_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_4_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_4_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_4_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_4_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_4_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_4_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_4_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_4_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_4_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_4_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_4_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_4_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_4_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_4_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_4_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_4_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_4_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_4_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_4_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_4_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_4_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_4_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_4_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 5 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(5))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_5_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_5_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_5_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_5_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_5_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_5_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_5_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_5_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_5_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_5_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_5_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_5_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_5_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_5_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_5_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_5_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_5_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_5_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_5_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_5_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_5_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_5_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_5_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_5_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_5_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_5_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_5_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_5_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 6 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(6))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_6_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_6_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_6_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_6_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_6_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_6_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_6_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_6_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_6_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_6_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_6_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_6_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_6_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_6_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_6_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_6_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_6_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_6_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_6_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_6_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_6_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_6_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_6_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_6_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_6_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_6_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_6_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_6_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 7 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(7))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_7_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_7_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_7_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_7_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_7_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_7_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_7_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_7_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_7_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_7_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_7_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_7_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_7_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_7_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_7_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_7_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_7_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_7_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_7_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_7_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_7_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_7_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_7_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_7_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_7_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_7_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_7_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_7_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE

# Module 8 Info Window.
module_1_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_module_info(8))
chan_mod_name = module_1_info_win.channel_info_module_name
# Ch 1
module_8_sensor_1_sensitivity = module_1_info_win.channel_info_sensor1_Sensitivity_LineEdit
module_8_sensor_1_damping = module_1_info_win.channel_info_sensor1_dampingLineEdit
module_8_sensor_1_bandwidth = module_1_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
module_8_sensor_1_fullscale = module_1_info_win.channel_info_sensor1_full_Scale_LineEdit
module_8_sensor_1_location = module_1_info_win.channel_info_sensor1_location_Edit
module_8_sensor_1_name = module_1_info_win.channel_info_sensor1_nameLineEdit
module_1_info_win.channel_info_sensor1_TITLE
module_8_sensor_1_type = module_1_info_win.channel_info_sensor1_type_DropDown
# Ch 2
module_8_sensor_2_damping = module_1_info_win.channel_info_sensor2_dampingLineEdit
module_8_sensor_2_bandwidth = module_1_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
module_8_sensor_2_sensitivity = module_1_info_win.channel_info_sensor2_Sensitivity_LineEdit
module_8_sensor_2_name = module_1_info_win.channel_info_sensor2_nameLineEdit
module_8_sensor_2_type = module_1_info_win.channel_info_sensor2_type_DropDown
module_1_info_win.channel_info_sensor2_TITLE
module_8_sensor_2_location = module_1_info_win.channel_info_sensor2_location_Edit
module_8_sensor_2_fullscale = module_1_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
module_8_sensor_3_name = module_1_info_win.channel_info_sensor3_nameLineEdit
module_8_sensor_3_type = module_1_info_win.channel_info_sensor3_type_DropDown
module_8_sensor_3_sensitivity = module_1_info_win.channel_info_sensor3_Sensitivity_LineEdit
module_8_sensor_3_bandwidth = module_1_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
module_8_sensor_3_fullscale = module_1_info_win.channel_info_sensor3_full_scale_LineEdit
module_8_sensor_3_damping = module_1_info_win.channel_info_sensor3_dampingLineEdit
module_8_sensor_3_location = module_1_info_win.channel_info_sensor3_location_Edit
module_1_info_win.channel_info_sensor3_TITLE
# Ch 4
module_8_sensor_4_name = module_1_info_win.channel_info_sensor4_nameLineEdit
module_8_sensor_4_type = module_1_info_win.channel_info_sensor4_type_DropDown
module_8_sensor_4_sensitivity = module_1_info_win.channel_info_sensor4_Sensitivity_LineEdit
module_8_sensor_4_bandwidth = module_1_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
module_8_sensor_4_fullscale = module_1_info_win.channel_info_senson4_full_Scale_LineEdit
module_8_sensor_4_location = module_1_info_win.channel_info_sensor4_location_Edit
module_8_sensor_4_damping = module_1_info_win.channel_info_sensor4_dampingLineEdit
module_1_info_win.channel_info_sensor4_TITLE



# Visualize Sensor Selection
viz_sensor_sel_win.sensor_selection_NEXT_Button.clicked.connect(lambda: show_progress_dialog('Plotting ' + 'What you wanna plot'))
viz_sensor_sel_win.sensor_select_MAX_Label
viz_sens_1 = viz_sensor_sel_win.Sensor_1
viz_sens_2 = viz_sensor_sel_win.Sensor_2
viz_sens_3 = viz_sensor_sel_win.Sensor_3
viz_sens_4 = viz_sensor_sel_win.Sensor_4
viz_sens_5 = viz_sensor_sel_win.Sensor_5
viz_sens_6 = viz_sensor_sel_win.Sensor_6
viz_sens_7 = viz_sensor_sel_win.Sensor_7
viz_sens_8 = viz_sensor_sel_win.Sensor_8
viz_sens_9 = viz_sensor_sel_win.Sensor_9
viz_sens_10 = viz_sensor_sel_win.Sensor_10
viz_sens_11 = viz_sensor_sel_win.Sensor_11
viz_sens_12 = viz_sensor_sel_win.Sensor_12
viz_sens_13 = viz_sensor_sel_win.Sensor_13
viz_sens_14 = viz_sensor_sel_win.Sensor_14
viz_sens_15 = viz_sensor_sel_win.Sensor_15
viz_sens_16 = viz_sensor_sel_win.Sensor_16
viz_sens_17 = viz_sensor_sel_win.Sensor_17
viz_sens_18 = viz_sensor_sel_win.Sensor_18
viz_sens_19 = viz_sensor_sel_win.Sensor_19
viz_sens_20 = viz_sensor_sel_win.Sensor_20
viz_sens_21 = viz_sensor_sel_win.Sensor_21
viz_sens_22 = viz_sensor_sel_win.Sensor_22
viz_sens_23 = viz_sensor_sel_win.Sensor_23
viz_sens_24 = viz_sensor_sel_win.Sensor_24
viz_sens_25 = viz_sensor_sel_win.Sensor_25
viz_sens_26 = viz_sensor_sel_win.Sensor_26
viz_sens_27 = viz_sensor_sel_win.Sensor_27
viz_sens_28 = viz_sensor_sel_win.Sensor_28
viz_sens_29 = viz_sensor_sel_win.Sensor_29
viz_sens_30 = viz_sensor_sel_win.Sensor_30
viz_sens_31 = viz_sensor_sel_win.Sensor_31
viz_sens_32 = viz_sensor_sel_win.Sensor_32
visualization_sensor_selection_list = [viz_sens_1, viz_sens_2, viz_sens_3, viz_sens_4, viz_sens_5, viz_sens_6,
                                       viz_sens_7, viz_sens_8,
                                       viz_sens_9, viz_sens_10, viz_sens_11, viz_sens_12, viz_sens_13, viz_sens_14,
                                       viz_sens_15,
                                       viz_sens_15, viz_sens_16, viz_sens_17, viz_sens_18, viz_sens_19, viz_sens_20,
                                       viz_sens_21,
                                       viz_sens_22, viz_sens_23, viz_sens_24, viz_sens_25, viz_sens_26, viz_sens_27,
                                       viz_sens_28,
                                       viz_sens_29, viz_sens_30, viz_sens_31,
                                       viz_sens_32]  # Used to get values easily (goes from 0 to 31)

# Main Sensor Selection
main_sensor_sel_win.sensor_selection_DONE_Button.clicked.connect(
    lambda: action_begin_recording())  # Close() DONE in UI.
main_sensor_sel_win.sensor_select_MAX_Label
win_sens_1 = main_sensor_sel_win.Sensor_1
win_sens_2 = main_sensor_sel_win.Sensor_2
win_sens_3 = main_sensor_sel_win.Sensor_3
win_sens_4 = main_sensor_sel_win.Sensor_4
win_sens_5 = main_sensor_sel_win.Sensor_5
win_sens_6 = main_sensor_sel_win.Sensor_6
win_sens_7 = main_sensor_sel_win.Sensor_7
win_sens_8 = main_sensor_sel_win.Sensor_8
win_sens_9 = main_sensor_sel_win.Sensor_9
win_sens_10 = main_sensor_sel_win.Sensor_10
win_sens_11 = main_sensor_sel_win.Sensor_11
win_sens_12 = main_sensor_sel_win.Sensor_12
win_sens_13 = main_sensor_sel_win.Sensor_13
win_sens_14 = main_sensor_sel_win.Sensor_14
win_sens_15 = main_sensor_sel_win.Sensor_15
win_sens_16 = main_sensor_sel_win.Sensor_16
win_sens_17 = main_sensor_sel_win.Sensor_17
win_sens_18 = main_sensor_sel_win.Sensor_18
win_sens_19 = main_sensor_sel_win.Sensor_19
win_sens_20 = main_sensor_sel_win.Sensor_20
win_sens_21 = main_sensor_sel_win.Sensor_21
win_sens_22 = main_sensor_sel_win.Sensor_22
win_sens_23 = main_sensor_sel_win.Sensor_23
win_sens_24 = main_sensor_sel_win.Sensor_24
win_sens_25 = main_sensor_sel_win.Sensor_25
win_sens_26 = main_sensor_sel_win.Sensor_26
win_sens_27 = main_sensor_sel_win.Sensor_27
win_sens_28 = main_sensor_sel_win.Sensor_28
win_sens_29 = main_sensor_sel_win.Sensor_29
win_sens_30 = main_sensor_sel_win.Sensor_30
win_sens_31 = main_sensor_sel_win.Sensor_31
win_sens_32 = main_sensor_sel_win.Sensor_32
main_sensor_selection_list = [win_sens_1, win_sens_2, win_sens_3, win_sens_4, win_sens_5, win_sens_6, win_sens_7,
                              win_sens_8,
                              win_sens_9, win_sens_10, win_sens_11, win_sens_12, win_sens_13, win_sens_14, win_sens_15,
                              win_sens_15, win_sens_16, win_sens_17, win_sens_18, win_sens_19, win_sens_20, win_sens_21,
                              win_sens_22, win_sens_23, win_sens_24, win_sens_25, win_sens_26, win_sens_27, win_sens_28,
                              win_sens_29, win_sens_30, win_sens_31,
                              win_sens_32]  # Used to get values easily (goes from 0 to 31)

# Acquiring Something
prog_dlg.progress_dialog_STOP_button.clicked.connect(lambda: action_cancel_everything())
dlg_prog_bar = prog_dlg.progress_dialog_progressBar
dlg_title = prog_dlg.progress_dialog_title

# Select Module for Channel Info.
mod_1_button = mod_sel_win.module_selection_Module1
mod_1_button.clicked.connect(lambda: show_channel_info_window(0))

mod_2_button = mod_sel_win.module_selection_Module2
mod_2_button.clicked.connect(lambda: show_channel_info_window(1))

mod_3_button = mod_sel_win.module_selection_Module3
mod_3_button.clicked.connect(lambda: show_channel_info_window(2))

mod_4_button = mod_sel_win.module_selection_Module4
mod_4_button.clicked.connect(lambda: show_channel_info_window(3))

mod_5_button = mod_sel_win.module_selection_Module5
mod_5_button.clicked.connect(lambda: show_channel_info_window(4))

mod_6_button = mod_sel_win.module_selection_Module6
mod_6_button.clicked.connect(lambda: show_channel_info_window(5))

mod_7_button = mod_sel_win.module_selection_Module7
mod_7_button.clicked.connect(lambda: show_channel_info_window(6))

mod_8_button = mod_sel_win.module_selection_Module8
mod_8_button.clicked.connect(lambda: show_channel_info_window(7))

module_button_list = [mod_1_button, mod_2_button, mod_3_button, mod_4_button, mod_5_button, mod_6_button,
                      mod_7_button, mod_8_button]


# File System
file_sys_win.file_system_treeView
file_sys_win.file_system_OPEN_button
file_sys_win.file_system_CANCEL_button

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  Main Tab Window  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Menu Bar
main_window.action_Help.triggered.connect(lambda: openUrl())
def openUrl():
    url = QtCore.QUrl('https://github.com/jrsm1/EWAS_Application/blob/master/README.md')
    if not QtGui.QDesktopServices.openUrl(url):
        show_error('Could not open Help URL')


main_window.action_Diagnose.triggered.connect(lambda: send_diagnostics())
def send_diagnostics():
    try:
        im = ins_man.instruction_manager(ins_port)
        im.send_diagnose_request()
    except serial.SerialException:
        show_not_connected_error()


main_window.actionTime.triggered.connect(lambda: time_plot())
def time_plot():
    show_visualization_sensor_selector_window()
    enable_main_start_connected_sensors()


# RECORDING  Settings
main_window.main_tab_RecordingSettings_LOAD_SETTINGS_Button.clicked.connect(lambda: handle_loading_saving('load', 1))
main_window.main_tab_RecordingSettings__SAVE_button.clicked.connect(lambda: handle_loading_saving('save', 1))
rec_name_edit = main_window.main_tab_RecordingSettings_name_LineEdit
rec_duration_edit = main_window.main_tab_RecordingSettings_durationLineEdit
rec_type_dropdown = main_window.main_tab_RecordingSettings_type_DropDown
delay_edit = main_window.main_tab_RecordingSettings_delay_LineEdit
# Localization Settings
main_window.main_tab_LocalizationSettings_acquire_GPS_Button.clicked.connect(lambda: sync_gps())
loc_type_dropdown = main_window.main_tab_LocalizationSettings_type_DropBox
loc_type_dropdown.currentIndexChanged.connect(lambda: change_local_allowed())
main_window.main_tab_LocalizationSettings_Name_lineEdit
main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button.clicked.connect(lambda: handle_loading_saving('load', 2))
main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button.clicked.connect(lambda: handle_loading_saving('save', 2))
main_window.main_tab_LocalizationSettings_longitudLineEdit
main_window.main_tab_LocalizationSettings_latitudLineEdit
main_window.main_tab_LocalizationSettings_hourLineEdit
main_window.main_tab_LocalizationSettings_minutesLineEdit
main_window.main_tab_LocalizationSettings_secondsLineEdit
# connecting close event
main_window.closeEvent = close_event

loc_gps_frame = main_window.main_tab_location_gps_frame
loc_specimen_frame = main_window.specimen_location_frame
### Module Loc. Settings
specimen_loc_1 = main_window.main_tab_module_loc_LineEdit_1
specimen_loc_2 = main_window.main_tab_module_loc_LineEdit_2
specimen_loc_3 = main_window.main_tab_module_loc_LineEdit_3
specimen_loc_4 = main_window.main_tab_module_loc_LineEdit_4
specimen_loc_5 = main_window.main_tab_module_loc_LineEdit_5
specimen_loc_6 = main_window.main_tab_module_loc_LineEdit_6
specimen_loc_7 = main_window.main_tab_module_loc_LineEdit_7
specimen_loc_8 = main_window.main_tab_module_loc_LineEdit_8
# Data Acquisition Settings
main_window.main_tab_DAQParams_SAVE_PARAMS_button.clicked.connect(lambda: handle_loading_saving('save', 3))  # TODO
main_window.main_tab_DAQParams_LOAD_PARAMS_button.clicked.connect(lambda: handle_loading_saving('load', 3))
# main_window.main_tab_DAQParams_ADC_Constant_Label
samfreq_dropdown = main_window.main_tab_DAQParams_samplingRate_DropDown
cutfreq_drodown = main_window.main_tab_DAQParams_Cutoff_Frequency_DropDown
cutfreq_drodown.currentIndexChanged.connect(lambda: suggest_sampling_freq())
gain_dropdown = main_window.main_tab_DAQParams_gain_DropDown
main_window.main_tab_CHANNEL_INFO_button.clicked.connect(lambda: False)
main_window.main_tab_START_button.clicked.connect(lambda: start_acquisition())
# File Name
fn_in = filename_input_win.filename_lineEdit
fn_in.returnPressed.connect(lambda: do_saving_loading_action())
fn_OK_btn = filename_input_win.filename_OK_button.clicked.connect(lambda: do_saving_loading_action())
fn_CANCEL_btn = filename_input_win.filename_CANCEL_button.clicked.connect(lambda: filename_input_win.close())
fn_EXPLORER_btn = filename_input_win.open_FILE_EXPLORER_Button.clicked.connect(file_choose)


# ----------------------------------------------- MAIN WINDOW ------------------------------------------------------
def suggest_sampling_freq():
    samfreq_dropdown.setCurrentIndex(cutfreq_drodown.currentIndex())


def action_begin_recording():
    """
    Prepares GUI and sends request to control module for begin recording data.
    """
    # Send Setting Information to Control Module.
    try:
        ins = ins_man.instruction_manager(ins_port)
        ins.send_set_configuration(setting_data_manager.settings_to_string())
        # TODO Prepare Real-Time Plot to receive Data.
        # Send Begin Recording FLAG to Control Module.
        ins.send_request_start()
        # Close Window
        main_sensor_sel_win.close()
        check_status_during_test()
    except serial.SerialException:
        show_not_connected_error()


def check_status_during_test():
    show_acquire_dialog('GPS Signal')
    prog_dlg.progress_dialog_progressBar.setMaximum(100)
    prog_dlg.progress_dialog_progressBar.setValue(0)
    try:
        ins = ins_man.instruction_manager(ins_port)
        timeout = 0
        test_successful = True  # Used to not request data if synched==False.
        duration = daq_config.recording_configs['test_duration']
        time_to_update_progress_bar = (duration/100)+2
        bar_value = 0
        while ins.send_request_status()[0] != 1:  # Status[2] --> gps_synched
            if log: print('Waiting for test to finish....')
            sleep(1)  # Wait for half a second before asking again.
            timeout += 1
            if timeout == time_to_update_progress_bar:
                timeout = 0
                prog_dlg.progress_dialog_progressBar.setValue(++bar_value)
                app.processEvents()
        if test_successful:
            prog_dlg.close()

            set_gps_into_gui()
    except serial.SerialException:
        show_not_connected_error()
        prog_dlg.close()


def action_cancel_everything():
    """
    Sends signal to Control Module to cancel all recording, storing, sending, synchronizing and/or
    any other process the system might be doing.

    Called by user when CANCEL action is desired.
    """
    try:
        ins = ins_man.instruction_manager(ins_port)
        ins.send_cancel_request()
        enable_main_window()
    except serial.SerialException:
        show_not_connected_error()


def ask_for_sensors():
    """
    Shows the Main Sensor Selection Window.

    CALL BEFORE SENDING REQUEST TO START.
    """
    # User Select which sensors it wants.
    show_main_sens_sel_window()
    # When Done pressed --> begin recording. | this is handled from UI.


# ************** STORING / LOADING *******************
load_save_instructions = {
    'action': '',
    'who_to_save': 0,
    'who_to_load': 0
}


def handle_loading_saving(what: str, who: int):
    """
    Prepares the logic that decides the desired loading/saving action.
    This Method contains information gathered from the user button press.
    """
    # show_filename_editor_window()
    # file_choose()

    load_save_instructions['action'] = what
    if (who == 0) or (what == ''):
        show_error('There has been an ERROR knowing what you want to do. Please Try Again.')
        if log: print('Loading Error.')
    else:
        if what == 'save':
            load_save_instructions['who_to_save'] = who
        elif what == 'load':
            load_save_instructions['who_to_load'] = who

    do_saving_loading_action()


def do_saving_loading_action():
    """
    Function continues to correct method depending on saving/loading and option combinations.
    """
    filename_input_win.close()
    if load_save_instructions['action'] == 'save':
        decide_who_to_save(load_save_instructions['who_to_save'])
    elif load_save_instructions['action'] == 'load':
        decide_who_to_load(load_save_instructions['who_to_load'])


def decide_who_to_save(instruction: int):
    """
    Based on Button Pressed, decides what to save.
    """
    if instruction == 1:  # Save Recording Settings
        action_store_Rec_Setts()
    elif instruction == 2:
        action_store_Location()
    elif instruction == 3:
        action_store_DAQ_Params()
    elif instruction == 4:
        action_store_module_info()


def decide_who_to_load(instruction: int):
    """
    Based on Button Pressed, decides what to load.
    """
    if instruction == 1:  # Save Recording Settings
        action_load_Rec_Setts()
    elif instruction == 2:
        action_load_Location()
    elif instruction == 3:
        action_load_DAQ_Params()
    elif instruction == 4:
        action_load_module_info()

def validate_filename(filename: str):
    """
    Validates filename has a CSV File Extension.

    :param filename: The User Input filename to validate.

    :return: True if the file extension is '.csv'
    """
    validated = filename.lower().endswith('.csv')

    if not validated:
        show_error('The File must have a *.csv file extension.')
        if log: print('File Extension Validation: FAILED')

    return validated

# ****** ACTIONS STORE/LOAD **********

def action_store_DAQ_Params():
    # TODO Make Sure Files are not empty.
    # Get filename from User
    # show_filename_editor_window()
    filename = fn_in.text()
    if validate_filename(filename):
        # Get info from GUI.
        get_daq_params_from_gui()
        # Save to File.
        setting_data_manager.store_signal_params(filename)
        # Close Window
        filename_input_win.close()


def action_load_DAQ_Params():
    relative_path = 'Config/DAQ/Signal'
    # Get filename from User
    filename = file_choose(relative_path)
    # Load Params from File
    setting_data_manager.load_signal_params(filename)

    if set_dat_man.verify_file_exists(filename):
        # Set Params into GUI.
        set_daq_params_to_gui()
        # Close Window
        filename_input_win.close()


def action_store_Location():
    # TODO Make Sure Files are not empty.
    # Get filename from User
    show_filename_editor_window()
    filename = fn_in.text()
    if validate_filename(filename):
        # Get info from GUI.
        # get_location_from_gui()
        loc_type = main_window.main_tab_LocalizationSettings_type_DropBox.currentIndex()
        if not loc_type: # FIXME ESTE IF NO HACE NADA.
            if not validate_gps_location_settings():
                # Save to File.
                setting_data_manager.store_location_configs(filename)
                # Close Window
                filename_input_win.close()
            else:
                show_error(validate_gps_location_settings())
        else:
            if not validate_module_location_settings():
                # Save to File.
                setting_data_manager.store_location_configs(filename)
                # Close Window
                filename_input_win.close()
            else:
                show_error(validate_module_location_settings())


def action_load_Location():
    relative_path = 'Config/DAQ/Location'
    # Get filename from User
    filename = file_choose(relative_path)
    # Load Params from File
    setting_data_manager.load_location_configs(filename)

    if set_dat_man.verify_file_exists(relative_path + filename):
        # Set Params into GUI.
        load_local_settings_to_gui()
        # Close Window
        filename_input_win.close()


def action_store_Rec_Setts():
    # TODO Make Sure Files are not empty.
    # Get filename from User
    show_filename_editor_window()
    filename = fn_in.text()
    if validate_filename(filename):
        if not validate_rec_settings(): # Validation calls get_rec_setts_from_gui()
            # Save to File.
            setting_data_manager.store_recording_configs(filename)
            # Close Window
            filename_input_win.close()
        else:
            show_error(validate_rec_settings())


def action_load_Rec_Setts():
    relative_path = 'Config/DAQ/Recording'
    # Get filename from User
    filename = file_choose(relative_path)

    # Load Params from File
    setting_data_manager.load_recording_configs(filename)
    if set_dat_man.verify_file_exists(filename):
        # Set Params into GUI.
        set_recording_into_gui()
        # Close Window
        filename_input_win.close()


# ********************************************* LOCATION ***************************************************************
def sync_gps():  # TODO TEST
    # disable_main_window()  # NOT Going to do. --> failed to re-enable correctly in all cases.
    # Show Progress Dialog.
    show_acquire_dialog('GPS Signal')
    prog_dlg.progress_dialog_progressBar.setMaximum(100)
    # prog_dlg.progress_dialog_progressBar.setValue(-1)
    try:
        ins = ins_man.instruction_manager(ins_port)
        ins.send_gps_sync_request()
        timeout = 0
        time_to_sleep = 0.5
        synched = True  # Used to not request data if synched==False.
        while ins.send_request_status()[2] != 1:  # Status[2] --> gps_synched
            if log: print('GPS Waiting....')
            sleep(0.500)  # Wait for half a second before asking again.
            timeout += 1
            prog_dlg.progress_dialog_progressBar.setValue(timeout*5)
            app.processEvents()
            if timeout == 10 * 2:  # = [desired timeout in seconds] * [1/(sleep value)]
                # prog_dlg.close()
                show_error('GPS Failed to Synchronize.')
                synched = False
                break
        # If synched Succesfull --> Request GPS data.
        if synched:
            ins.send_gps_data_request()
            set_gps_into_gui()
    except serial.SerialException:
        show_not_connected_error()
        prog_dlg.close()


def load_local_settings_to_gui():
    """
    Loads Settings already in the program to GUi components depending on location type selected by user.
    The fields for the types not selected will be disabled.
    """
    if log: print(loc_type_dropdown.currentIndex())

    if loc_type_dropdown.currentIndex() == 0:  # GPS
        loc_gps_frame.setEnabled(True)
        loc_specimen_frame.setEnabled(False)
        set_gps_into_gui()

    elif loc_type_dropdown.currentIndex() == 1:  # Specimen
        loc_gps_frame.setEnabled(False)
        loc_specimen_frame.setEnabled(True)
        set_specimen_location_into_gui()


def change_local_allowed():
    if log: print(loc_type_dropdown.currentIndex())

    if loc_type_dropdown.currentIndex() == 0:  # GPS
        loc_gps_frame.setEnabled(True)
        loc_specimen_frame.setEnabled(False)

    elif loc_type_dropdown.currentIndex() == 1:  # Specimen
        loc_gps_frame.setEnabled(False)
        loc_specimen_frame.setEnabled(True)


# ---------------------------------------------- MODULE INFORMATION----------------------------------------------------

def action_store_module_info():
    pass
# """
# Loads fields from Channel info data structure into GUI.
# """
# def load_channel_to_gui():
#     sens_1 = chan.
#
#
# def load_channel_from_file():
#     channel =

# ----------------------------------------------- ACQUIRE DIALOG -----------------------------------------------------


def show_acquire_dialog(message: str):
    """
    Shows Dialog with 'Acquiring' as the title beginning.

    :param message : the desired dialog message.
    """
    # Set progress is default to undetermined.
    # Show Dialog & Set Message
    show_progress_dialog('Acquiring ' + message)

    # Enable Main Window when done.  # FIXME Change to correct function.
    # enable_main_window()


# ****************************************** SENSOR & MODULE INFORMATION *********************************************
def save_module_info(module: int):
    """
    Saves sensor data from UI into structure.
    """
    # Get info from GUI.
    try:
        ins = ins_man.instruction_manager(ins_port)
        connected_module_list = ins.send_request_number_of_mods_connected()
        if log: print("entered enable start")
        if connected_module_list[0]:
            sensors_all[0] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_1_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_1_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_1_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_1_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_1_sensor_1_damping.text()),
                                                      sensor_localization=str(module_1_sensor_1_location.text()) )
            sensors_all[1] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_1_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_1_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_1_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_1_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_1_sensor_2_damping.text()),
                                                      sensor_localization=str(module_1_sensor_2_location.text()) )

            sensors_all[2] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_1_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_1_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_1_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_1_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_1_sensor_3_damping.text()),
                                                      sensor_localization=str(module_1_sensor_3_location.text()))

            sensors_all[3] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_1_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_1_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_1_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_1_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_1_sensor_4_damping.text()),
                                                      sensor_localization=str(module_1_sensor_4_location.text()))

            modules_all[0].channel_info['Sensor 1'] = sensors_all[0]
            modules_all[0].channel_info['Sensor 1'] = sensors_all[1]
            modules_all[0].channel_info['Sensor 1'] = sensors_all[2]
            modules_all[0].channel_info['Sensor 1'] = sensors_all[3]
            setting_data_manager.store_module_configs(get_filename(), modules_all[0])

        if connected_module_list[1]:
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_2_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_2_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_2_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_2_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_2_sensor_1_damping.text()),
                                                      sensor_localization=str(module_2_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_2_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_2_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_2_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_2_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_2_sensor_2_damping.text()),
                                                      sensor_localization=str(module_2_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_2_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_2_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_2_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_2_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_2_sensor_3_damping.text()),
                                                      sensor_localization=str(module_2_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_2_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_2_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_2_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_2_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_2_sensor_4_damping.text()),
                                                      sensor_localization=str(module_2_sensor_4_location.text()))
        if connected_module_list[2]:  # MODULE 3
            sensors_all[8] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_3_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_3_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_3_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_3_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_3_sensor_1_damping.text()),
                                                      sensor_localization=str(module_3_sensor_1_location.text()))

            sensors_all[9] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_3_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_3_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_3_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_3_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_3_sensor_2_damping.text()),
                                                      sensor_localization=str(module_3_sensor_2_location.text()))

            sensors_all[10] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_3_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_3_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_3_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_3_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_3_sensor_3_damping.text()),
                                                      sensor_localization=str(module_3_sensor_3_location.text()))

            sensors_all[11] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_3_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_3_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_3_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_3_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_3_sensor_4_damping.text()),
                                                      sensor_localization=str(module_3_sensor_4_location.text()))
        if connected_module_list[3]:  # MODULE 4
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_4_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_4_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_4_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_4_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_4_sensor_1_damping.text()),
                                                      sensor_localization=str(module_4_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_4_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_4_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_4_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_4_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_4_sensor_2_damping.text()),
                                                      sensor_localization=str(module_4_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_4_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_4_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_4_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_4_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_4_sensor_3_damping.text()),
                                                      sensor_localization=str(module_4_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_4_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_4_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_4_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_4_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_4_sensor_4_damping.text()),
                                                      sensor_localization=str(module_4_sensor_4_location.text()))
        if connected_module_list[4]: # MODULE 5
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_5_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_5_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_5_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_5_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_5_sensor_1_damping.text()),
                                                      sensor_localization=str(module_5_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_5_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_5_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_5_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_5_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_5_sensor_2_damping.text()),
                                                      sensor_localization=str(module_5_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_5_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_5_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_5_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_5_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_5_sensor_3_damping.text()),
                                                      sensor_localization=str(module_5_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_5_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_5_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_5_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_5_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_5_sensor_4_damping.text()),
                                                      sensor_localization=str(module_5_sensor_4_location.text()))
        if connected_module_list[5]:  # MODULE 6
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_6_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_6_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_6_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_6_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_6_sensor_1_damping.text()),
                                                      sensor_localization=str(module_6_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_6_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_6_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_6_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_6_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_6_sensor_2_damping.text()),
                                                      sensor_localization=str(module_6_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_6_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_6_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_6_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_6_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_6_sensor_3_damping.text()),
                                                      sensor_localization=str(module_6_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_6_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_6_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_6_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_6_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_6_sensor_4_damping.text()),
                                                      sensor_localization=str(module_6_sensor_4_location.text()))
        if connected_module_list[6]:  # MODULE 7
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_7_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_7_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_7_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_7_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_7_sensor_1_damping.text()),
                                                      sensor_localization=str(module_7_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_7_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_7_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_7_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_7_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_7_sensor_2_damping.text()),
                                                      sensor_localization=str(module_7_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_7_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_7_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_7_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_7_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_7_sensor_3_damping.text()),
                                                      sensor_localization=str(module_7_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_7_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_7_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_7_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_7_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_7_sensor_4_damping.text()),
                                                      sensor_localization=str(module_7_sensor_4_location.text()))
        if connected_module_list[7]: # MODULE 8
            sensors_all[4] = Sensor_Individual.Sensor(sensor_name='Sensor_1',
                                                      sensor_type=module_8_sensor_1_type.currentIndex(),
                                                      sensor_sensitivity=str(module_8_sensor_1_sensitivity.text()),
                                                      sensor_bandwidth=str(module_8_sensor_1_bandwidth.text()),
                                                      sensor_full_scale=str(module_8_sensor_1_fullscale.text()),
                                                      sensor_damping=str(module_8_sensor_1_damping.text()),
                                                      sensor_localization=str(module_8_sensor_1_location.text()))

            sensors_all[5] = Sensor_Individual.Sensor(sensor_name='Sensor_2',
                                                      sensor_type=module_8_sensor_2_type.currentIndex(),
                                                      sensor_sensitivity=str(module_8_sensor_2_sensitivity.text()),
                                                      sensor_bandwidth=str(module_8_sensor_2_bandwidth.text()),
                                                      sensor_full_scale=str(module_8_sensor_2_fullscale.text()),
                                                      sensor_damping=str(module_8_sensor_2_damping.text()),
                                                      sensor_localization=str(module_8_sensor_2_location.text()))

            sensors_all[6] = Sensor_Individual.Sensor(sensor_name='Sensor_3',
                                                      sensor_type=module_8_sensor_3_type.currentIndex(),
                                                      sensor_sensitivity=str(module_8_sensor_3_sensitivity.text()),
                                                      sensor_bandwidth=str(module_8_sensor_3_bandwidth.text()),
                                                      sensor_full_scale=str(module_8_sensor_3_fullscale.text()),
                                                      sensor_damping=str(module_8_sensor_3_damping.text()),
                                                      sensor_localization=str(module_8_sensor_3_location.text()))

            sensors_all[7] = Sensor_Individual.Sensor(sensor_name='Sensor_4',
                                                      sensor_type=module_8_sensor_4_type.currentIndex(),
                                                      sensor_sensitivity=str(module_8_sensor_4_sensitivity.text()),
                                                      sensor_bandwidth=str(module_8_sensor_4_bandwidth.text()),
                                                      sensor_full_scale=str(module_8_sensor_4_fullscale.text()),
                                                      sensor_damping=str(module_8_sensor_4_damping.text()),
                                                      sensor_localization=str(module_8_sensor_4_location.text()))
        if log: print("got out of enable start connected sensors")
        # If not Connected to not continue.
    except serial.SerialException:
        continuar = False
        show_not_connected_error()

    # Set info to correct Data Structure.
    # Set sensor info (4)
    sens_1 = sens.Sensor('NAME', 0)
    sens_2 = sens.Sensor('NAME', 0)
    sens_3 = sens.Sensor('NAME', 0)
    sens_4 = sens.Sensor('NAME', 0)

    # Set channel sensors.
    channel = chan.Module('NAME', sens_1, sens_2, sens_3, sens_4)


# ------------------------------------------------ VISUALIZATION ------------------------------------------------------


def plot_time(filename: str):
    """
    [1]
    Creates and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plt_time().show_plot(
        'RESPECT TO TIME')  # TODO SWITCH TO FILENAME FILE.


def plot_fft(filename: str, sensor: str, freq: int):
    """
    [2]
    Creats and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_fft('S1', 100).show_plot(
        'FOURIER TRANSFORM')  # TODO SWITCH TO FILENAME FILE.


def plot_aps(filename: str, sensor: str, freq: int):
    """
    [3]
    Creates and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_PSD('S1', 100).show_plot(
        'AUTO-POWER SPECTRA')  # TODO SWITCH TO FILENAME FILE.


def plot_cps(filename: str):
    """
    [4]
    Creates and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_CSD().show_plot(
        'CROSS-POWER SPECTRA')  # TODO SWITCH TO FILENAME FILE.


def plot_phase(filename: str):
    """
    [5]
    Creates and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_Phase().show_plot(
        'UNWRAPPED PHASE FUNCTION')  # TODO SWITCH TO FILENAME FILE.


def plot_cohere(filename: str):
    """
    [6]
    Creates and Opens Window with Time plot using user information from file.
    """
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_coherence().show_plot(
        'COHERENCE')  # TODO SWITCH TO FILENAME FILE.


def init():
    """
    Beginning of the program.
    Main will redirect here for GUI setup.
    """
    global ins_port
    main_window.show()
    loc_specimen_frame.setEnabled(False)  # Begin with GPS only enabled.
    ins_port = save_port()

    if ins_port == 'COM-1':
        show_error('Device Not Connected. Please try again.')
        sleep(2.0)
        # sys.exit()
    else:
        sync_gps()

    # --------- TESTING ------------
    # get_rec_setts_from_gui()
    # setting_data_manager.store_daq_configs('Testing_Configs.csv')
    # set_recording_into_gui()
    # set_daq_params_to_gui()
    # load_gps_into_gui()
    # load_local_settings_to_gui()
    # show_progress_dialog('Message')
    # sensor_sel.show()
    # mod_sel.show()
    # channel_info_win.show()
    # show_acquire_dialog('SOMETHING')
    # show_main_sens_sel_window()
    # show_visualization_sensor_selector_window()

    sys.exit(app.exec_())
