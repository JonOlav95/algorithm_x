
class Node:
    """A node used to represent one cell in the Sudoku board.

    Attributes:
        value: The current value the node holds in the Sudoku game.
        x: The horizontal position of the node.
        y: The vertical position of the node.
        initial: Whether or not the node is a part of the initial solution. If the node is an initial node
        the value will not be changed.
    """
    def __init__(self):
        self.value = -1
        self.x = -1
        self.y = -1
        self.initial = False


def arr_to_node(board):
    """Creates a matrix of Nodes from a matrix of integers.

    The matrix of Nodes is used in the backtracking algorithm to solve the board.

    Args:
        board: A matrix of integers which represents the Sudoku board.

    Returns:
        matrix: A matrix of nodes which represents the Sudoku board.
    """
    matrix = [[Node() for i in range(len(board))] for j in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            matrix[i][j].x = i
            matrix[i][j].y = j

            if board[i][j] != 0:
                matrix[i][j].value = board[i][j]
                matrix[i][j].initial = True

    return matrix


def node_to_arr(node_matrix):
    """Creates a matrix of integers from a matrix of Nodes.

    Used after the backtracking algorithm is done to return a more common format
    of the sudoku board.

    Args:
        node_matrix: A matrix of Nodes which represents the Sudoku board.

    Returns:
        sol: A matrix of integers which represents the Sudoku board.
    """
    sol = []

    for y in range(9):

        row = []
        for x in range(9):
            row.append(node_matrix[y][x].value)

        sol.append(row)

    return sol


def print_board(node_matrix):
    """Prints the Sudoku board in the console.

    Args:
        node_matrix: A matrix of Nodes which represents the Sudoku board.
    """
    for y in range(9):
        for x in range(9):
            node = node_matrix[y][x]
            val = 0

            if node.value != -1:
                val = node.value

            print(str(val) + " ", end="")

        print("")
    print("")
