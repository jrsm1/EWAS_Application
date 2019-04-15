# Not going to do a class because only 1 instance of this window will only have one instance.
from PyQt5 import QtWidgets, uic
from Control_Module_Comm import instruction_manager as im
from GUI import GUI_Handler


# app = QtWidgets.QApplication([])
# main_window = uic.loadUi("main_tab_layout_V2.ui")
# TODO CREATE AND IMPORT APP RUNNING DIALOG.


def action_Begin_Recording():
    instruc_man = im.instruction_manager()
    # Activate App Running Dialog.
    # Send Setting Information to Control Module.
    instruc_man.send_set_configuration('Configuration String.')
    # Prepare Real-Time Plot to receive Data.
    # Send Begin Recording FLAG to Control Module.
    instruc_man.send_request_start()

    # Close Window
    GUI_Handler.main_sensor_sel_win.close()

    # Show Progress Dialog
    GUI_Handler.show_progress_dialog('Test Message')


def action_store_DAQ_Params():
    sc = Sensor_Individual.Sensor('Name', 0)
    cc = Channel_Individual.Channel('mName', sc, sc, sc, sc)
    daq = DAQ_Configuration.DAQconfigs()
    sfm = Setting_File_Manager(cc, sc, daq)


def ask_for_sensors():
    # User Select which sensors it wants.
    GUI_Handler.show_main_sens_sel_window()
    # When Done pressed --> begin recording. | this is handled from UI.
