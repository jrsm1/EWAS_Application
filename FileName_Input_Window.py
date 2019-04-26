from PyQt5 import uic
from PyQt5.QtGui import QIcon

from Window import Window

# TESTING
log = 1

class FileInputWindow(Window):
    def __init__(self, main_window_parent):
        super().__init__()

        self.filename_input_win = uic.loadUi('GUI/Qt_Files/filename_editor_window.ui')
        self.filename_input_win.setWindowIcon(QIcon('GUI/EWAS_Logo_1.svg'))

        self.main_window_parent = main_window_parent

        # Objects
        self.fn_in = self.filename_input_win.filename_lineEdit

        # Signals
        self.fn_OK_btn = self.filename_input_win.filename_OK_button.clicked.connect( lambda: self.main_window_parent.do_saving_loading_action())
        self.fn_CANCEL_btn = self.filename_input_win.filename_CANCEL_button.clicked.connect(lambda: self.close())
        self.fn_in.returnPressed.connect(lambda: self.main_window_parent.do_saving_loading_action())

        pass

    def open(self):
        """
        Opens Filename Input Window. [Does not create a new instance]
        """
        super().open()
        self.filename_input_win.show()

    def close(self):
        """
        Closes Filename Input Window.
        """
        super().close()
        self.filename_input_win.close()

    def validate_filename(self, filename: str):
        """
        Validates filename has a CSV File Extension.

        :param filename: The User Input filename to validate.

        :return: True if the file extension is '.csv'
        """
        validated = filename.lower().endswith('.csv')

        if not validated:
            self.display_error('The File must have a *.csv file extension.')
            if log: print('File Extension Validation: FAILED')

        return validated
