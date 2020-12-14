class SudokuState:
    """Saves the state of the Sudoku board before a change.

    Use lists to save the state of the board before a change is made.
    A change can be one node or multiple nodes at the same time, therefore lists are used.

    Attributes:
        x: The x-position of the node(s) being changed.
        y: The y-position of the node(s) being changed.
        val: The value of the node(s) before the change is made.
    """
    def __init__(self):
        self.x = []
        self.y = []
        self.val = []


def store_state(arr):
    """Store the current state of the entire Sudoku Board.

    Used when clearing the entire board or when solving the entire board.

    Args:
        arr: Two-dimensional integer used to represent the Sudoku board.

    Returns:
        The state which represents the current board.
    """
    current = []
    state = SudokuState()

    for i in range(9):
        for j in range(9):
            current.append([i, j])

    for x, y in current:
        state.x.append(x)
        state.y.append(y)
        state.val.append(arr[x][y])

    return state


def cell_change(cell, x, y):
    """Change one state and store the change.

    Args:
        cell: The QPushButton being changed.
        x: The x-position of the changing cell.
        y: The y-position of the changing cell.

    Returns:
        The state change as a SudokuState object.
    """
    state = SudokuState()

    old_val = cell.text()

    if old_val == "":
        old_val = 0
    else:
        old_val = int(old_val)

    state.val.append(old_val)

    state.x.append(x)
    state.y.append(y)

    return state
