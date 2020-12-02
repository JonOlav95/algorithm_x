import sys
from PyQt5.Qt import *
from functools import partial

from backtrack import Backtrack


def solve_method(cells):

    arr = []

    for row in cells:
        line = []
        for cell in row:
            text = cell.text()

            if text != "":
                line.append(int(cell.text()))

            else:
                line.append(0)

        arr.append(line)

    backtrack = Backtrack(arr)
    solved = backtrack.b_track()

    for y in range(9):
        for x in range(9):
            cells[y][x].setText(str(solved[y][x]))

    print("x")




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFixedHeight(462)
        self.setFixedWidth(800)
        self.setStyleSheet("background-color: black;")

        self.setWindowTitle("Sudoku")

        cells = []
        size = 50
        margin = 1

        for row in range(9):
            cell_row = []
            for column in range(9):
                cell = QLineEdit(self)
                only_int = QIntValidator(1, 9, self)
                cell.setValidator(only_int)

                tmp_x = 0
                tmp_y = 0

                if column >= 3:
                    tmp_x += 2

                if column >= 6:
                    tmp_x += 2

                if row >= 3:
                    tmp_y += 2

                if row >= 6:
                    tmp_y += 2

                cell.setFont(QFont("Callibri", 28))
                cell.resize(size, size)
                cell.move((size + margin) * column + tmp_x, (size + margin) * row + tmp_y)
                cell.setStyleSheet("background-color: white; border: 1px solid black;")
                cell.setAlignment(Qt.AlignCenter)
                cell_row.append(cell)

            cells.append(cell_row)

        btn = QPushButton(self)
        btn.resize(100, 100)
        btn.move(500, 100)
        btn.setStyleSheet("background-color: white;")
        btn.clicked.connect(partial(solve_method, cells))
        btn.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()


