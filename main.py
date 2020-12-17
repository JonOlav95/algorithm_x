import sys
from PyQt5.QtWidgets import QApplication
from interface.main_window import MainWindow


"""Initiate the application by running this function."""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

