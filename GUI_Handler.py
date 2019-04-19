# import PyQt5
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from time import sleep

from Control_Module_Comm import instruction_manager as ins_man
from Control_Module_Comm.Structures import Channel_Individual as chan, Sensor_Individual as sens
from Data_Processing import Plot_Data
from Control_Module_Comm.Structures import Channel_Individual, DAQ_Configuration, Sensor_Individual
from Settings import setting_data_manager as set_dat_man

app = QtWidgets.QApplication([])
main_window = uic.loadUi("GUI/main_window.ui")
channel_info_win = uic.loadUi("GUI/channel_info_window.ui")
prog_dlg = uic.loadUi("GUI/progress_dialog_v1.ui")
viz_sensor_sel_win = uic.loadUi('GUI/visualize_sensor_selection_matrix.ui')
main_sensor_sel_win = uic.loadUi('GUI/main_sensor_selection_matrix.ui')
mod_sel_win = uic.loadUi('GUI/module_selection_window.ui')
file_sys_win = uic.loadUi('GUI/file_system_window.ui')

main_window.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
channel_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
prog_dlg.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
viz_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
main_sensor_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
mod_sel_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
file_sys_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))


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
ch_1 = Channel_Individual.Channel('Channel 1', sens_1, sens_2, sens_3, sens_4)
ch_2 = Channel_Individual.Channel('Channel 2', sens_5, sens_6, sens_7, sens_8)
ch_3 = Channel_Individual.Channel('Channel 3', sens_9, sens_10, sens_11, sens_12)
ch_4 = Channel_Individual.Channel('Channel 4', sens_13, sens_14, sens_15, sens_16)
ch_5 = Channel_Individual.Channel('Channel 5', sens_17, sens_18, sens_19, sens_20)
ch_6 = Channel_Individual.Channel('Channel 6', sens_21, sens_22, sens_23, sens_24)
ch_7 = Channel_Individual.Channel('Channel 7', sens_25, sens_26, sens_27, sens_28)
ch_8 = Channel_Individual.Channel('Channel 8', sens_29, sens_30, sens_31, sens_32)
channels_all = [ch_1, ch_2, ch_3, ch_4, ch_5, ch_6, ch_7, ch_8]  # Used to get channels easily (goes from 0 to 7)

# ----------- CONFIGS ----------
daq_config = DAQ_Configuration.DAQconfigs()

# setting_data_manager = set_dat_man.Setting_File_Manager(daq_con=daq_config)

# testing purposes
log = 1

"""
Displays Main Window on Computer's Screen.
"""
def show_main_window():
    main_window.show()


"""
    Disables Input for every Widget inside Main Window.
"""
def disable_main_window():
    main_window.setEnabled(False)


"""
    Disables Input for every Widget inside Main Window.
"""
def enable_main_window():
    main_window.setEnabled(True)


"""
    Creates an Error Message dialog
    
    :param message: String - The Desired Message Output.
"""
def show_error(message: str):
    err_dlg = QtWidgets.QErrorMessage()
    err_dlg.showMessage(message)
    err_dlg.exec()


"""
Opens Module Selection Window.
Done before Channel Selection.
"""
def open_module_selection_window():
    mod_sel_win.show()

"""
    Opens Channel Information Window
"""
def show_channel_info_window(channel: int):
    # TODO DECIDE SENSOR NAMES BASED ON CHANNEL.
    # TODO VERIFY IF THE SENSORS IN THE CHANNEL ARE CONNECTED.
    # TODO ENABLE MODULE SELECTION BUTTONS BASED ON CONNECTED SENSORS.
    # LATER TODO SAVE CORRECT VALUES FOR CHANNEL.

    # Close Mosule Selection Window now as it will not do anything. --> Open after module settings are saved.
    mod_sel_win.close()

    chan_mod_name.setTextFormat(1)  # Qt::RichText	1
    # TODO Format Texts

    # Decide which Module the user has selected.
    if channel == 0:
        chan_mod_name.setText('Module 1')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 1')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_1')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 2')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_2')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 3')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_3')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 4')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_4')
    elif channel == 1:
        chan_mod_name.setText('Module 2')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 5')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_5')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 6')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_6')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 7')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_7')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 8')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_8')
    elif channel == 2:
        chan_mod_name.setText('Module 3')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 9')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_9')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 10')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_10')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 11')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_11')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 12')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_12')
    elif channel == 3:
        chan_mod_name.setText('Module 4')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 13')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_13')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 14 ')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_14')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 15')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_15')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 16')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_16')
    elif channel == 4:
        chan_mod_name.setText('Module 5')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 17')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_17')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 18')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_18')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 19')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_19')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 20')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_20')
    elif channel == 5:
        chan_mod_name.setText('Module 6')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 21')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_21')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 22')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_22')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 23')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_23')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 24')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_24')
    elif channel == 6:
        chan_mod_name.setText('Module 7')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 25')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_25')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 26')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_26')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 27')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_27')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 28')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_28')
    elif channel == 7:
        chan_mod_name.setText('Module 8')
        channel_info_win.channel_info_sensor1_TITLE.setText('Sensor 29')
        channel_info_win.channel_info_sensor1_nameLineEdit.setPlaceholderText('Sensor_29')
        channel_info_win.channel_info_sensor2_TITLE.setText('Sensor 30')
        channel_info_win.channel_info_sensor2_nameLineEdit.setPlaceholderText('Sensor_30')
        channel_info_win.channel_info_sensor3_TITLE.setText('Sensor 31')
        channel_info_win.channel_info_sensor3_nameLineEdit.setPlaceholderText('Sensor_31')
        channel_info_win.channel_info_sensor4_TITLE.setText('Sensor 32')
        channel_info_win.channel_info_sensor4_nameLineEdit.setPlaceholderText('Sensor_32')

    channel_info_win.show()


"""
    Opens Sensor Selection Window for Recording
"""
def show_main_sens_sel_window():
    disable_main_window()
    main_sensor_sel_win.show()


"""
Creates and Opens Progress Dialog.
Default is to 'undetermined' infinite progress. 
To change default behaviour use { void QProgressBar::setRange(int minimum, int maximum) }

:param message : Custom message to show on Dialog.
"""
def show_progress_dialog(message: str):
    dlg_title.setText(message)
    prog_dlg.show()


def show_visualization_sensor_selector_window(plot: int):  # TODO
    viz_sensor_sel_win.show()

"""
Begins Visualization Analysis for user selected plots.
"""
def begin_visualization(plot: int):
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


"""
Sets GPS information on current settings into GUI fields.
"""
def set_gps_into_gui():
    loc_type_dropdown.setCurrentIndex(0)  # Set to GPS in Drop Down.
    main_window.main_tab_LocalizationSettings_Name_lineEdit.setText(daq_config.location_configs['loc_name'])
    main_window.main_tab_LocalizationSettings_longitudLineEdit.setText(daq_config.location_configs['longitude'])
    main_window.main_tab_LocalizationSettings_latitudLineEdit.setText(daq_config.location_configs['latitude'])
    main_window.main_tab_LocalizationSettings_hourLineEdit.setText(daq_config.location_configs['hour'])
    main_window.main_tab_LocalizationSettings_minutesLineEdit.setText(daq_config.location_configs['minute'])
    main_window.main_tab_LocalizationSettings_secondsLineEdit.setText(daq_config.location_configs['second'])


"""
Sets Specimen Location information on current settings into GUI fields.
"""
def set_specimen_location_into_gui():
    specimen_loc_1.setText(daq_config.specimen_location['1'])
    specimen_loc_2.setText(daq_config.specimen_location['2'])
    specimen_loc_3.setText(daq_config.specimen_location['3'])
    specimen_loc_4.setText(daq_config.specimen_location['4'])
    specimen_loc_5.setText(daq_config.specimen_location['5'])
    specimen_loc_6.setText(daq_config.specimen_location['6'])
    specimen_loc_7.setText(daq_config.specimen_location['7'])
    specimen_loc_8.setText(daq_config.specimen_location['8'])


"""
Sets Recording settings to GUI Fields.
"""
def set_recording_into_gui():
    rec_name_edit.setText(daq_config.recording_configs['test_name'])
    rec_id_edit.setText(daq_config.recording_configs['test_ID'])
    rec_duration_edit.setText(str(daq_config.recording_configs['test_duration'])) # Convert int to String for compatibility.
    rec_type_dropdown.setCurrentIndex(daq_config.recording_configs['test_type'])

    if daq_config.data_handling_configs['visualize']:
        rec_viz_checkbox.setCheckState(2)  # Qt::Checked	2
    else:
        rec_viz_checkbox.setCheckState(0)

    if daq_config.data_handling_configs['store']:
        rec_store_checkbox.setCheckState(2)
    else:
        rec_store_checkbox.setCheckState(0)  # Qt::Unchecked	0


"""
Sets Data Acquisition Parameters to GUI Fields.
"""
def set_daq_params_to_gui():
    samfreq_dropdown.setCurrentIndex(daq_config.signal_configs['sampling_rate'])
    cutfreq_drodown.setCurrentIndex(daq_config.signal_configs['cutoff_frequency'])
    gain_dropdown.setCurrentIndex(daq_config.signal_configs['signal_gain'])

"""
Gets all the data from fields in Main Window
"""
def snapshot_data():
    # we have to change everything to string, because that's how it's going to get passed
    # main tab recording settings
    name = main_window.main_tab_RecordingSettings_name_LineEdit.text()
    recording_name_id = main_window.main_tab_RecordingSettings_id_LineEdit.text()
    duration = main_window.main_tab_RecordingSettings_durationLineEdit.text()
    """
    QComboBox, which are the dropdown needs currentText()
    it has to be casted to string
    """
    type = str(main_window.main_tab_RecordingSettings_type_DropDown.currentText())
    """
    QCheckbox, needs checkState() to get the state.
    there are two states.
    2 = checked
    0 = unchecked
    it has to be 
    """
    vis_bool = str(main_window.main_tab_RecordingSettings_visualize_checkBox.checkState())
    store_bool = str(main_window.main_tab_RecordingSettings_store_checkBox.checkState())

    # main tab localization settings
    loc_type = str(main_window.main_tab_LocalizationSettings_type_DropBox.currentText())
    loc_name = main_window.main_tab_LocalizationSettings_Name_lineEdit.text()
    loc_longitude = main_window.main_tab_LocalizationSettings_longitudLineEdit.text()
    loc_latitude = main_window.main_tab_LocalizationSettings_latitudLineEdit.text()
    loc_hour = main_window.main_tab_LocalizationSettings_hourLineEdit.text()
    loc_minutes = main_window.main_tab_LocalizationSettings_minutesLineEdit.text()
    loc_seconds = main_window.main_tab_LocalizationSettings_secondsLineEdit.text()

    # specimen by module
    module_loc1 = main_window.main_tab_module_loc_LineEdit_1.text()
    module_loc2 = main_window.main_tab_module_loc_LineEdit_2.text()
    module_loc3 = main_window.main_tab_module_loc_LineEdit_3.text()
    module_loc4 = main_window.main_tab_module_loc_LineEdit_4.text()
    module_loc5 = main_window.main_tab_module_loc_LineEdit_5.text()
    module_loc6 = main_window.main_tab_module_loc_LineEdit_6.text()
    module_loc7 = main_window.main_tab_module_loc_LineEdit_7.text()
    module_loc8 = main_window.main_tab_module_loc_LineEdit_8.text()

    # daq parameters
    daq_adc = main_window.main_tab_DAQParams_ADC_Constant_LineEdit.text()
    daq_sample_rate = str(main_window.main_tab_DAQParams_samplingRate_DropDown.currentText())
    daq_cutoff = str(main_window.main_tab_DAQParams_Cutoff_Frequency_LineEdit.currentText())
    daq_gain = str(main_window.main_tab_DAQParams_gain_DropDown.currentText())

    # sensor info has to be fixed
    # sensor info
    # sensor1_name = channel_info_win.channel_info_sensor1_nameLineEdit.text()
    # sensor1_type = str(channel_info_win.channel_info_sensor1_type_DropDown.currentText())
    # sensor1_sensitivity = channel_info_win.channel_info_sensor1_Sensitivity_LineEdit.text()
    # sensor1_bandwidth = channel_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit.text()
    # sensor1_scale = channel_info_win.channel_info_senson1_full_Scale_LineEdit.text()
    # sensor1_loc = channel_info_win.channel_info_sensor1_location_Edit.text()
    # sensor1_damp = channel_info_win.channel_info_sensor1_dampingLineEdit.text()
    #
    # sensor2_name = channel_info_win.channel_info_sensor2_nameLineEdit.text()
    # sensor2_type = str(channel_info_win.channel_info_sensor2_type_DropDown.currentText())
    # sensor2_sensitivity = channel_info_win.channel_info_sensor2_Sensitivity_LineEdit.text()
    # sensor2_bandwidth = channel_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit.text()
    # sensor2_scale = channel_info_win.channel_info_senson2_full_Scale_LineEdit.text()
    # sensor2_loc = channel_info_win.channel_info_sensor2_location_Edit.text()
    # sensor2_damp = channel_info_win.channel_info_sensor2_dampingLineEdit.text()
    #
    # sensor3_name = channel_info_win.channel_info_sensor3_nameLineEdit.text()
    # sensor3_type = str(channel_info_win.channel_info_sensor3_type_DropDown.currentText())
    # sensor3_sensitivity = channel_info_win.channel_info_sensor3_Sensitivity_LineEdit.text()
    # sensor3_bandwidth = channel_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit.text()
    # sensor3_scale = channel_info_win.channel_info_senson3_full_Scale_LineEdit.text()
    # sensor3_loc = channel_info_win.channel_info_sensor3_location_Edit.text()
    # sensor3_damp = channel_info_win.channel_info_sensor3_dampingLineEdit.text()
    #
    # sensor4_name = channel_info_win.channel_info_sensor4_nameLineEdit.text()
    # sensor4_type = str(channel_info_win.channel_info_sensor4_type_DropDown.currentText())
    # sensor4_sensitivity = channel_info_win.channel_info_sensor4_Sensitivity_LineEdit.text()
    # sensor4_bandwidth = channel_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit.text()
    # sensor4_scale = channel_info_win.channel_info_senson4_full_Scale_LineEdit.text()
    # sensor4_loc = channel_info_win.channel_info_sensor4_location_Edit.text()
    # sensor4_damp = channel_info_win.channel_info_sensor4_dampingLineEdit.text()

    if vis_bool == "2":
        show_main_sens_sel_window()

    if log:
        print("name=" + name)
        print("id=" + recording_name_id)
        print("duration=" + duration)
        print("type=" + type)
        print("visualization=" + vis_bool)
        print("store_bool=" + store_bool)
        print("localization:")
        print("localization type:" + loc_type + ", name:" + loc_name + ", localization longitud:" + loc_longitude
              + ", localization latitude:" + loc_latitude + ", lozalization hour" + loc_hour
              + ", minutes:" + loc_minutes + ", seconds:" + loc_seconds)
        print("specimen by module:")
        print("1:" + module_loc1 + ", 2:" + module_loc2 + ", 3:" + module_loc3 +
              ", 4:" + module_loc4 + ", 5:" + module_loc5 + ", 6:" + module_loc6 +
              ", 7:" + module_loc7 + ", 8:" + module_loc8)
        print("DAQ parameters")
        print("adc constant=" + daq_adc + ", sampling rate=" + daq_sample_rate + ", cutoff=" + daq_cutoff +
              ", gain=" + daq_gain)
        print("sensor info:")
        # print("name="+sensor1_name+", type="+sensor1_type+", sensitivity="+sensor1_sensitivity
        #       +", bandwidth="+sensor1_bandwidth+", fullscale="+sensor1_scale+", damping="+sensor1_damp
        #       +", localization="+sensor1_loc)


"""
Begin Acquisition Process
"""
def start_acquisition():
    show_main_sens_sel_window()
    enable_start_connected_sensors()
    # snapshot_data()


def enable_start_connected_sensors():
    for s in range(0, 32, 1):  # Go through 32 sensors.
        if not sensors_all[s].connected:  # If sensor in not connected.
            sensor_selection_list[s].setEnabled(False)


"""
Add default functionality here
"""
# Channel Info Window.
channel_info_win.channel_info_SAVE_Button.clicked.connect(lambda: save_sensor_info())
chan_mod_name = channel_info_win.channel_info_module_name
# Ch 1
channel_info_win.channel_info_sensor1_Sensitivity_LineEdit
channel_info_win.channel_info_sensor1_dampingLineEdit
channel_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
channel_info_win.channel_info_sensor1_full_Scale_LineEdit
channel_info_win.channel_info_sensor1_location_Edit
channel_info_win.channel_info_sensor1_nameLineEdit
channel_info_win.channel_info_sensor1_TITLE
channel_info_win.channel_info_sensor1_type_DropDown
# Ch 2
channel_info_win.channel_info_sensor2_dampingLineEdit
channel_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
channel_info_win.channel_info_sensor2_Sensitivity_LineEdit
channel_info_win.channel_info_sensor2_nameLineEdit
channel_info_win.channel_info_sensor2_type_DropDown
channel_info_win.channel_info_sensor2_TITLE
channel_info_win.channel_info_sensor2_location_Edit
channel_info_win.channel_info_sensor2_full_Scale_LineEdit
# Ch 3
channel_info_win.channel_info_sensor3_nameLineEdit
channel_info_win.channel_info_sensor3_type_DropDown
channel_info_win.channel_info_sensor3_Sensitivity_LineEdit
channel_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
channel_info_win.channel_info_sensor3_full_scale_LineEdit
channel_info_win.channel_info_sensor3_dampingLineEdit
channel_info_win.channel_info_sensor3_location_Edit
channel_info_win.channel_info_sensor3_TITLE
# Ch 4
channel_info_win.channel_info_sensor4_nameLineEdit
channel_info_win.channel_info_sensor4_type_DropDown
channel_info_win.channel_info_sensor4_Sensitivity_LineEdit
channel_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
channel_info_win.channel_info_senson4_full_Scale_LineEdit
channel_info_win.channel_info_sensor4_location_Edit
channel_info_win.channel_info_sensor4_dampingLineEdit
channel_info_win.channel_info_sensor4_TITLE

# Visualize Sensor Selection
viz_sensor_sel_win.sensor_selection_Save_Plot_Data_checkBox
viz_sensor_sel_win.sensor_selection_NEXT_Button.clicked.connect(lambda: show_progress_dialog('Plotting ' + 'What you wanna plot'))
viz_sensor_sel_win.sensor_select_MAX_Label
viz_sensor_sel_win.Sensor_1
viz_sensor_sel_win.Sensor_2
viz_sensor_sel_win.Sensor_3
viz_sensor_sel_win.Sensor_4
viz_sensor_sel_win.Sensor_5
viz_sensor_sel_win.Sensor_6
viz_sensor_sel_win.Sensor_7
viz_sensor_sel_win.Sensor_8
viz_sensor_sel_win.Sensor_9
viz_sensor_sel_win.Sensor_10
viz_sensor_sel_win.Sensor_11
viz_sensor_sel_win.Sensor_12
viz_sensor_sel_win.Sensor_13
viz_sensor_sel_win.Sensor_14
viz_sensor_sel_win.Sensor_15
viz_sensor_sel_win.Sensor_16
viz_sensor_sel_win.Sensor_17
viz_sensor_sel_win.Sensor_18
viz_sensor_sel_win.Sensor_19
viz_sensor_sel_win.Sensor_20
viz_sensor_sel_win.Sensor_21
viz_sensor_sel_win.Sensor_22
viz_sensor_sel_win.Sensor_23
viz_sensor_sel_win.Sensor_24
viz_sensor_sel_win.Sensor_25
viz_sensor_sel_win.Sensor_26
viz_sensor_sel_win.Sensor_27
viz_sensor_sel_win.Sensor_28
viz_sensor_sel_win.Sensor_29
viz_sensor_sel_win.Sensor_30
viz_sensor_sel_win.Sensor_31
viz_sensor_sel_win.Sensor_32

# Main Sensor Selection
main_sensor_sel_win.sensor_selection_DONE_Button.clicked.connect(lambda: action_Begin_Recording())  # Close() DONE in UI.
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
sensor_selection_list = [win_sens_1, win_sens_2, win_sens_3, win_sens_4, win_sens_5, win_sens_6, win_sens_7, win_sens_8,
                         win_sens_9, win_sens_10, win_sens_11, win_sens_12, win_sens_13, win_sens_14, win_sens_15,
                         win_sens_15, win_sens_16, win_sens_17, win_sens_18, win_sens_19, win_sens_20, win_sens_21,
                         win_sens_22, win_sens_23, win_sens_24, win_sens_25, win_sens_26, win_sens_27, win_sens_28,
                         win_sens_29, win_sens_30, win_sens_31, win_sens_32]  # Used to get values easily (goes from 0 to 31)

# Acquiring Something
prog_dlg.progress_dialog_STOP_button.clicked.connect(lambda: action_cancel_everything())
dlg_prog_bar = prog_dlg.progress_dialog_progressBar
dlg_title = prog_dlg.progress_dialog_title

# Select Module for Channel Info.
mod_sel_win.module_selection_Module1.clicked.connect(lambda: show_channel_info_window(0))
mod_sel_win.module_selection_Module2.clicked.connect(lambda: show_channel_info_window(1))
mod_sel_win.module_selection_Module3.clicked.connect(lambda: show_channel_info_window(2))
mod_sel_win.module_selection_Module4.clicked.connect(lambda: show_channel_info_window(3))
mod_sel_win.module_selection_Module5.clicked.connect(lambda: show_channel_info_window(4))
mod_sel_win.module_selection_Module6.clicked.connect(lambda: show_channel_info_window(5))
mod_sel_win.module_selection_Module7.clicked.connect(lambda: show_channel_info_window(6))
mod_sel_win.module_selection_Module8.clicked.connect(lambda: show_channel_info_window(7))

# File System
file_sys_win.file_system_treeView
file_sys_win.file_system_OPEN_button
file_sys_win.file_system_CANCEL_button

# Main Tab Window
# RECORDING  Settings
main_window.main_tab_RecordingSettings_LOAD_SETTINGS_Button
main_window.main_tab_RecordingSettings__SAVE_button
rec_name_edit = main_window.main_tab_RecordingSettings_name_LineEdit
rec_id_edit = main_window.main_tab_RecordingSettings_id_LineEdit
rec_duration_edit = main_window.main_tab_RecordingSettings_durationLineEdit
rec_type_dropdown = main_window.main_tab_RecordingSettings_type_DropDown
rec_viz_checkbox = main_window.main_tab_RecordingSettings_visualize_checkBox
rec_store_checkbox = main_window.main_tab_RecordingSettings_store_checkBox
# Localization Settings
main_window.main_tab_LocalizationSettings_acquire_GPS_Button.clicked.connect(lambda: sync_gps())
loc_type_dropdown = main_window.main_tab_LocalizationSettings_type_DropBox
loc_type_dropdown.currentIndexChanged.connect(lambda: load_local_settings_to_gui())
main_window.main_tab_LocalizationSettings_Name_lineEdit
main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button
main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button
main_window.main_tab_LocalizationSettings_longitudLineEdit
main_window.main_tab_LocalizationSettings_latitudLineEdit
main_window.main_tab_LocalizationSettings_hourLineEdit
main_window.main_tab_LocalizationSettings_minutesLineEdit
main_window.main_tab_LocalizationSettings_secondsLineEdit
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
main_window.main_tab_DAQParams_SAVE_PARAMS_button.clicked.connect(lambda: action_store_DAQ_Params())  # TODO
main_window.main_tab_DAQParams_LOAD_PARAMS_button
# main_window.main_tab_DAQParams_ADC_Constant_Label
samfreq_dropdown = main_window.main_tab_DAQParams_samplingRate_DropDown
cutfreq_drodown = main_window.main_tab_DAQParams_Cutoff_Frequency_DropDown
gain_dropdown = main_window.main_tab_DAQParams_gain_DropDown
main_window.main_tab_CHANNEL_INFO_button.clicked.connect(lambda: open_module_selection_window())
# main_window.main_tab_START_button.clicked.connect(lambda: show_main_sens_sel_window()) #this was the one before
main_window.main_tab_START_button.clicked.connect(lambda: start_acquisition())
# Visualization
main_window.visualize_tab_tableWidget
main_window.visualize_tab_TIME_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plt_time().show_plot('PLOT'))  # TODO GET INFO FROM USER.
main_window.visualize_tab_FFT_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_fft('S1', 100).show_plot('PLOT'))
main_window.visualize_tab_APS_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_PSD('S1', 100).show_plot('PLOT'))
main_window.visualize_tab_XPS_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_CSD('S1', 'S2', 100).show_plot('PLOT'))
main_window.visualize_tab_PHASE_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_Phase('S1', 100).show_plot('PLOT'))
main_window.visualize_tab_COHERE_button.clicked.connect(lambda: Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_coherence('S1', 'S2', 100).show_plot('PLOT'))

# ----------------------------------------------- MAIN WINDOW ------------------------------------------------------
"""
Prepares GUI and sends request to control module for begin recording data.
"""


def action_Begin_Recording():
    instruc_man = ins_man.instruction_manager()
    # Activate App Running Dialog.
    # Send Setting Information to Control Module.
    # instruc_man.send_set_configuration('Configuration String.')
    # Prepare Real-Time Plot to receive Data.
    # Send Begin Recording FLAG to Control Module.
    # instruc_man.send_request_start()

    # Close Window
    main_sensor_sel_win.close()

    # Show Progress Dialog
    show_progress_dialog('Data')


"""
Shows the Main Sensor Selection Window.

CALL BEFORE SENDING REQUEST TO START.
"""


def ask_for_sensors():
    # User Select which sensors it wants.
    show_main_sens_sel_window()
    # When Done pressed --> begin recording. | this is handled from UI.

# ************** STORING / LOADING *******************
def action_store_DAQ_Params():
    # TODO Implement
    return


def action_load_DAQ_Params():
    # Get filename from User
    # Load Params from File
    set_dat_man.Setting_File_Manager()
    # Set Params into GUI.


def action_store_Location():
    # TODO Implement
    return


def action_load_Location():
    # Get filename from User
    # Load Params from File
    set_dat_man.Setting_File_Manager()
    # Set Params into GUI.


def action_store_Rec_Setts():
    # TODO Implement
    return


def action_load_Rec_Setts():
    # Get filename from User
    # Load Params from File
    set_dat_man.Setting_File_Manager()
    # Set Params into GUI.


# ********************************************* LOCATION ***************************************************************
def sync_gps():  # TODO TEST
    disable_main_window()
    show_acquire_dialog('GPS Signal')
    im = ins_man.instruction_manager()
    im.send_gps_sync_request()

    timeout = 0
    while im.send_request_status() != 1:
    # while 1:
        if log: print('GPS Waiting....')

        sleep(0.500)  # Wait for half a second before asking again.
        timeout += 1
        if timeout == 5 * 2:  # = [desired timeout in seconds] * [1/(sleep value)]
            show_error('GPS Failed to Synchronize.')
            break

    enable_main_window()
    set_gps_into_gui()


"""
Loads Settings already in the program to GUi components depending on location type selected by user.
The fields for the types not selected will be disabled.
"""
def load_local_settings_to_gui():
    if log: print(loc_type_dropdown.currentIndex())
    if loc_type_dropdown.currentIndex() == 0:  # GPS
        loc_gps_frame.setEnabled(True)
        loc_specimen_frame.setEnabled(False)
        set_gps_into_gui()

    elif loc_type_dropdown.currentIndex() == 1:  # Specimen
        loc_gps_frame.setEnabled(False)
        loc_specimen_frame.setEnabled(True)
        set_specimen_location_into_gui()


# ---------------------------------------------- CHANNEL INFORMATION----------------------------------------------------
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
"""
Shows Dialog with 'Acquiring' as the title beginning.

:param message : the desired dialog message.
"""
def show_acquire_dialog(message: str):
    # Set progress is default to undetermined.
    # Show Dialog & Set Message
    show_progress_dialog('Acquiring ' + message)

    # Enable Main Window when done.  # FIXME Change to correct function.
    enable_main_window()


"""
Sends signal to Control Module to cancel all recording, storing, sending, synchronizing and/or
any other process the system might be doing. 

Called by user when CANCEL action is desired.
"""
def action_cancel_everything():
    # im = ins_man.instruction_manager()
    # im.send_cancel_request()
    enable_main_window()


# ****************************************** SENSOR & CHANNEL INFORMATION *********************************************
"""
Saves sensor data from UI into structure.
"""
def save_sensor_info():
    # Get info from GUI.
    # Set info to correct Data Structure.
    # Set sensor info (4)
    sens_1 = sens.Sensor('NAME', 0)
    sens_2 = sens.Sensor('NAME', 0)
    sens_3 = sens.Sensor('NAME', 0)
    sens_4 = sens.Sensor('NAME', 0)

    # Set channel sensors.
    channel = chan.Channel('NAME', sens_1, sens_2, sens_3, sens_4)


# ------------------------------------------------ VISUALIZATION ------------------------------------------------------
"""
[1]
Creates and Opens Window with Time plot using user information from file.
"""
def plot_time(filename: str):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plt_time().show_plot('RESPECT TO TIME')  # TODO SWITCH TO TEMP FILE.


"""
[2]
Creats and Opens Window with Time plot using user information from file.
"""
def plot_fft(filename: str, sensor: str, freq: int):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_fft('S1', 100).show_plot('FOURIER TRANSFORM')  # TODO SWITCH TO TEMP FILE.


"""
[3]
Creates and Opens Window with Time plot using user information from file.
"""
def plot_aps(filename: str, sensor: str, freq: int):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_PSD('S1', 100).show_plot('AUTO-POWER SPECTRA')  # TODO SWITCH TO TEMP FILE.


"""
[4]
Creates and Opens Window with Time plot using user information from file.
"""
def plot_cps(filename: str):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_CSD().show_plot('CROSS-POWER SPECTRA')  # TODO SWITCH TO TEMP FILE.


"""
[5]
Creates and Opens Window with Time plot using user information from file.
"""
def plot_phase(filename: str):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_Phase().show_plot('UNWRAPPED PHASE FUNCTION')  # TODO SWITCH TO TEMP FILE.


"""
[6]
Creates and Opens Window with Time plot using user information from file.
"""
def plot_cohere(filename: str):
    Plot_Data.Plot_Data('Data/Random_Dummy_Data_v2.csv').plot_coherence().show_plot('COHERENCE')  # TODO SWITCH TO TEMP FILE.


"""
Beginning of the program.
Main will redirect here for GUI setup. 
"""
def init():
    main_window.show()
    loc_specimen_frame.setEnabled(False)  # Begin with GPS only enabled.

    # --------- TESTING ------------
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
    app.exec()
