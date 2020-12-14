import numpy as np


def knight_constraint(arr, x, y, val):
    """Checks for the knight constraint on a Sudoku board.

    The knight constraint checks if a given cell has any surrounding cell of same values.
    The surrounding cells in this scenario is a knight-step away referring to chess.

    Args:
        arr: The Sudoku board as a two-dimensional list of integers.
        x: The x-position of the cell.
        y: The y-position of the cell.
        val: The value which will be tested at the given position.

    Returns:
        True if the value does not break the knight constraint on the given position in the board.
        False otherwise.
    """

    if x != 0:
        if y > 1:
            if val == arr[y - 2][x - 1]:
                return False

        if y < 7:
            if val == arr[y + 2][x - 1]:
                return False

    if x != 8:
        if y > 1:
            if val == arr[y - 2][x + 1]:
                return False

        if y < 7:
            if val == arr[y + 2][x + 1]:
                return False

    if y != 0:
        if x > 1:
            if val == arr[y - 1][x - 2]:
                return False

        if x < 7:
            if val == arr[y - 1][x + 2]:
                return False
    if y != 8:
        if x > 1:
            if val == arr[y + 1][x - 2]:
                return False

        if x < 7:
            if val == arr[y + 1][x + 2]:
                return False

    return True


def king_constraint(arr, x, y, val):
    """Checks for the king constraint on a Sudoku board.

    The king constraint checks if any surrounding cells of a given cell has the same value.

    Args:
        arr: The Sudoku board as a two-dimensional list of integers.
        x: The x-position of the cell.
        y: The y-position of the cell.
        val: The value which will be tested at the given position.

    Returns:
        True if the value does not break the king constraint on the given position in the board.
        False otherwise.
    """

    # Pad 0-values around the matrix to avoid checking if the cell is on the edge of the board.
    pad_arr = np.pad(arr, [(1, 1), (1, 1)], mode="constant", constant_values=0)

    # To compensate for the padding.
    x += 1
    y += 1

    for i in range(-1, 2):
        if pad_arr[y - 1][x + i] == val:
            return False

        if pad_arr[y + 1][x + i] == val:
            return False

    if pad_arr[y][x + 1] == val:
        return False

    if pad_arr[y][x - 1] == val:
        return False

    return True


def constraint_pass_inv(arr, x, y, val):
    """Checks the common constraints on a Sudoku board.

    Checks if a given value fits on the row, column, and block of the board.

    Args:
        arr: The Sudoku board as a two-dimensional list of integers.
        x: The x-position of the cell.
        y: The y-position of the cell.
        val: The value which will be tested at the given position.

    Returns:
        True if the value at the given position does not break any constraints.
        False otherwise.
    """
    for i in range(9):
        if i != x:
            row_cell = arr[y][i]
            if row_cell == val:
                return False

        if i != y:
            column_cell = arr[i][x]
            if column_cell == val:
                return False

    # Finds the correct block arithmetically.
    i = int(x / 3)
    j = int(y / 3)

    for n in range(3 * j, 3 * j + 3):
        for k in range(3 * i, 3 * i + 3):
            if n != y and k != x and arr[n][k] == val:
                return False

    return True


def check_board(arr, king, knight):
    """Checks the entire board if any constraints are broken.

    Args:
        arr: The Sudoku board as a two-dimensional list of integers.
        king: If the king constraint is enabled.
        knight: If the knight constraint is enabled.

    Returns:
        True if any constraint is broken, false otherwise.
    """
    for i in range(9):
        for j in range(9):

            if arr[i][j] == 0:
                continue

            if not constraint_pass_inv(arr, j, i, arr[i][j]):
                print("regular constraint at x: " + str(j) + ", y: " + str(i))
                return False
            if king and not king_constraint(arr, j, i, arr[i][j]):
                print("king constraint at x: " + str(j) + ", y: " + str(i))
                return False
            if knight and not knight_constraint(arr, j, i, arr[i][j]):
                print("knight constraint at x: " + str(j) + ", y: " + str(i))
                return False

    return True
