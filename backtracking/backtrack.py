from backtracking.backtrack_helpers import arr_to_node, node_to_arr
from constraint import *


class Backtrack:
    """Backtrack algorithm used to solve Sudoku.

    The backtracking algorithm is brute force with a very high worst case complexity.

    Attributes:
        _node_matrix: A matrix of node objects.
        knight: If the knight constraint is enabled.
        king: If the king constraint is enabled.
    """
    def __init__(self, board):

        self._node_matrix = arr_to_node(board)
        self.knight = False
        self.king = False

    def solve(self):
        """The function which initiates the algorithm.

        The solve function attempts to solve the Sudoku board.

        Returns:
            A matrix of integers which represents the solution.
            If the backtracking gets stuck which means there is no solution,
            an empty list is returned instead.
        """
        y = 0
        x = 0

        while y < 9:
            while x < 9 and y < 9:

                node = self._node_matrix[y][x]

                if node.initial:
                    x, y = self._step_forward(x, y)
                    continue

                if node.value == -1:
                    x, y = self._backtrack(x, y, 9)

                else:
                    x, y = self._backtrack(x, y, node.value - 1)

                # This indicates that the algorithm failed to find a solution.
                if y < 0:
                    return []

                x, y = self._step_forward(x, y)

        return node_to_arr(self._node_matrix)

    def _step_forward(self, x, y):
        """One step forward.

        The algorithm moves towards the right and downwards when
        reaching the last right node in the row.

        Args:
            x: The current x-position.
            y: The current y-position.

        Returns:
            The new x and y-position.
        """
        if x == 8:
            return 0, y + 1

        return x + 1, y

    def _step_back(self, x, y):
        """One step back.

        The algorithm recursively moves backwards until it finds a node
        which is not part of the initial solution.

        Args:
            x: The current x-position.
            y: The current y-position.

        Returns:
            The new x and y-position.
        """
        if x == 0:
            x = 8
            y -= 1

        else:
            x -= 1

        if self._node_matrix[y][x].initial:
            return self._step_back(x, y)

        return x, y

    def _backtrack(self, x, y, val):
        """The core of the backtracking algorithm.

        Recursively decrement the value of a node until a fitting value is placed.
        If no fitting value is found, the backtracking takes a step back and repeats the process.

        Args:
             x: The current x-position of the algorithm.
             y: The current y-position of the algorithm.
             val: The value which the function will attempt to place.

         Returns:
             The new position of where the latest fitting value was found.
             If the algorithm falls outside the bounds of the matrix, -1 and -1 is returned.
             This is to indicate that the algorithm failed to find a solution.
        """
        if val == 0:
            self._node_matrix[y][x].value = -1
            x, y = self._step_back(x, y)

            if y < 0:
                return -1, -1

            return self._backtrack(x, y, self._node_matrix[y][x].value - 1)

        if self._check_constraints(x, y, val):
            self._node_matrix[y][x].value = val
            return x, y

        return self._backtrack(x, y, val - 1)

    def _check_constraints(self, x, y, val):
        """Checks if a value fits the position.

        Args:
            x: The x-position which will be checked.
            y: The y-position which will be checked.
            val: The value which will be checked.
        """
        arr = []
        for i in range(len(self._node_matrix)):

            line = []
            for j in range(len(self._node_matrix[0])):
                if self._node_matrix[i][j].value == -1:
                    line.append(0)
                else:
                    line.append(self._node_matrix[i][j].value)

            arr.append(line)

        if self.king:
            if not king_constraint(arr, x, y, val):
                return False

        if self.knight:
            if not knight_constraint(arr, x, y, val):
                return False

        if not constraint_pass_inv(arr, x, y, val):
            return False

        return True
