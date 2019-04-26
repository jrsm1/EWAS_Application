from PyQt5.QtCore import QThread
import progress_dialog_window as pw

if __name__ == "__main__":
    thread = pw.progress_dialog_window()
    thread.start()
    i = 0
