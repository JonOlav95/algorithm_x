
class Node:
    """A dancing link node used to solve Sudoku with exact cover.

    The class has similar structure to a linked list.

    Attributes:
        up: The node above which this node points to.
        down: The node below which this node points to.
        left: The node to the left which this node points to.
        right: The node to the right which this node points to.
        x: The x-position of the node.
        y: The y-position of the node.
        covered: If the node is covered or not during algorithm x.
    """
    def __init__(self):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.x = -1
        self.y = -1
        self.covered = False


class ColumnNode(Node):
    """Inherits from the regular Node.

    Attributes:
        node_amount: Keeps track of the total vertical connected nodes on the column.
    """
    def __init__(self):
        super().__init__()
        self.node_amount = 0


class HeaderNode(Node):
    """Dummy header node.

    Has no unique qualities and is mostly used for easier debugging.
    """
    def __init__(self):
        super().__init__()
