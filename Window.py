from PyQt5 import QtWidgets
# import Main_Window
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget
from Control_Module_Comm import instruction_manager
from regex import regex
import GUI_Handler

# Global Variables.
ins_manager = None

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.init_objects()
        self.center()
        pass

    def center(self):
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

    def create_instruction_manager(self, port):
        global ins_manager
        ins_manager = instruction_manager.instruction_manager(port)
        return ins_manager

    def get_instruction_manager(self):
        return ins_manager


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

    # if no path receives --> user hit cancel --> do nothing.
    if filename == '':
        return True

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

