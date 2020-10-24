class Node:

    def __init__(self):
        self.value = -1
        self.x = -1
        self.y = -1
        self.initial = False


class Backtrack:

    def __init__(self, board):
        self.board = board
        self.initial_board = board
        self.node_matrix = [[Node() for i in range(len(board))] for j in range(len(board[0]))]


        self.solve(0, 0)

    def create_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.node_matrix[i][j].x = i
                self.node_matrix[i][j].y = j

                if board[i][j] != 0:
                    self.node_matrix[i][j].value = board[i][j]
                    self.node_matrix[i][j].initial = True


    def solve(self, x, y, forward):

        node = self.node_matrix[x][y]

        if node.initial:
            x, y = self.move(forward)
            self.solve(x, y, forward)
            return

        if forward:

            while True:

                if node.value == 9:
                    node.value = 0
                    x, y = self.move(False)
                    self.solve(x, y, False)
                node.value += 1

                if self.constraint(node):
                    x, y = self.move(forward)
                    self.solve(x, y, forward)













    def move(self, forward):
        return 0, 0


    def constraint(self, node):
        x = node.x
        y = node.y

        for j in range(9):

            if j != x:
                if self.node_matrix[j][y].value == node.value:
                    return False

            if j != y:
                if self.node_matrix[x][j].value == node.value:
                    return False

            

