import sys
from time import sleep

import serial
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon

import Exceptions
import Window
from Control_Module_Comm import instruction_manager as ins_man
from Control_Module_Comm.Structures import Module_Individual, DAQ_Configuration, Sensor_Individual
from Main_Window import MainWindow
from Progress_Dialog import ProgressDialog
from Save_Data_Option_Dialog import SaveDataOptionDialog
from Sensor_Selection_Matrix import SensorSelectionMatrix
from Settings import setting_data_manager as set_dat_man
from Window import Window
from Data_Processing.CSV_Handler import Data_Handler

app = QtWidgets.QApplication([])
file_sys_win = uic.loadUi('GUI/Qt_Files/file_system_window.ui')
module_2_info_win = uic.loadUi("GUI/Qt_Files/module_1_info_window.ui")

file_sys_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))
module_2_info_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))


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
mod_1 = Module_Individual.Module('Module 1', sens_1, sens_2, sens_3, sens_4)
mod_2 = Module_Individual.Module('Module 2', sens_5, sens_6, sens_7, sens_8)
mod_3 = Module_Individual.Module('Module 3', sens_9, sens_10, sens_11, sens_12)
mod_4 = Module_Individual.Module('Module 4', sens_13, sens_14, sens_15, sens_16)
mod_5 = Module_Individual.Module('Module 5', sens_17, sens_18, sens_19, sens_20)
mod_6 = Module_Individual.Module('Module 6', sens_21, sens_22, sens_23, sens_24)
mod_7 = Module_Individual.Module('Module 7', sens_25, sens_26, sens_27, sens_28)
mod_8 = Module_Individual.Module('Module 8', sens_29, sens_30, sens_31, sens_32)
modules_all = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6, mod_7,
               mod_8]  # Used to get channels easily (goes from 0 to 7)

# ----------- CONFIGS ----------
daq_config = DAQ_Configuration.DAQconfigs()
base_window = Window()
setting_data_manager = set_dat_man.Setting_File_Manager(daq_config=daq_config, module_config=modules_all)
main_window = MainWindow(daq_configuration=daq_config, setting_manager=setting_data_manager, modules=modules_all)
store_data_window = SaveDataOptionDialog(daq_config)
sensor_matrix = SensorSelectionMatrix()
prog_dlg = ProgressDialog()

# TESTING purposes
log = 1
log_working = 0

# Global Variables.
stop_break_loop = True
# status global variables
recorded = 0
stored = 0
gps_sync = 0
ins_port = 'COM-1'
start_diagnose_decision = 0
START_TEST = 1
DIAGNOSE = 2

def get_sensor_enabled():
    sensor_enable = []
    if log: print("entered get_module_and_sensors_selected()")
    if log: print("created empy sensor selected array")

    # for i in main_sensor_selection_list:
    for i in sensor_enable:
        sensor_enable.append(i.checkState())

    return sensor_enable


def start_acquisition(who_called: int):
    """
    Begin Acquisition Process
    """
    global start_diagnose_decision
    error_string = ''
    error_string += main_window.validate_rec_settings()
    loc_type = main_window.loc_type_dropdown.currentIndex()
    if not loc_type:
        error_string += main_window.validate_gps_location_settings()
    else:
        # specimen by module
        error_string += main_window.nvalidate_module_location_settings()

    if not main_window.validate_daq_params():
        error_string += 'Error: Invalid Signal Parameters. Please select a valid option from the drop-downs.<br>'
    if not error_string:
        if save_port() == 'COM-1':
            base_window.not_connected_error()
        else:
            # Find out who called me
            if who_called == START_TEST:
                start_diagnose_decision = START_TEST
            elif who_called == DIAGNOSE:
                start_diagnose_decision = DIAGNOSE
            # show_main_sens_sel_window()
            store_data_window.open()
    else:
        main_window.display_error(error_string)
    pass

def check_for_port(what_was_clicked: str):
    # if not save_port() == 'COM-1':
    #     if what_was_clicked == 'START':
    #         start_acquisition(START_TEST)
    #     elif what_was_clicked == 'GPS':
    #         sync_gps()
    # else:
    #     main_window.not_connected_error()
    # _________________________________________ TODO change BAck for real.

    if what_was_clicked == 'START':
        start_acquisition(START_TEST)
    elif what_was_clicked == 'GPS':
        sync_gps()


def save_port():  # TODO adapt for class reconstruction
    global ins_port
    port = 'COM-1'
    pid = "0403"
    hid = "6001"
    ports = list(serial.tools.list_ports.comports())

    for p in ports:
        if pid and hid in p.hwid:
            port = p.device
    ins_port = port
    return port

def sync_gps():  # TODO TEST IN ENVIRONMENT WHERE IT DOES SYNC.
    # Show Progress Dialog.
    global stop_break_loop
    stop_break_loop = True
    prog_dlg = ProgressDialog()
    prog_dlg.acquire_dialog('GPS Signal')
    prog_dlg.progress_bar.setMaximum(100)
    prog_dlg.progress_bar.setValue(0)
    app.processEvents()
    try:
        ins = ins_man.instruction_manager(ins_port)
        ins.send_gps_sync_request()
        timeout = 0
        synced = True  # Used to not request data if synched==False.
        while (ins.send_request_status()[2] != 1) and stop_break_loop:  # Status[2] --> gps_synched
            print('GPS Waiting....')
            sleep(0.1)  # Wait for half a second before asking again.
            timeout += 1
            prog_dlg.progress_bar.setValue(timeout * 1.3)
            app.processEvents()
            if timeout == 6 * 10:  # = [desired timeout in seconds] * [1/(sleep value)]
                prog_dlg.progress_bar.setValue(100)
                base_window.display_error('GPS Failed to Synchronize.')
                prog_dlg.close()
                synced = False
                break
        if synced and stop_break_loop:
            prog_dlg.progress_bar.setValue(100)
            ins.send_gps_data_request()
            main_window.set_GPS_into_gui()
        if not stop_break_loop:
            ins.send_cancel_request()
        prog_dlg.close()
        del ins
    except serial.SerialException:
        prog_dlg.close()
        base_window.not_connected_error()

def check_status():
    global recorded, stored, gps_sync
    try:
        ins = Window.get_instruction_manager()
        status = ins.send_request_status()
        recorded = status[0]
        stored = status[1]
        gps_sync = status[2]
        if log:
            print("status = " + str(status))
        return status
    except serial.SerialException:
        base_window.not_connected_error()
        return False
    except Exceptions.noPowerException:
        base_window.display_error('The Control Module appears to be disconnected or has a major power problem.')

def send_diagnostics():
    try:
        im = Window.get_instruction_manager()
        im.send_diagnose_request()
    except serial.SerialException:
        base_window.not_connected_error()

def action_begin_recording(sens: SensorSelectionMatrix, start_diagnose: int):
    """
    Prepares GUI and sends request to control module for begin recording data.
    """
    # Send Setting Information to Control Module.

    # try:
    configuration = setting_data_manager.settings_to_string()

    sens_selected, mods_selected = sensor_matrix.get_modules_and_sensors_selected()
    sens.close()

    sensors_enabled = get_sensor_enabled()
    ins = ins_man.instruction_manager(ins_port)
    # ins.send_set_configuration(setting_data_manager.settings_to_string())
    # Send Begin Recording FLAG to Control Module.
    if start_diagnose == START_TEST:
        if configuration:
            # ins = ins_man.instruction_manager(ins_port)
            # ins.send_set_configuration(configuration)
            bool = ins.send_recording_parameters(sfrequency=daq_config.sampling_rate_index,
                                                 cutoff=daq_config.cutoff_freq_index,
                                                 gain=daq_config.gain_index,
                                                 duration=daq_config.recording_configs["test_duration"],
                                                 start_delay=daq_config.recording_configs["test_start_delay"],
                                                 store_data_sd=daq_config.data_handling_configs["store"],
                                                 sensor_enable=sensors_enabled,
                                                 name="Not Used", location="Not Used")
            # Send Begin Recording FLAG to Control Module.
            print("sent was " + str(bool))
            if bool: sent = True
            sleep(1)
        ins.send_request_start()
    elif start_diagnose == DIAGNOSE:
        ins.send_diagnose_request()
    # Close Window
    sensor_matrix.close()
    check_status_during_test(ins, mods_selected)
    # except serial.SerialException:
    #     show_not_connected_error()
    # except Exceptions.noPowerException:
    #     show_error('The Control Module appears to be disconnected or has a major power problem.')


def check_status_during_test(ins, mods_selected):
    global stop_break_loop
    stop_break_loop = True
    # Prepare Infinite Progress Dialog.
    prog_dlg.acquire_dialog('Test in Progress')
    prog_dlg.progress_bar.setMaximum(0)
    # Setup Local Variables.
    timeout = 0
    synced = True  # Used to not request data if synched==False.
    duration = daq_config.recording_configs['test_duration']
    time_break = 0
    # Wait for Control Module to store data.
    while ins.send_request_status()[1] != 1 and stop_break_loop:  # Status[1] --> stored
        if log: print('Waiting for test to finish....')
        sleep(0.1)
        timeout += 1
        time_break += 1
        app.processEvents()
        if time_break == 10*duration + 100: # timeout in seconds.
            break

    if synced and stop_break_loop:
        print('get all data')
        data_handler = Data_Handler(modules_all, daq_config)
        data_handler.store_data('test.csv', data_handler.request_all_data(mods_selected, ins))

    if not stop_break_loop:
        ins.send_cancel_request()
    prog_dlg.close()
    del ins
    # get_all_data TODO CHANGE TO CSV HANDLER GETT ALL DATA METHOD

    prog_dlg.close()


def get_all_data():
    prog_dlg.acquire_dialog('Test Data')
    prog_dlg.progress_dialog_progressBar.setMaximum(100)
    prog_dlg.progress_dialog_progressBar.setValue(0)
    data = ''
    try:
        ins = Window.get_instruction_manager()
        data = ins.send_request_all_data()
        prog_dlg.close()
    except serial.SerialException:
        data = ''
        base_window.not_connected_error()
        prog_dlg.close()

def cancel_everything():
    """
    Sends Instruction to Control Module to cancel all recording, storing, sending, synchronizing and/or
    any other process the system might be doing.

    Called by user when CANCEL action is desired.
    """

    global stop_break_loop
    stop_break_loop = False

    pass

def auto_fill():
    """
    Auto-fill Main Window with Default Parameters.
    Used for Testing
    """
    main_window.set_recording_into_gui()
    main_window.set_DAQ_params_into_gui()
    main_window.set_GPS_into_gui()

def init():
    """
    Beginning of the program.
    Main will redirect here for GUI setup.
    """
    global ins_port
    main_window.open()
    main_window.enable_gps_disable_spec()  # Begin with GPS only enabled.

    ins_port = save_port()
    # base_window.create_instruction_manager(ins_port)
    # data_handler = Data_Handler(modules_all, daq_config)
    # data_handler.store_data('test.csv', data_handler.request_all_data({1}))

    if ins_port == 'COM-1':
        base_window.display_error('Device Not Connected. Please try again.')
        sleep(2.0)
        # sys.exit()
    else:
        sync_gps()

    auto_fill()

    # --------- TESTING ------------
    # validate_file_path(r'C:\Users\drgdm\OneDrive\Documents\GitHub\EWAS_Application\Data\Huerta _nw301001.csv')
    # begin_visualization()
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
