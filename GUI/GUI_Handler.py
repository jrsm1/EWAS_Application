# import PyQt5
from GUI import Main_Window as main_win
from GUI import Channel_Info_Window as chan_info_win
from GUI import Acquire_Dialog as acq_dlg
from Settings import setting_data_manager as set_man
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
main_window = uic.loadUi("main_tab_layout_V2.ui")
channel_info_win = uic.loadUi("channel_info_window.ui")
prog_dlg = uic.loadUi("progress_dialog_v1.ui")
viz_sensor_sel_win = uic.loadUi('visualize_sensor_selection_matrix.ui')
main_sensor_sel_win = uic.loadUi('main_sensor_selection_matrix.ui')
mod_sel_win = uic.loadUi('module_selection_window.ui')
file_sys_win = uic.loadUi('file_system_window.ui')

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
    Opens Channel Information Window
"""
def show_channel_info_window():
    channel_info_win.show()


"""
    Opens Sensor Selection Window for Recording
"""
def show_main_sens_sel_window():
    disable_main_window()
    main_sensor_sel_win.show()


def show_progress_dialog(message: str):
    prog_dlg.progress_dialog_title.setText('Acquiring' + message)
    prog_dlg.show()


"""
Add default functionality here
"""
# Channel Info Window.
channel_info_win.channel_info_SAVE_Button.clicked.connect(lambda: chan_info_win.save_info())
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
viz_sensor_sel_win.sensor_selection_NEXT_Button.clicked.connect(lambda: acq_dlg.show_dialog())
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
main_sensor_sel_win.sensor_selection_DONE_Button.clicked.connect(lambda: main_win.action_Begin_Recording())  # Close() DONE in UI.
main_sensor_sel_win.sensor_select_MAX_Label
main_sensor_sel_win.Sensor_1
main_sensor_sel_win.Sensor_2
main_sensor_sel_win.Sensor_3
main_sensor_sel_win.Sensor_4
main_sensor_sel_win.Sensor_5
main_sensor_sel_win.Sensor_6
main_sensor_sel_win.Sensor_7
main_sensor_sel_win.Sensor_8
main_sensor_sel_win.Sensor_9
main_sensor_sel_win.Sensor_10
main_sensor_sel_win.Sensor_11
main_sensor_sel_win.Sensor_12
main_sensor_sel_win.Sensor_13
main_sensor_sel_win.Sensor_14
main_sensor_sel_win.Sensor_15
main_sensor_sel_win.Sensor_16
main_sensor_sel_win.Sensor_17
main_sensor_sel_win.Sensor_18
main_sensor_sel_win.Sensor_19
main_sensor_sel_win.Sensor_20
main_sensor_sel_win.Sensor_21
main_sensor_sel_win.Sensor_22
main_sensor_sel_win.Sensor_23
main_sensor_sel_win.Sensor_24
main_sensor_sel_win.Sensor_25
main_sensor_sel_win.Sensor_26
main_sensor_sel_win.Sensor_27
main_sensor_sel_win.Sensor_28
main_sensor_sel_win.Sensor_29
main_sensor_sel_win.Sensor_30
main_sensor_sel_win.Sensor_31
main_sensor_sel_win.Sensor_32

# Acquiring Something
prog_dlg.progress_dialog_STOP_button.clicked.connect(lambda: acq_dlg.action_cancel_everything())
prog_dlg.progress_dialog_progressBar
prog_dlg.progress_dialog_title

# Select Module for Channel Info.
mod_sel_win.module_selection_Module1
mod_sel_win.module_selection_Module2
mod_sel_win.module_selection_Module3
mod_sel_win.module_selection_Module4
mod_sel_win.module_selection_Module5
mod_sel_win.module_selection_Module6
mod_sel_win.module_selection_Module7
mod_sel_win.module_selection_Module8

# File System
file_sys_win.file_system_treeView
file_sys_win.file_system_OPEN_button
file_sys_win.file_system_CANCEL_button

# Main Tab Window
# Localization  Settings
main_window.main_tab_RecordingSettings_LOAD_SETTINGS_Button
main_window.main_tab_RecordingSettings__SAVE_button
main_window.main_tab_RecordingSettings_name_LineEdit
main_window.main_tab_RecordingSettings_id_LineEdit
main_window.main_tab_RecordingSettings_durationLineEdit
main_window.main_tab_RecordingSettings_type_DropDown
main_window.main_tab_RecordingSettings_visualize_checkBox
main_window.main_tab_RecordingSettings_store_checkBox
# Localization Settings
main_window.main_tab_LocalizationSettings_type_DropBox
main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button
main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button
main_window.main_tab_LocalizationSettings_longitudLineEdit
main_window.main_tab_LocalizationSettings_latitudLineEdit
main_window.main_tab_LocalizationSettings_hourLineEdit
main_window.main_tab_LocalizationSettings_minutesLineEdit
### Module Loc. Settings
main_window.main_tab_module_loc_LineEdit_1
main_window.main_tab_module_loc_LineEdit_2
main_window.main_tab_module_loc_LineEdit_3
main_window.main_tab_module_loc_LineEdit_4
main_window.main_tab_module_loc_LineEdit_5
main_window.main_tab_module_loc_LineEdit_6
main_window.main_tab_module_loc_LineEdit_7
main_window.main_tab_module_loc_LineEdit_8
# Data Acquisition Settings
main_window.main_tab_DAQParams_SAVE_PARAMS_button.clicked.connect(lambda: main_win.action_store_DAQ_Params())
main_window.main_tab_DAQParams_LOAD_PARAMS_button
main_window.main_tab_DAQParams_ADC_Constant_LineEdit  # FIXME This may change widgets thus changing Object Name.
main_window.main_tab_DAQParams_samplingRate_DropDown
main_window.main_tab_DAQParams_Cutoff_Frequency_LineEdit
main_window.main_tab_DAQParams_gain_DropDown
main_window.main_tab_CHANNEL_INFO_button.clicked.connect(lambda: show_channel_info_window())
main_window.main_tab_START_button.clicked.connect(lambda: show_main_sens_sel_window())
# Visualization
main_window.visualize_tab_tableWidget
main_window.visualize_tab_TIME_button
main_window.visualize_tab_FFT_button
main_window.visualize_tab_APS_button
main_window.visualize_tab_XPS_button
main_window.visualize_tab_PHASE_button
main_window.visualize_tab_COHERE_button

main_window.show()
# show_progress_dialog()
# sensor_sel.show()
# mod_sel.show()
# channel_info_win.show()
app.exec()
