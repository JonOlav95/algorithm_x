
class Node:

    def __init__(self):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.x = -1
        self.y = -1
        self.covered = False


class ColumnNode(Node):

    def __init__(self):
        super().__init__()
        self.node_amount = 0


class HeaderNode(Node):

    def __init__(self):
        super().__init__()
