from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QTextEdit, QPushButton


class SudokuGUI(QMainWindow):
    """The class used to create the Sudoku GUI.

    This class is responsible for the GUI elements of the program.
    It is not responsible for functionality of the program, for example it
    creates the buttons but does not decide what the buttons do.

    Attributes:
        cells: Each Sudoku cell/node as a QPushButton.
        king_check: QCheckBox for king constraint to be enabled.
        knight_check: QCheckBox for knight constraint to be enabled.
        check_text: QTextEdit used to display information to the user.
        generate_btn: QPushButton used to pseudo generate a unsolved Sudoku board.
        undo_btn: QPushButton used to undo the latest actions performed by the user.
        clear_btn: QPushButton used to clear the entire board.
        solve_btn: QPushButton used to solve the board.
    """
    def __init__(self, *args, **kwargs):
        super(SudokuGUI, self).__init__(*args, **kwargs)

        self.move(700, 250)
        self.setFixedHeight(462)
        self.setFixedWidth(620)
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Sudoku")

        self.cells = []

        self.check_text = QTextEdit(self)
        self.check_text.setReadOnly(True)
        self.check_text.move(465, 255)
        self.check_text.resize(150, 150)
        self.check_text.setStyleSheet("background-color: lightblue;")
        self.check_text.setText("")

        self.knight_check = QCheckBox(self)
        self.knight_check.resize(75, 25)
        self.knight_check.move(465, 5)
        self.knight_check.setText("Knight")
        self.knight_check.setChecked(False)
        self.knight_check.setStyleSheet("background-color: #33afff;")

        self.king_check = QCheckBox(self)
        self.king_check.resize(75, 25)
        self.king_check.move(540, 5)
        self.king_check.setText("King")
        self.king_check.setChecked(False)
        self.king_check.setStyleSheet("background-color: #33afff;")

        self.generate_btn = self._create_button(465, 35, "Generate")
        self.undo_btn = self._create_button(465, 90, "Undo")
        self.clear_btn = self._create_button(465, 145, "Clear")
        self.check_btn = self._create_button(465, 200, "Check")
        self.solve_btn = self._create_button(465, 410, "Solve")

        self._create_board()

    def _create_board(self):
        """Arithmetically creates a Sudoku board of QPushButtons."""
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
                cell_row.append(cell)

            self.cells.append(cell_row)

    def _create_button(self, x, y, text):
        """Create a button with the same style.

        Args:
            x: The x-position of the button.
            y: The y-position of the button.
            text: The text on the button.

        Returns:
            The button as a QPushButton element.
        """
        button = QPushButton(self)
        button.setText(text)
        button.move(x, y)
        button.resize(150, 50)
        button.setStyleSheet("background-color: #33afff;")

        return button
