# Not going to do a class because only 1 instance of this window will only have one instance.
from PyQt5 import QtWidgets, uic
from Control_Module_Comm import instruction_manager as im

# app = QtWidgets.QApplication([])
# main_window = uic.loadUi("main_tab_layout_V2.ui")
# TODO CREATE AND IMPORT APP RUNNING DIALOG.

def action_Begin_Recording():
    instruc_man = im.instruction_manager()
    instruc_man.send_request_start()
    # Activate App Running Dialog.
    # Send Setting Information to Control Module.
    # Prepare Real-Time Plot to receive Data.
    # Send Begin Recording FLAG to Control Module.



