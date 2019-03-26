# import PyQt5
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
main_window = uic.loadUi("main_tab_layout.ui")
channel_info_win = uic.loadUi("channel_info_window.ui")
err_dlg = uic.loadUi("error_dialog_v1.ui")
prog_dlg = uic.loadUi("progress_dialog_v1.ui")


main_window.show()
err_dlg.show()
app.exec()
