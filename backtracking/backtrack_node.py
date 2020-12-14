class Node:
    """One node used to represent a cell on the Sudoku board.

    This node is tailored for working with backtracking and constraint propagation.
    The node has the potential values from 1-9, we will then apply constraint propagation
    which will reduce the domain of the values for many nodes. Afterwards we will apply
    backtracking, which will only try to potential values, and not all values (1-9).

    Attributes:
        value: The value of the node, -1 indicates a value is not set.
        values: The potential values the node can have, initially is 1-9, but this domain
        will decrease after CPS has adjusted the nodes.
        index: The index used to indicate which of the values the node is currently pointing to
        when working with the backtracking algorithm.
        x: The x-position of the node.
        y: The y-position of the node.
    """
    def __init__(self):
        self.value = -1
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.index = -1
        self.x = -1
        self.y = -1

    def set_value(self, val):
        self.values.clear()
        self.values.append(val)

    def remove_value(self, val):
        if val in self.values:
            self.values.remove(val)

    def update_val(self):
        """Update the value of a node when done with CPS.

        Sets the index of the node to the last possible index. If there is only
        one value, the value attribute is set to that value.
        """
        self.index = len(self.values) - 1

        if len(self.values) == 1:
            self.value = self.values[0]

    def is_initial(self):
        """Checks if the node is part of the initial solution"""
        if len(self.values) == 1:
            return True

        return False

    def reset_node(self):
        self.value = -1
        self.index = len(self.values) - 1

