from backtrack import Backtrack
from constraint import check_board
from gui_helpers import btn_to_arr
from sudoku_action import Action


def check_method(cells, king_check, knight_check, label):

    arr = btn_to_arr(cells)
    king = king_check.isChecked()
    knight = knight_check.isChecked()

    for line in arr:
        if 0 in line:
            label.setText("Missing")
            return

    if not check_board(arr, king, knight):
        label.setText("Wrong")
        return

    label.setText("Correct")


def generate_method(cells):
    sudoku_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    for i in range(9):
        for j in range(9):
            if sudoku_medium[i][j] != 0:
                cells[i][j].setText(str(sudoku_medium[i][j]))


def clear_method(cells, actions):

    arr = btn_to_arr(cells)
    before_clear = []

    for i in range(9):
        for j in range(9):
            if arr[i][j] != 0:
                before_clear.append([i, j])

    action = Action()

    for x, y in before_clear:
        action.x.append(x)
        action.y.append(y)
        action.old_val.append(arr[x][y])
        action.new_val.append(cells[x][y])

    actions.append(action)

    for row in cells:
        for cell in row:
            cell.setText("")


def solve_method(cells, king_check, knight_check, check_text, actions):

    arr = btn_to_arr(cells)
    king = king_check.isChecked()
    knight = knight_check.isChecked()

    if not check_board(arr, king, knight):
        check_text.setText("Invalid Board")
        return

    unfinished = []
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                unfinished.append([i, j])

    backtrack = Backtrack(arr)

    action = Action()

    for x, y in unfinished:
        action.x.append(x)
        action.y.append(y)
        action.old_val.append(0)
        action.new_val.append(cells[x][y])

    actions.append(action)

    backtrack.king = king
    backtrack.knight = knight

    solved = backtrack.b_track()

    for y in range(9):
        for x in range(9):
            cells[y][x].setText(str(solved[y][x]))
