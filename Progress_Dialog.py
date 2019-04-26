from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon

# FIXME Process finished with exit code -1073740791 (0xC0000409)
#   Error Related to QtThreading.
import GUI_Handler


class ProgressDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProgressDialog, self).__init__()
        self.progress_dialog = uic.loadUi("GUI/Qt_Files/progress_dialog_v1.ui")
        self.progress_dialog.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        # Objects
        self.progress_bar = self.progress_dialog.progress_dialog_progressBar
        self.dlg_title = self.progress_dialog.progress_dialog_title

        # Signals
        self.stop_button = self.progress_dialog.progress_dialog_STOP_button.clicked.connect(lambda: GUI_Handler.cancel_everything())

        pass

    def open(self, message: str):
        """
        Opens Progress Dialog. [Does not create a new instance]
        Default is to 'undetermined' infinite progress.
        To change default behaviour use { void QProgressBar::setRange(int minimum, int maximum) }

        :param message : Custom message to show on Dialog.
        """
        self.dlg_title.setText(message)
        self.progress_dialog.show()

    def close(self):
        """
        Closes Progress Dialog.
        """
        self.progress_dialog.close()
        pass

    def acquire_dialog(self, message: str):
        """
        Progress Dialog Wrapper.
        Shows Dialog with 'Acquiring' as the title beginning.

        :param message : the desired dialog message.
        """

        self.open('Acquiring... ' + message)
