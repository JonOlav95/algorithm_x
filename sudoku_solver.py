from node import *
from node_matrix import NodeMatrix


class SudokuSolver:

    def __init__(self, matrix, sudoku_raw):

        # Note down the size of the sudoku board
        self._rows = len(matrix)
        self._columns = len(matrix[0])
        self._size = len(sudoku_raw)
        self._matrix = matrix
        self._solution = []

        if self._columns != 0:

            node_matrix = NodeMatrix(matrix, sudoku_raw)
            self._header, self._link_matrix = node_matrix.construct_matrix()

            self._initial_state(sudoku_raw)
            self._solve()

    # Sets the initial state of the sudoku board (the given numbers)
    def _initial_state(self, sudoku_raw):

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

                column_node = self._link_matrix[0][c]

                self._solution.append(node.y)

                self._cover(node)
                right_node = node.right

                while right_node != node:
                    self._cover(right_node)
                    right_node = right_node.right

            counter += self._size

    # Cover up a row and all connected rows and columns
    def _cover(self, node):
        column_node = self._link_matrix[0][node.x]

        column_node.left.right = column_node.right
        column_node.right.left = column_node.left

        row_node = column_node.down

        while row_node != column_node:

            right_node = row_node.right

            while right_node != row_node:
                right_node.up.down = right_node.down
                right_node.down.up = right_node.up

                self._link_matrix[0][right_node.x].node_amount -= 1

                if self._link_matrix[0][right_node.x].node_amount < 0:
                    print("Too little")

                right_node = right_node.right

            row_node = row_node.down

    # Uncover a row and all connected rows and columns
    def _uncover(self, node):
        column_node = self._link_matrix[0][node.x]

        row_node = column_node.up

        while row_node != column_node:

            left_node = row_node.left

            while left_node != row_node:
                left_node.up.down = left_node
                left_node.down.up = left_node

                self._link_matrix[0][left_node.x].node_amount += 1

                if self._link_matrix[0][left_node.x].node_amount < 0:
                    print("Too much")

                left_node = left_node.left

            row_node = row_node.up

        column_node.left.right = column_node
        column_node.right.left = column_node

    # Finds the column with the least amount of nodes connected to it
    def _find_minimum(self):
        node = self._header.right

        minimum = node.node_amount
        minimum_node = node

        while node != self._header:

            if node.node_amount < minimum:
                minimum_node = node
                minimum = node.node_amount

            node = node.right

        return minimum_node

    # The recursive main method used to solve sudoku
    def _solve(self):

        # If the linked list is empty, a solution has been found
        if self._header.right == self._header:
            print("A solution has been found")

            self._print_solution()
            return

        # Find the column with the least amount of nodes
        column_node = self._find_minimum()

        self._cover(column_node)

        row_node = column_node.down

        '''
        The loop browses down the column with the least amount of nodes and 
        adds the first row to the solution array. If the row does not fit it 
        is removed from the solution array, and the next row is added.
        '''
        while row_node != column_node:

            self._solution.append(row_node.y)
            right_node = row_node.right

            while right_node != row_node:
                self._cover(right_node)
                right_node = right_node.right

            self._solve()
            self._solution.pop()

            left_node = row_node.left

            while left_node != row_node:
                self._uncover(left_node)
                left_node = left_node.left

            row_node = row_node.down

        self._uncover(column_node)

    def _print_solution(self):

        subarray = []
        for n in range(self._size):
            subarray.append(n)

        counter = self._size
        for i in range(self._size * self._size):

            if counter == self._size:
                print("[", end="")
                counter = 0

            value = 0

            for k in range(len(subarray)):
                if subarray[k] in self._solution:
                    value = subarray[k] + 1
                    break

            if value != 0:
                value = int(value - self._size * i)

            counter += 1
            if counter == self._size:
                print(" " + str(value) + " ", end="")
                print("]")
            else:
                print(" " + str(value) + " ", end="")

            for j in range(self._size):
                subarray[j] += self._size
