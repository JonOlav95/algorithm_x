from node import *


class NodeMatrix:

    def __init__(self, matrix, sudoku_raw):
        # Note down the size of the sudoku board
        self._rows = len(matrix)
        self._columns = len(matrix[0])
        self._size = len(sudoku_raw)
        self._matrix = matrix



    ''' Current implementation of the matrix creates all the nodes then connects them
        A better solution could be to simultaneously create and connect the nodes'''
    # TODO: This function requires rework as it complexity is too high
    def construct_matrix(self):

        header = HeaderNode()
        link_matrix = [[None for i in range(self._columns)] for j in range(self._rows + 1)]

        column = header

        # TODO: A column might be empty
        for i in range(self._columns):
            new_column = ColumnNode()

            new_column.x = i
            new_column.y = 0

            new_column.left = column
            column.right = new_column

            column = new_column

            link_matrix[0][i] = column

            row_node = column
            for j in range(self._rows):

                if self._matrix[j][i] == 1:
                    new_row_node = Node()

                    # TODO: Currently works but lacks readability
                    link_matrix[0][i].node_amount += 1

                    new_row_node.x = i
                    new_row_node.y = j

                    new_row_node.up = row_node
                    row_node.down = new_row_node

                    row_node = new_row_node

                    link_matrix[j + 1][i] = row_node

            row_node.down = column
            column.up = row_node

        column.right = header
        header.left = column

        column = header

        for i in range(self._columns):
            column = column.right

            for j in range(self._rows):

                if self._matrix[j][i] == 1:

                    row_node = link_matrix[j + 1][i]

                    if row_node.right is None:

                        for k in range(i + 1, self._columns):

                            if self._matrix[j][k] == 1:
                                next_row_node = link_matrix[j + 1][k]

                                row_node.right = next_row_node
                                next_row_node.left = row_node

                                row_node = next_row_node

                        for n in range(0, i):

                            if self._matrix[j][n] == 1:
                                next_row_node = link_matrix[j + 1][n]

                                row_node.right = next_row_node
                                next_row_node.left = row_node

                                row_node = next_row_node

        return header, link_matrix
