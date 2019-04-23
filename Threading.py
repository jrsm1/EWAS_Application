from PyQt5 import QtCore
from PyQt5.QtCore import *
from Control_Module_Comm import instruction_manager as ins_man
import time
import serial

class QThreadGps(QtCore.QThread):
    signal_error = pyqtSignal(bool)
    signal_synced = pyqtSignal(bool)
    signal_not_synced = pyqtSignal(bool)

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.running = True
        port = 'COM-1'
        global ins_port
        pid = "0403"
        hid = "6001"
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if pid and hid in p.hwid:
                port = p.device
        ins_port = port
        try:
            # while self.running:
                ins = ins_man.instruction_manager(ins_port)
                ins.send_gps_sync_request()
                timeout = 0
                synced = True  # Used to not request data if synched==False.
                while ins.send_request_status()[2] != 1:  # Status[2] --> gps_synched
                    print('GPS Waiting....')
                    time.sleep(2)  # Wait for half a second before asking again.
                    timeout += 1
                    if timeout == 2 * 2:  # = [desired timeout in seconds] * [1/(sleep value)]
                        self.signal_not_synced.emit(True)
                        break
                if synced:
                    self.signal_synced.emit(True)
        except serial.SerialException:
            self.signal_error.emit(True)
