from PyQt5 import uic
from PyQt5.QtCore import QThread


class progress_dialog_window(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.progress_dialog = uic.loadUi("GUI/progress_dialog_v1.ui")
        print()

    def __del__(self):
        self.wait()

    def run(self):
        self.progress_dialog.show()
        print("set show on progress dialog")
