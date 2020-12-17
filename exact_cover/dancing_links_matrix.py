from exact_cover.ec_node import *


def dl_matrix(matrix, columns, rows):
    """Create a matrix of nodes from the matrix of integers.

    Note that this function does not connect the nodes, this function simply creates
    the matrix unconnected.

    Args:
        matrix: The matrix of integers which represent the sudoku exact cover problem.
        columns: The total amount of columns in the matrix.
        rows: The total amount of rows in the matrix.

    Returns:
        A matrix of nodes.
    """
    link_matrix = [[None for i in range(columns)] for j in range(rows + 1)]

    for i in range(columns):
        new_column = ColumnNode()
        new_column.x = i
        new_column.y = 0

        link_matrix[0][i] = new_column

        for j in range(rows):

            if matrix[j][i] != 1:
                continue

            node = Node()
            node.x = i
            node.y = j

            link_matrix[j + 1][i] = node

    return link_matrix


def connect_dl(matrix, link_matrix, columns, rows):
    """Connects all the nodes appropriately in the node matrix.

     Args:
         matrix: The matrix of integers.
         link_matrix: The matrix of nodes.
         columns: The total amount of columns in the matrix.
         rows: The total amount of rows in the matrix.

     Returns:
         The header node which points to the beginning and end of the matrix.
     """
    header = HeaderNode()

    link_matrix[0][0].left = header
    link_matrix[0][columns - 1].right = header

    header.right = link_matrix[0][0]
    header.left = link_matrix[0][columns - 1]

    for i in range(0, columns):

        column = link_matrix[0][i]
        column.node_amount = 9

        if i != 0:
            column.left = link_matrix[0][i - 1]
            link_matrix[0][i - 1].right = column

        # Up down connections
        row_node = column
        for j in range(rows):

            if matrix[j][i] != 1:
                continue

            row_node.down = link_matrix[j + 1][i]
            link_matrix[j + 1][i].up = row_node

            row_node = link_matrix[j + 1][i]

            itr_node = link_matrix[j + 1][i]
            if itr_node.right is None:
                for k in range(i + 1, columns):
                    if matrix[j][k] == 1:
                        next_row_node = link_matrix[j + 1][k]

                        itr_node.right = next_row_node
                        next_row_node.left = itr_node

                        itr_node = next_row_node

                for n in range(0, i):
                    if matrix[j][n] == 1:
                        next_row_node = link_matrix[j + 1][n]

                        itr_node.right = next_row_node
                        next_row_node.left = itr_node

                        itr_node = next_row_node

        row_node.down = column
        column.up = row_node

    return header
