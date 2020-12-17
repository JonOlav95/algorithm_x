import copy

from exact_cover.algorithmx_helpers import print_solution, exact_to_arr
from exact_cover.exact_cover_problem import construct_problem
from exact_cover.dancing_links_matrix import *


class AlgorithmX:
    """Algorithm X.

    Attributes:
        _matrix: The matrix with size 729*324 for a 9-size Sudoku puzzle. This matrix is
        filled with 1s and 0s only and is used to represent the exact cover problem.
        _rows: The total amount of rows in _matrix.
        _columns: The total amount of columns in _matrix.
        _size: The total size of the puzzle.
        _solution: Potential solutions will be added and removed from this list as the
        algorithm progresses.
        _final_solution: The final solution when the algorithm is finished.
        _link_matrix: The dancing links matrix.
        _header: The dummy node which points to the first and last header in the link matrix.
    """
    def __init__(self):
        self._size = 9
        self._matrix = construct_problem(self._size)
        self._rows = len(self._matrix)
        self._columns = len(self._matrix[0])
        self._solution = []
        self._final_solution = []


        if self._columns != 0:
            self._link_matrix = dl_matrix(self._matrix, self._columns, self._rows)
            self._header = connect_dl(self._matrix, self._link_matrix, self._columns, self._rows)

    def solve(self, board):
        """The public solve function which initiates the algorithm.

        Args:
            board: The Sudoku puzzle as a matrix of integers.

        Returns:
            The solution as a matrix of integers. An empty list if there is no solution.
        """
        self._solution.clear()
        self._final_solution.clear()
        self._initial_state(board)
        self._solve()

        # Reconnect the dancing links nodes to the correct connections.
        self._header = connect_dl(self._matrix, self._link_matrix, self._columns, self._rows)

        return exact_to_arr(self._size, self._final_solution)

    def _initial_state(self, sudoku_raw):
        """Adds the rows which are part of the initial puzzle.

        Args:
            sudoku_raw: Matrix of integers with represent the puzzle.
        """
        raw_rows = len(sudoku_raw)
        raw_columns = len(sudoku_raw[0])
        raw_size = raw_rows

        counter = 0

        for i in range(raw_rows):
            for j in range(raw_columns):

                value = sudoku_raw[i][j]

                if value == 0:
                    continue

                r = value + j * raw_size + counter * raw_size
                c = j + raw_size * i

                node = self._link_matrix[r][c]
                self._solution.append(node.y)

                self._cover(node)
                right_node = node.right

                while right_node != node:
                    self._cover(right_node)
                    right_node = right_node.right

            counter += self._size

    def _cover(self, node):
        """Cover a column and the connected nodes.

        Args:
            node: The node which indicates the locations that will be covered.
        """
        column_node = self._link_matrix[0][node.x]

        column_node.covered = True
        column_node.left.right = column_node.right
        column_node.right.left = column_node.left

        row_node = column_node.down

        while row_node != column_node:

            right_node = row_node.right

            while right_node != row_node:
                right_node.up.down = right_node.down
                right_node.down.up = right_node.up

                self._link_matrix[0][right_node.x].node_amount -= 1

                right_node = right_node.right

            row_node = row_node.down

    def _uncover(self, node):
        """The uncover process when the solve method is backtracking.

        This function is used when the algorithm needs to backtrack and remove
        values from it current solution. This will put previously covered nodes back
        into play to be a potential part of the new solution.

        Args:
            node: The node where the uncover process will begin.
        """
        column_node = self._link_matrix[0][node.x]

        row_node = column_node.up

        while row_node != column_node:

            left_node = row_node.left

            while left_node != row_node:
                left_node.up.down = left_node
                left_node.down.up = left_node

                self._link_matrix[0][left_node.x].node_amount += 1

                left_node = left_node.left

            row_node = row_node.up

        column_node.covered = False
        column_node.left.right = column_node
        column_node.right.left = column_node

    def _find_minimum(self):
        """Finds the column with the least amount of nodes connected to it"""
        node = self._header.right

        minimum = node.node_amount
        minimum_node = node

        while node != self._header:

            if node.node_amount < minimum:
                minimum_node = node
                minimum = node.node_amount

            node = node.right

        return minimum_node

    def _solve(self):
        """The recursive heart of the algorithm."""

        # If the linked list is empty, a solution has been found
        if self._header.right == self._header:
            self._final_solution = copy.copy(self._solution)
            print_solution(self._size, self._solution)
            return True

        # Find the column with the least amount of nodes
        column_node = self._find_minimum()
        self._cover(column_node)

        row_node = column_node.down
        # The loop browses down the column with the least amount of nodes and
        # adds the first row to the solution array. If the row does not fit it
        # is removed from the solution array, and the next row is added.
        while row_node != column_node:

            self._solution.append(row_node.y)
            right_node = row_node.right

            while right_node != row_node:
                self._cover(right_node)
                right_node = right_node.right

            # If a solution was found, return True.
            if self._solve():
                return True

            self._solution.pop()

            left_node = row_node.left

            while left_node != row_node:
                self._uncover(left_node)
                left_node = left_node.left

            row_node = row_node.down

        self._uncover(column_node)
        return False


