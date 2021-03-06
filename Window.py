from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget
from regex import regex

# Global Variables.
ins_manager = None

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.center()
        pass

    def center(self):
        """
        Center the window frame in the screen.
        """
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    # TODO how to implement abstract methods and make sure all inherited uses it.
    def open(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """

        pass

    # TODO how to implement abstract methods and make sure all inherited uses it.
    def close(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """
        super().close()

        pass

    def display_error(self, message: str):
        """
        Displays an error dialog with custom Message
        :param message: Error Message to display in Error Dialog.
        :param parent: Window who called the Error Message.

        :return: a Qt StandardButton
        """

        return QtWidgets.QMessageBox().critical(self, 'WARNING', message)

    def not_connected_error(self):
        """
        Displays Error indicating device is not connected.
        """
        self.display_error('Device not connected. <br> <br>'
                           'Inspect all connections and power cables are properly connected.')

    def file_system(self, root_path: str):
        """
        Opens a File system window on root path.

        :param root_path: Path in which File System window will open.
        """

        path = str(QFileDialog.getOpenFileName(None, 'Open CSV File', root_path, 'CSV Files (*.csv)')[0])

        error = validate_path(path)

        if error == '': # if return empty string --> no error
            return path
        elif error == 'path':
            self.display_error('Choose a file from the default file path.!')
            return ''
        elif error == 'cancel':  # if cancel --> user does not want to do anything else.
            pass


def validate_path(path: str):
    """
    Ensures Data Files is opened from within allowed path.
    Also verifies if Filename ends in .csv for redundancy as the File Explorer already does this.

    :param path: User requested file path [may be file name with full path.]

    :return: Empty String if Data Files is opened from within allowed path.
    """
    # Keep to validate Filename : Done like this to maintain Code clarity and naming convention on functions.
    filename = path
    error = ''

    # if no path receives --> user hit cancel --> do nothing.
    if filename == '' or filename is None:
        error = 'cancel'

    elif '/EWAS_Application/' not in path:
        error = 'path'

    return error


def validate_filename(filename: str):
    """
    Validates filename has a CSV File Extension.

    :param filename: The User Input filename to validate.

    :return: True if the file extension is '.csv'
    """
    validated = filename.lower().endswith('.csv')

    return validated


def check_boxes(text_box: str, pattern: str):
    """
    Used for Validation of REGEX Text.

    :param text_box: Plain Text to validate.
    :param pattern: Regex Pattern for validation.

    :return: True if test_box is valid.
    """
    return regex.match(pattern, text_box)

