from PyQt5 import QtWidgets
import GUI_Handler

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    GUI_Handler.show_main_window()
    app.exec()

