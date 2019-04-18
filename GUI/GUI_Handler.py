# import PyQt5
from GUI import Main_Window as main_win
from GUI import Channel_Info_Window as chan_info_win
from GUI import Acquire_Dialog as acq_dlg
from Settings import setting_data_manager as set_man
from PyQt5 import QtWidgets, uic, QtCore
from Control_Module_Comm import instruction_manager as ins_man
from Control_Module_Comm.Structures import Channel_Individual as chan, Sensor_Individual as sens

app = QtWidgets.QApplication([])
main_window = uic.loadUi("GUI/main_tab_layout_V2.ui")
channel_info_win = uic.loadUi("GUI/channel_info_window.ui")
prog_dlg = uic.loadUi("GUI/progress_dialog_v1.ui")
viz_sensor_sel_win = uic.loadUi('GUI/visualize_sensor_selection_matrix.ui')
main_sensor_sel_win = uic.loadUi('GUI/main_sensor_selection_matrix.ui')
mod_sel_win = uic.loadUi('GUI/module_selection_window.ui')
file_sys_win = uic.loadUi('GUI/file_system_window.ui')

# testing purposes
log = 1
log_working = 0

# some global bariables
daq_sample_rate = 0
daq_cutoff = 0
daq_gain = 0
duration = 0


def show_main_window():
    main_window.show()


# testing purposes
log = 1

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


def snapshot_data():
    # we have to change everything to string, because that's how it's going to get passed
    # main tab recording settings
    name = main_window.main_tab_RecordingSettings_name_LineEdit.text()
    id = main_window.main_tab_RecordingSettings_id_LineEdit.text()
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
    loc_longitud = main_window.main_tab_LocalizationSettings_longitudLineEdit.text()
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
    daq_sample_rate = str(main_window.main_tab_DAQParams_samplingRate_DropDown.currentIndex())
    daq_cutoff = str(main_window.main_tab_DAQParams_Cutoff_Frequency_LineEdit.currentIndex())
    daq_gain = str(main_window.main_tab_DAQParams_gain_DropDown.currentIndex())

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
        pass
        show_main_sens_sel_window()
    else:
        ins = ins_man.instruction_manager()
        ins.send_recording_parameters(daq_sample_rate, daq_cutoff, daq_gain, duration, "0000")

    if log_working:
        print("name=" + name)
        print("id=" + id)
        print("duration=" + duration)
        print("type=" + type)
        print("visualization=" + vis_bool)
        print("store_bool=" + store_bool)
        print("localization:")
        print("localization type:" + loc_type + ", name:" + loc_name + ", localization longitud:" + loc_longitud
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


def get_module_and_sensors_selected():
    if log: print("entered get_module_and_sensors_selected()")
    count = 0;
    sensors_sel = []
    if log: print("created empy sensor selected array")
    sensors_sel.append(main_sensor_sel_win.Sensor_1)
    # test = int(main_sensor_sel_win.Sensor_1)
    # if log:
    #     print("added the first sensor to the list")
    #     print("tester prints ", test)
    #     print("sensor sel is ", str(sensors_sel))
    sensors_sel.append(main_sensor_sel_win.Sensor_2)
    sensors_sel.append(main_sensor_sel_win.Sensor_3)
    sensors_sel.append(main_sensor_sel_win.Sensor_4)
    sensors_sel.append(main_sensor_sel_win.Sensor_5)
    sensors_sel.append(main_sensor_sel_win.Sensor_6)
    sensors_sel.append(main_sensor_sel_win.Sensor_7)
    sensors_sel.append(main_sensor_sel_win.Sensor_8)
    # if log: print("sensor sel is ", str(sensors_sel))
    sensors_sel.append(main_sensor_sel_win.Sensor_9)
    sensors_sel.append(main_sensor_sel_win.Sensor_10)
    sensors_sel.append(main_sensor_sel_win.Sensor_11)
    sensors_sel.append(main_sensor_sel_win.Sensor_12)
    sensors_sel.append(main_sensor_sel_win.Sensor_13)
    sensors_sel.append(main_sensor_sel_win.Sensor_14)
    sensors_sel.append(main_sensor_sel_win.Sensor_15)
    sensors_sel.append(main_sensor_sel_win.Sensor_16)
    sensors_sel.append(main_sensor_sel_win.Sensor_17)
    sensors_sel.append(main_sensor_sel_win.Sensor_18)
    sensors_sel.append(main_sensor_sel_win.Sensor_19)
    sensors_sel.append(main_sensor_sel_win.Sensor_20)
    sensors_sel.append(main_sensor_sel_win.Sensor_21)
    sensors_sel.append(main_sensor_sel_win.Sensor_22)
    sensors_sel.append(main_sensor_sel_win.Sensor_23)
    sensors_sel.append(main_sensor_sel_win.Sensor_24)
    sensors_sel.append(main_sensor_sel_win.Sensor_25)
    sensors_sel.append(main_sensor_sel_win.Sensor_26)
    sensors_sel.append(main_sensor_sel_win.Sensor_27)
    sensors_sel.append(main_sensor_sel_win.Sensor_28)
    sensors_sel.append(main_sensor_sel_win.Sensor_29)
    sensors_sel.append(main_sensor_sel_win.Sensor_30)
    sensors_sel.append(main_sensor_sel_win.Sensor_31)
    sensors_sel.append(main_sensor_sel_win.Sensor_32)
    # if log: print("sensor sel is ", str(sensors_sel))

    if log: print("print sensors array created correctly")
    sensors_selected = "0000"
    correct = 1
    index = 0
    for i in sensors_sel:
        index += 1
        if i.checkState() == 2:
            count = count + 1
            module = str(int((index - 1) / 4)+1)
            sensor = str(((index - 1) % 4) + 1)
            sensors_selected = module + sensor + sensors_selected
        if count > 2:
            correct = 0
            break

    if log: print("sensors selected are: ", sensors_selected)

    for i in sensors_sel:
        i.setCheckState(False)

    if correct:
        sensors_selected = sensors_selected[0:4]
        return sensors_selected
    return "0000"


def start_aquisition():
    snapshot_data()

def sensor_sel_start():
    sens = get_module_and_sensors_selected()
    if log: print("sensors selected are ", sens)
    ins = ins_man.instruction_manager()
    main_sensor_sel_win.close()
    ins.send_recording_parameters(daq_sample_rate, daq_cutoff, daq_gain, duration, sens)
    if log: print("came back to sensor_sel_start")
    enable_main_window()

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
main_sensor_sel_win.sensor_selection_DONE_Button.clicked.connect(
    lambda: sensor_sel_start())  # Close() DONE in UI.
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
main_window.main_tab_LocalizationSettings_Name_lineEdit
main_window.main_tab_LocalizationSettings_LOAD_LOCATION_button
main_window.main_tab_LocalizationSettings_SAVE_LOCATION_button
main_window.main_tab_LocalizationSettings_longitudLineEdit
main_window.main_tab_LocalizationSettings_latitudLineEdit
main_window.main_tab_LocalizationSettings_hourLineEdit
main_window.main_tab_LocalizationSettings_minutesLineEdit
main_window.main_tab_LocalizationSettings_secondsLineEdit
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
# main_window.main_tab_START_button.clicked.connect(lambda: show_main_sens_sel_window()) #this was the one before
main_window.main_tab_START_button.clicked.connect(lambda: start_aquisition())
# Visualization
main_window.visualize_tab_tableWidget
main_window.visualize_tab_TIME_button
main_window.visualize_tab_FFT_button
main_window.visualize_tab_APS_button
main_window.visualize_tab_XPS_button
main_window.visualize_tab_PHASE_button
main_window.visualize_tab_COHERE_button

# ------------------------------------------- MAIN WINDOW -------------------------------------------------
"""
Prepares GUI and sends request to control module for begin recording data.
"""


def action_Begin_Recording():
    instruc_man = ins_man.instruction_manager()
    # Activate App Running Dialog.
    # Send Setting Information to Control Module.
    instruc_man.send_set_configuration('Configuration String.')
    # Prepare Real-Time Plot to receive Data.
    # Send Begin Recording FLAG to Control Module.
    instruc_man.send_request_start()

    # Close Window
    main_sensor_sel_win.close()

    # Show Progress Dialog
    show_progress_dialog('Test Message')


"""
Shows the Main Sensor Selection Window.

CALL BEFORE SENDING REQUEST TO START.
"""


def ask_for_sensors():
    # User Select which sensors it wants.
    show_main_sens_sel_window()
    # When Done pressed --> begin recording. | this is handled from UI.


# ------------------------------------------- ACQUIRE DIALOG -------------------------------------------------
"""
Shows Dialog with 'Acquiring' as the title beginning.

:param message : the desired dialog message.
"""


def show_acquire_dialog(message: str):
    # Set progress  # TODO LEARN

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
    im = ins_man.instruction_manager()
    im.send_cancel_request()
    enable_main_window()


# ------------------------------------------- ACQUIRE DIALOG -------------------------------------------------
"""
Saves sensor data from UI into structure.
"""


def save_sesnor_info():
    # Get info from GUI.
    # Set info to correct Data Structure.
    # Set sensor info (4)
    sens_1 = sens.Sensor('NAME', 'Sensor_1 description', 'sensitivity', 'where am i?')
    sens_2 = sens.Sensor('NAME', 'Sensor_2 description', 'sensitivity', 'where am i?')
    sens_3 = sens.Sensor('NAME', 'Sensor_3 description', 'sensitivity', 'where am i?')
    sens_4 = sens.Sensor('NAME', 'Sensor_4 description', 'sensitivity', 'where am i?')

    # Set channel sensors.
    channel = chan.Channel('NAME', sens_1, sens_2, sens_3, sens_4)

    main_window.show()
    # show_progress_dialog()
    # sensor_sel.show()
    # mod_sel.show()
    # channel_info_win.show()
    app.exec()
