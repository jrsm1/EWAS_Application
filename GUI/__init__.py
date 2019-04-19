# import PyQt5
# import Main_Window as mw
# import GUI_Handler
# from PyQt5 import QtWidgets, uic
#
# app = QtWidgets.QApplication([])
# main_window = uic.loadUi("GUI/main_tab_layout_V2.ui")
# channel_info_win = uic.loadUi("GUI/channel_info_window.ui")
# prog_dlg = uic.loadUi("GUI/progress_dialog_v1.ui")
# sensor_sel = uic.loadUi('GUI/sensor_selection_matrix.ui')
# mod_sel = uic.loadUi('GUI/module_selection_window.ui')
# file_sys = uic.loadUi('GUI/file_system_window.ui')
#
#
# """
#     Creates an Error Message dialog
#     :param message: String - The Desired Message Output.
# """
# def show_error(message: str):
#     err_dlg = QtWidgets.QErrorMessage()
#     err_dlg.showMessage(message)
#     err_dlg.exec()
#
#
# """
# Add default functionality here
# """
# # Channel Info Window.
# # Ch 1
# channel_info_win.channel_info_sensor1_Sensitivity_LineEdit
# channel_info_win.channel_info_sensor1_dampingLineEdit
# channel_info_win.channel_info_sensor1_frequency_Bandwidth_LineEdit
# channel_info_win.channel_info_sensor1_full_Scale_LineEdit
# channel_info_win.channel_info_sensor1_location_Edit
# channel_info_win.channel_info_sensor1_nameLineEdit
# channel_info_win.channel_info_sensor1_TITLE
# channel_info_win.channel_info_sensor1_type_DropDown
# # Ch 2
# channel_info_win.channel_info_sensor2_dampingLineEdit
# channel_info_win.channel_info_sensor2_frequency_Bandwidth_LineEdit
# channel_info_win.channel_info_sensor2_Sensitivity_LineEdit
# channel_info_win.channel_info_sensor2_nameLineEdit
# channel_info_win.channel_info_sensor2_type_DropDown
# channel_info_win.channel_info_sensor2_TITLE
# channel_info_win.channel_info_sensor2_location_Edit
# channel_info_win.channel_info_sensor2_full_Scale_LineEdit
# # Ch 3
# channel_info_win.channel_info_sensor3_nameLineEdit
# channel_info_win.channel_info_sensor3_type_DropDown
# channel_info_win.channel_info_sensor3_Sensitivity_LineEdit
# channel_info_win.channel_info_sensor3_frequency_Bandwidth_LineEdit
# channel_info_win.channel_info_sensor3_full_scale_LineEdit
# channel_info_win.channel_info_sensor3_dampingLineEdit
# channel_info_win.channel_info_sensor3_location_Edit
# channel_info_win.channel_info_sensor3_TITLE
# # Ch 4
# channel_info_win.channel_info_sensor4_nameLineEdit
# channel_info_win.channel_info_sensor4_type_DropDown
# channel_info_win.channel_info_sensor4_Sensitivity_LineEdit
# channel_info_win.channel_info_sensor4_frequency_Bandwidth_LineEdit
# channel_info_win.channel_info_senson4_full_Scale_LineEdit
# channel_info_win.channel_info_sensor4_location_Edit
# channel_info_win.channel_info_sensor4_dampingLineEdit
# channel_info_win.channel_info_sensor4_TITLE
#
#
# # Sensor Selection
# sensor_sel.sensor_selection_Save_Plot_Data_checkBox
# sensor_sel.sensor_selection_NEXT_Bbutton
# sensor_sel.sensor_select_MAX_Label
# sensor_sel.Sensor_1
# sensor_sel.Sensor_2
# sensor_sel.Sensor_3
# sensor_sel.Sensor_4
# sensor_sel.Sensor_5
# sensor_sel.Sensor_6
# sensor_sel.Sensor_7
# sensor_sel.Sensor_8
# sensor_sel.Sensor_9
# sensor_sel.Sensor_10
# sensor_sel.Sensor_11
# sensor_sel.Sensor_12
# sensor_sel.Sensor_13
# sensor_sel.Sensor_14
# sensor_sel.Sensor_15
# sensor_sel.Sensor_16
# sensor_sel.Sensor_17
# sensor_sel.Sensor_18
# sensor_sel.Sensor_19
# sensor_sel.Sensor_20
# sensor_sel.Sensor_21
# sensor_sel.Sensor_22
# sensor_sel.Sensor_23
# sensor_sel.Sensor_24
# sensor_sel.Sensor_25
# sensor_sel.Sensor_26
# sensor_sel.Sensor_27
# sensor_sel.Sensor_28
# sensor_sel.Sensor_29
# sensor_sel.Sensor_30
# sensor_sel.Sensor_31
# sensor_sel.Sensor_32
#
# # Acquiring Something
# prog_dlg.progress_dialog_STOP_button
# prog_dlg.progress_dialog_progressBar
# prog_dlg.progress_dialog_title
#
#
# # Select Module for Channel Info.
# mod_sel.module_selection_Module1
# mod_sel.module_selection_Module2
# mod_sel.module_selection_Module3
# mod_sel.module_selection_Module4
# mod_sel.module_selection_Module5
# mod_sel.module_selection_Module6
# mod_sel.module_selection_Module7
# mod_sel.module_selection_Module8
#
#
# # File System
# file_sys.file_system_treeView
# file_sys.file_system_OPEN_button
# file_sys.file_system_CANCEL_button
#
#
# # Main Tab Window
# # Localization  Settings
# main_window.main_tab_RecordingSettings_LOAD_SETTINGS_Button
# main_window.main_tab_RecordingSettings__SAVE_button
# main_window.main_tab_RecordingSettings_name_LineEdit
# main_window.main_tab_RecordingSettings_id_LineEdit
# main_window.main_tab_RecordingSettings_durationLineEdit
# main_window.main_tab_RecordingSettings_type_DropDown
# main_window.main_tab_RecordingSettings_visualize_checkBox
# main_window.main_tab_RecordingSettings_store_checkBox
# # Localization Settings
# main_window.main_tab_LocalizationSettings_type_DropBox
# main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button
# main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button
# main_window.main_tab_LocalizationSettings_longitudLineEdit
# main_window.main_tab_LocalizationSettings_latitudLineEdit
# main_window.main_tab_LocalizationSettings_hourLineEdit
# main_window.main_tab_LocalizationSettings_minutesLineEdit
# ### Module Loc. Settings
# main_window.main_tab_module_loc_LineEdit_1
# main_window.main_tab_module_loc_LineEdit_2
# main_window.main_tab_module_loc_LineEdit_3
# main_window.main_tab_module_loc_LineEdit_4
# main_window.main_tab_module_loc_LineEdit_5
# main_window.main_tab_module_loc_LineEdit_6
# main_window.main_tab_module_loc_LineEdit_7
# main_window.main_tab_module_loc_LineEdit_8
# # Data Acquisition Settings
# main_window.main_tab_DAQParams_SAVE_PARAMS_button
# main_window.main_tab_DAQParams_LOAD_PARAMS_button
# main_window.main_tab_DAQParams_ADC_Constant_LineEdit # FIXME This may change widgets thus changing Object Name.
# main_window.main_tab_DAQParams_samplingRate_DropDown
# main_window.main_tab_DAQParams_Cutoff_Frequency_LineEdit
# main_window.main_tab_DAQParams_gain_DropDown
# main_window.main_tab_CHANNEL_INFO_button
# main_window.main_tab_START_button
# # Visualization
# main_window.visualize_tab_tableWidget
# main_window.visualize_tab_TIME_button
# main_window.visualize_tab_FFT_button
# main_window.visualize_tab_APS_button
# main_window.visualize_tab_XPS_button
# main_window.visualize_tab_PHASE_button
# main_window.visualize_tab_COHERE_button
#
# main_window.show()
# # prog_dlg.show()
# # sensor_sel.show()
# # mod_sel.show()
# # channel_info_win.show()
# app.exec()
