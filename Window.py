from PyQt5 import QtWidgets
# import Main_Window
from PyQt5.QtWidgets import QFileDialog

from regex import regex

# Global Variables.
# MAX_DURATION = {  # Max allowed Duration in seconds TODO Remove if safe.
#     '2 Hz': 1800,
#     '4 Hz': 1800,
#     '8 Hz': 1800,
#     '16 Hz': 1800,
#     '32 Hz': 1800,
#     '64 Hz': 1800,
#     '128 Hz': 1365,
#     '256 Hz': 682,
#     '512 Hz': 341,
#     '1024 Hz': 170,
#     '2048 Hz': 85,
#     '4096 Hz': 42,
#     '8192 Hz': 21,
#     '16384 Hz': 10,
#     '20000 Hz': 8,
#     'Please Select': -1}
# MIN_DURATION = 5  # Min allowed Duration in seconds TODO Remove if safe.


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.init_objects()

        pass

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

        :return:
        """
        self.display_error('Device not connected. <br> <br>'
                           'Inspect all connections and power cables are properly connected.')

    def file_system(self, root_path: str):
        """
        Opens a File system window on root path.

        :param root_path: Path in which File System window will open.

        :return:
        """

        path = str(QFileDialog.getOpenFileName(None, 'Open CSV File', root_path, 'CSV Files (*.csv)')[0])

        if validate_path(path):
            return path
        else:
            self.display_error('Choose a file from the default file path.!')
            return ''

    # TODO how to implement abstract methods and make sure all inherited uses it.
    def init_objects(self):
        """
        Abstract Method that every child MUST Implement.

        :return:
        """

        pass


def validate_path(path: str):
    """
    Ensures Data Files is opened from within allowed path.
    Also verifies if Filename ends in .csv for redundancy as the File Explorer already does this.

    :param path: User requested file path [may be file name with full path.]

    :return: True if Data Files is opened from within allowed path.
    """
    validated = False
    # Keep to validate Filename : Done like this to maintain Code clarity and naming convention on functions.
    filename = path

    if '/EWAS_Application/' in path:  # If user cancels --> Path is empty --> NOT VALID
        validated = True

    return validated and validate_filename(filename)


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
