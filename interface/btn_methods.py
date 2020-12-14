from backtracking.backtrack import Backtrack
from boards.pick_board import pick_board
from constraint import check_board
from interface.helpers import btn_to_arr
from interface.sudoku_state import store_state
from exact_cover.sudoku_solver import SudokuSolver


def check_method(cells, king_check, knight_check, check_text):
    """Checks if the board is correct or not.

    Args:
        cells: Matrix of QPushButtons which represents the Sudoku board.
        king_check: Boolean which represents if the king constraint is on.
        knight_check: Boolean which represents if the knight constraint is on.
        check_text: QTextEdit used to display information to the user.
    """
    arr = btn_to_arr(cells)
    king = king_check.isChecked()
    knight = knight_check.isChecked()

    correct = check_board(arr, king, knight)

    for line in arr:
        if 0 in line:

            if not correct:
                check_text.setText("Missing values and puzzle contains constraint mistakes.")
            else:
                check_text.setText("Missing values.")
            return

    if not correct:
        check_text.setText("Not correct.")
        return

    check_text.setText("Correct.")


def generate_method(cells, states, king_check, knight_check):
    """Picks an example board which fits the constraint criteria.

    Args:
        cells: Matrix of QPushButtons which represents the Sudoku board.
        king_check: Boolean which represents if the king constraint is on.
        knight_check: Boolean which represents if the knight constraint is on.
        states: A list of the object SudokuState.
    """
    king = king_check.isChecked()
    knight = knight_check.isChecked()

    board = pick_board(king, knight)
    arr = btn_to_arr(cells)
    states.append(store_state(arr))

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                cells[i][j].setText(str(board[i][j]))


def clear_method(cells, states):
    """Clear the entire Sudoku board.

    Clear the entire board by removing the text on the QPushButtons.
    In addition also updates the state so the undo action can be performed
    after clearing.

    Args:
        cells: Matrix of QPushButtons which represents the Sudoku board.
        states: A list of the object SudokuState.
    """
    arr = btn_to_arr(cells)
    states.append(store_state(arr))

    for row in cells:
        for cell in row:
            cell.setText("")


def solve_method(cells, king_check, knight_check, check_text, states):
    """Solve the given Sudoku Board.

    Args:
        cells: Matrix of QPushButtons which represents the Sudoku board.
        king_check: Boolean which represents if the king constraint is on.
        knight_check: Boolean which represents if the knight constraint is on.
        check_text: QTextEdit used to display information to the user.
        states: A list of the object SudokuState.
    """
    arr = btn_to_arr(cells)
    king = king_check.isChecked()
    knight = knight_check.isChecked()

    states.append(store_state(arr))

    if not check_board(arr, king, knight):
        check_text.setText("Invalid Board")
        return

    if not king and not knight:
        algorithm_x = SudokuSolver(arr)
        solved = algorithm_x.solve()
    else:
        backtrack = Backtrack(arr)
        backtrack.king = king
        backtrack.knight = knight
        solved = backtrack.solve()

    if not solved:
        check_text.setText("No solution.")
        return

    for y in range(9):
        for x in range(9):
            cells[y][x].setText(str(solved[y][x]))


def undo_method(cells, states):
    """Undo the last action performed by going back to the previous state.

    Args:
        cells: Matrix of QPushButtons which represents the Sudoku board.
        states: A list of the object SudokuState.
    """
    if len(states) == 0:
        return

    last_action = states[-1]
    states.pop()

    for i in range(len(last_action.val)):

        x = last_action.x[i]
        y = last_action.y[i]
        old = last_action.val[i]

        if old == 0:
            cells[x][y].setText("")
        else:
            cells[x][y].setText(str(old))