import GUI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont


class Error_Dialog():
    def __init__(self, message: str):
        err_dlg = QtWidgets.QMessageBox.warning()
        err_dlg.setWindowIcon(QIcon('GUI/cancel'))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        err_dlg.setFont(font)
        err_dlg.setMinimumSize(800, 350)
        err_dlg.showMessage(message)
        err_dlg.exec()
        # err_dlg.

#TESTING
err = Error_Dialog('Some Error')
