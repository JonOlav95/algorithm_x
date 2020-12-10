from PyQt5.Qt import *
from functools import partial
from gui_buttons import check_method, solve_method, clear_method
from sudoku_action import Action


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.move(700, 250)
        self.setFixedHeight(462)
        self.setFixedWidth(620)
        self.setStyleSheet("background-color: black;")
        self._target_cell = None
        self._target_x = -1
        self._target_y = -1
        self.setWindowTitle("Sudoku")
        self.cells = []
        self.actions = []

        self.king_check = QCheckBox(self)
        self.knight_check = QCheckBox(self)
        self.check_text = QTextEdit(self)
        self.check_text.setReadOnly(True)

        self._create_board()
        self.init_gui()

    def init_gui(self):

        self.check_text.move(465, 255)
        self.check_text.resize(150, 150)
        self.check_text.setStyleSheet("background-color: lightblue;")
        self.check_text.setText("")

        self.knight_check.resize(75, 25)
        self.knight_check.move(465, 5)
        self.knight_check.setText("Knight")
        self.knight_check.setChecked(False)
        self.knight_check.setStyleSheet("background-color: #33afff;")

        self.king_check.resize(75, 25)
        self.king_check.move(540, 5)
        self.king_check.setText("King")
        self.king_check.setChecked(False)
        self.king_check.setStyleSheet("background-color: #33afff;")

        self._create_button(465, 35, "Generate")

        undo_btn = self._create_button(465, 90, "Undo")
        undo_btn.clicked.connect(partial(self.undo))

        clear_btn = self._create_button(465, 145, "Clear")
        clear_btn.clicked.connect(partial(clear_method, self.cells, self.actions))

        check_btn = self._create_button(465, 200, "Check")
        check_btn.clicked.connect(partial(check_method, self.cells, self.king_check, self.knight_check, self.check_text))

        solve_btn = self._create_button(465, 410, "Solve")
        solve_btn.clicked.connect(partial(solve_method, self.cells, self.king_check, self.knight_check, self.check_text, self.actions))

    def _create_board(self):
        size = 50
        margin = 1

        for row in range(9):
            cell_row = []
            for column in range(9):
                cell = QPushButton("", self)

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
                cell.clicked.connect(partial(self.cell_click, cell, row, column))
                cell_row.append(cell)

            self.cells.append(cell_row)

    def _create_button(self, x, y, text):
        button = QPushButton(self)
        button.setText(text)
        button.move(x, y)
        button.resize(150, 50)
        button.setStyleSheet("background-color: #33afff;")

        return button

    def cell_click(self, cell, x, y):

        for row in self.cells:
            for c in row:
                c.setStyleSheet("background-color: white; border: 1px solid black;")

        if self._target_cell is cell:
            self._target_cell = None
            self._target_x = -1
            self._target_y = -1
            return

        if self._target_cell is not None:
            self._target_cell.setStyleSheet("background-color: white; border: 1px solid black;")

        self._target_x = x
        self._target_y = y
        self._target_cell = cell
        cell.setStyleSheet("background-color: lightblue; border: 1px solid black;")

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_1:
            self.sudoku_key(1)

        elif event.key() == Qt.Key_2:
            self.sudoku_key(2)

        elif event.key() == Qt.Key_3:
            self.sudoku_key(3)

        elif event.key() == Qt.Key_4:
            self.sudoku_key(4)

        elif event.key() == Qt.Key_5:
            self.sudoku_key(5)

        elif event.key() == Qt.Key_6:
            self.sudoku_key(6)

        elif event.key() == Qt.Key_7:
            self.sudoku_key(7)

        elif event.key() == Qt.Key_8:
            self.sudoku_key(8)

        elif event.key() == Qt.Key_9:
            self.sudoku_key(9)

        elif event.key() == Qt.Key_Backspace or event.key() == Qt.Key_Delete:
            if self._target_cell is not None:
                if self._target_cell.text is not "":
                    self.save_action(0)
                    self._target_cell.setText("")

    def sudoku_key(self, val):
        if self._target_cell is not None:
            self.save_action(val)
            self._target_cell.setText(str(val))

    def undo(self):
        last_action = self.actions[-1]
        self.actions.pop()

        for i in range(len(last_action.old_val)):

            x = last_action.x[i]
            y = last_action.y[i]
            old = last_action.old_val[i]

            if old == 0:
                self.cells[x][y].setText("")
            else:
                self.cells[x][y].setText(str(old))

    def save_action(self, val):
        action = Action()

        old_val = self._target_cell.text()

        if old_val == "":
            old_val = 0
        else:
            old_val = int(old_val)

        action.old_val.append(old_val)
        action.new_val.append(val)

        action.x.append(self._target_x)
        action.y.append(self._target_y)

        self.actions.append(action)
