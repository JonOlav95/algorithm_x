from backtracking.backtrack_node import Node


def arr_to_node(arr):

    node_arr = [[Node() for i in range(len(arr))] for j in range(len(arr[0]))]

    for i in range(9):
        for j in range(9):

            node = Node()
            node.x = j
            node.y = i

            if arr[i][j] != 0:
                node.set_value(arr[i][j])

            node_arr[i][j] = node

    return node_arr


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
