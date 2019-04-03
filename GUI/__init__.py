# import PyQt5
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
main_window = uic.loadUi("main_tab_layout.ui")
channel_info_win = uic.loadUi("channel_info_window.ui")
# err_dlg = uic.loadUi("error_dialog_v1.ui")
prog_dlg = uic.loadUi("progress_dialog_v1.ui")


def start():
    main_window.main_advanced_sample_rate_label.setText("NEW TEXT")

"""
    Creates an Error Message dialog
    :param message: String - The Desired Message Output.
"""
def show_error(message: str):
    err_dlg = QtWidgets.QErrorMessage()
    err_dlg.showMessage(message)
    err_dlg.exec()
"""
Add default functionality here
"""

main_window.main_advanced_HELP_button.clicked.connect(lambda: show_error('This is an Error Message Dialig Box. \n You have done Something Wrong.'))

main_window.show()
app.exec()

