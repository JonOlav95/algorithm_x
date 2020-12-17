from backtracking.backtrack_helpers import arr_to_node


class CSP:
    """Constraint Satisfaction Problem.

    Use CSP to partially (or potentially fully) solve the Sudoku board.

    Attributes:
        king: If the king constraint is enabled.
        knight: If the knight constraint is enabled.
        node_arr: A two-dimensional array of node objects.
    """
    def __init__(self, board, king, knight):
        self.king = king
        self.knight = knight
        self.node_arr = arr_to_node(board)

    def solve(self):
        """Narrow down the Sudoku board.

        This is the main function which attempts to solve the sudoku board. It may not
        solve any cells on the board, partially solve it, or fully solve it. Regardless of
        which it does, it will at the very least narrow down the options of each cell in the
        board by using constraints.
        The function repeats certain logic until it stagnates. If the total amount of potential
        values for every node in the board does not change after running the constraint functions,
        it is declared as stagnated and the function will return. If the total amount of values are
        81 this means that the function has reached a solution.

        Returns:
            A two-dimensional array of the node object with narrowed down values.
        """
        while True:

            values_before = self._total_values()

            for i in range(9):
                for j in range(9):

                    # Check the node for reduction
                    self._reduction(self.node_arr[i][j])

            values_after = self._total_values()

            if values_after == 81:
                self._update_values()
                return self.node_arr

            if values_before == values_after:
                self._update_values()
                return self.node_arr

    def _total_values(self):
        """Get the total amount of values in the node array."""
        values = 0

        for row in self.node_arr:
            for node in row:
                values += len(node.values)

        return values

    def _update_values(self):
        """Update the values of each node."""
        for row in self.node_arr:
            for node in row:
                node.update_val()

    def _reduction(self, node):
        """The main reduction function.

        Args:
            node: The node being checked for reduction.
        """

        # If there is only one potential value for the node set the node to that value
        # and remove that value from each node in the same domain (same row, same column, same box).
        if len(node.values) == 1:
            val = [node.values[0]]
            self._reduce(node, val)

        # If there is two potential values for the node, it may be a contender for the naked
        # twins function.
        if len(node.values) == 2:
            self._naked_twins(node)

        # Check for reduction within the king domain if king constraint is enabled.
        if self.king and len(node.values) == 1:
            self._king_reduce(node)

        # Check for reduction within the knight domain if knight constraint is enabled.
        if self.knight and len(node.values) == 1:
            self._knight_reduce(node)

    def _reduce(self, node, val, ign=None):
        """The standard reduction function for columns, rows, and squares.

        Args:
            node: The node which will reduce the values of the nodes within the same domains.
            val: The value which will be reduced.
            ign: The nodes that may be ignored when iterating through the node array.
        """
        if ign is None:
            ign = []

        if node not in ign:
            ign.append(node)

        x = node.x
        y = node.y

        for i in range(9):
            if self.node_arr[y][i] not in ign:
                for v in val:
                    self.node_arr[y][i].remove_value(v)

            if self.node_arr[i][x] not in ign:
                for v in val:
                    self.node_arr[i][x].remove_value(v)

        i = int(x / 3)
        j = int(y / 3)

        for n in range(3 * j, 3 * j + 3):
            for k in range(3 * i, 3 * i + 3):
                if self.node_arr[n][k] not in ign:
                    for v in val:
                        self.node_arr[n][k].remove_value(v)

    def _king_reduce(self, node):
        """Reduce the potential values of nodes according to the king constraint.

        The function arithmetically iterates through the neighbours and reduce their value.
        The function has to constantly take into account that the node may be at the edge of
        the board. Therefore, this functions contains a lot of if-statements to make sure
        only nodes within bounds are alternated.

        Args:
            node: The node which may reduce the potential value of its neighbours.
        """
        x = node.x
        y = node.y
        val = node.values[0]

        if x != 0:
            if y != 0:
                self.node_arr[y - 1][x - 1].remove_value(val)

            if y != 8:
                self.node_arr[y + 1][x - 1].remove_value(val)

            self.node_arr[y][x - 1].remove_value(val)

        if x != 8:
            if y != 0:
                self.node_arr[y - 1][x + 1].remove_value(val)

            if y != 8:
                self.node_arr[y + 1][x + 1].remove_value(val)

            self.node_arr[y][x + 1].remove_value(val)

        if y != 0:
            self.node_arr[y - 1][x].remove_value(val)

        if y != 8:
            self.node_arr[y + 1][x].remove_value(val)

    def _knight_reduce(self, node):
        """Reduce the potential values of nodes according to the knight constraint.

        This function is extremely similar to the _king_reduce function.

        Args:
            node: The node which will decrease the values of surrounding nodes.
        """
        x = node.x
        y = node.y
        val = node.values[0]

        if x != 0:
            if y > 1:
                self.node_arr[y - 2][x - 1].remove_value(val)

            if y < 7:
                self.node_arr[y + 2][x - 1].remove_value(val)

        if x != 8:
            if y > 1:
                self.node_arr[y - 2][x + 1].remove_value(val)

            if y < 7:
                self.node_arr[y + 2][x + 1].remove_value(val)

        if y != 0:
            if x > 1:
                self.node_arr[y - 1][x - 2].remove_value(val)

            if x < 7:
                self.node_arr[y - 1][x + 2].remove_value(val)

        if y != 8:
            if x > 1:
                self.node_arr[y + 1][x - 2].remove_value(val)

            if x < 7:
                self.node_arr[y + 1][x + 2].remove_value(val)


    def _naked_twins(self, node):
        """The naked twins function.

        The function checks all the standard Sudoku domains to see if there are any other
        nodes with the same two values. If there are then a proper function is applied
        with the two nodes as argument.

        Args:
            node: The node which will be checked for naked twins.
        """
        x = node.x
        y = node.y

        for i in range(9):

            if node != self.node_arr[y][i]:
                if set(node.values) == set(self.node_arr[y][i].values):
                    self._nt_row(node, self.node_arr[y][i])

            if node != self.node_arr[i][x]:
                if set(node.values) == set(self.node_arr[i][x].values):
                    self._nt_column(node, self.node_arr[i][x])

        i = int(x / 3)
        j = int(y / 3)

        for n in range(3 * j, 3 * j + 3):
            for k in range(3 * i, 3 * i + 3):
                if node != self.node_arr[n][k]:
                    if set(node.values) == set(self.node_arr[n][k].values):
                        self._nt_box(node, self.node_arr[n][k])

    def _nt_row(self, node_1, node_2,):
        """Two nodes in the same row have the two same values.

        The other nodes in the same row will have their values reduced by the
        two values the twin nodes holds.
        """
        row = node_1.y
        values = node_1.values

        for i in range(9):
            if node_1 == self.node_arr[row][i]:
                continue

            if node_2 == self.node_arr[row][i]:
                continue

            for val in values:
                self.node_arr[row][i].remove_value(val)

    def _nt_column(self, node_1, node_2):
        """Two nodes in the same column have the two same values.

        The other nodes in the same column will have their values reduced by the
        two values the twin nodes holds.
        """
        column = node_1.x
        values = node_1.values

        for i in range(9):
            if node_1 == self.node_arr[i][column]:
                continue

            if node_2 == self.node_arr[i][column]:
                continue

            for val in values:
                self.node_arr[i][column].remove_value(val)

    def _nt_box(self, node_1, node_2):
        """Two nodes in the same square have the two same values.

        The other nodes in the same square will have their values reduced by the
        two values the twin nodes holds.
        """
        x = node_1.x
        y = node_2.y
        values = node_1.values

        i = int(x / 3)
        j = int(y / 3)

        for n in range(3 * j, 3 * j + 3):
            for k in range(3 * i, 3 * i + 3):
                if self.node_arr[n][k] == node_1:
                    continue

                if self.node_arr[n][k] == node_2:
                    continue

                for val in values:
                    self.node_arr[n][k].remove_value(val)
