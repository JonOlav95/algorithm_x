from PyQt5.Qt import *
from functools import partial
from interface.btn_methods import *
from interface.gui_parent import SudokuGUI
from interface.sudoku_state import SudokuState, cell_change


class MainWindow(SudokuGUI):
    """The main window.

    Is responsible for the functionality of the GUI elements. Also responsible for
    dynamic GUI changes.

    Attributes:
        states: A list of the previous states of the Sudoku board. Used to go back
        to a previous state with the undo button.
        _target_x: The current x-position of the targeted cell (integer).
        _target_y: The current y-position of the targeted cell (integer).
        _target_cell: The current cell being targeted (QPushButton).
        _algorithm_x: Used to solve regular Sudoku.
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.states = []
        self._target_x = 0
        self._target_y = 0
        self._target_cell = None
        self._algorithm_x = AlgorithmX()

        self._btn_connect()

    def _btn_connect(self):
        """Connects the QPushButtons to the appropriate functions"""

        self.undo_btn.clicked.connect(partial(undo_method, self.cells, self.states))
        self.clear_btn.clicked.connect(partial(clear_method, self.cells, self.states))
        self.check_btn.clicked.connect(partial(check_method, self.cells, self.king_check,
                                               self.knight_check, self.check_text))
        self.solve_btn.clicked.connect(partial(solve_method, self.cells, self.king_check,
                                               self.knight_check, self.check_text, self.states, self._algorithm_x))
        self.generate_btn.clicked.connect(partial(generate_method, self.cells, self.states,
                                                  self.king_check, self.knight_check))

        for i in range(9):
            for j in range(9):
                self.cells[i][j].clicked.connect(partial(self.cell_click, self.cells[i][j], i, j))

    def cell_click(self, cell, x, y):
        """Color change of a cell when clicked.

        Change the background color of a cell when clicked, and likewise change the
        color of the previously clicked cell (if any) to the normal background color.

        Args:
            cell: The QPushButton being clicked:
            x: The x-position of the cell.
            y: The y-position of the cell.
        """

        # If the same cell is clicked twice the cell should be untargeted.
        if self._target_cell is cell:
            self._target_cell.setStyleSheet("background-color: white; border: 1px solid black;")
            self._target_cell = None
            self._target_x = -1
            self._target_y = -1
            return

        # If a previous cell has been targeted, untarget it.
        if self._target_cell is not None:
            self._target_cell.setStyleSheet("background-color: white; border: 1px solid black;")

        self._target_x = x
        self._target_y = y
        self._target_cell = cell
        cell.setStyleSheet("background-color: lightblue; border: 1px solid black;")

    def keyPressEvent(self, event):
        """Overriding the keyPressEvent function from QWidget.

        Args:
            event: The event happening in the window,will only be used
            for certain keyboard input.
        """
        if event.key() == Qt.Key_1:
            self._sudoku_key(1)

        elif event.key() == Qt.Key_2:
            self._sudoku_key(2)

        elif event.key() == Qt.Key_3:
            self._sudoku_key(3)

        elif event.key() == Qt.Key_4:
            self._sudoku_key(4)

        elif event.key() == Qt.Key_5:
            self._sudoku_key(5)

        elif event.key() == Qt.Key_6:
            self._sudoku_key(6)

        elif event.key() == Qt.Key_7:
            self._sudoku_key(7)

        elif event.key() == Qt.Key_8:
            self._sudoku_key(8)

        elif event.key() == Qt.Key_9:
            self._sudoku_key(9)

        elif event.key() == Qt.Key_Backspace or event.key() == Qt.Key_Delete:
            if self._target_cell is not None:
                if self._target_cell.text is not "":
                    state_change = cell_change(self._target_cell, self._target_x, self._target_y)
                    self.states.append(state_change)
                    self._target_cell.setText("")

    def _sudoku_key(self, val):
        """When a cell is clicked.

        The state of the cell being changed is stored, and the new value is applied
        by changing the text of the QPushButton cell.

        Args:
            val: The value which the cell will be changed to.
        """
        if self._target_cell is not None:
            state_change = cell_change(self._target_cell, self._target_x, self._target_y)
            self.states.append(state_change)
            self._target_cell.setText(str(val))
