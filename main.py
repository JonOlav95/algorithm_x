import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

