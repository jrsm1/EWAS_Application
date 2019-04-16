from PyQt5 import QtWidgets
import GUI.Main_Window
import Control_Module_Comm.instruction_manager
from GUI import GUI_Handler

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    GUI_Handler.show_main_window()
    app.exec()

