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
        self.create_board(self.initial_board)

    def create_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.node_matrix[i][j].x = i
                self.node_matrix[i][j].y = j

                if board[i][j] != 0:
                    self.node_matrix[i][j].value = board[i][j]
                    self.node_matrix[i][j].initial = True

    def b_track(self):

        y = 0
        x = 0

        while y < 9:
            while x < 9 and y < 9:

                node = self.node_matrix[y][x]

                if node.initial:
                    x, y = self.step(x, y)
                    continue

                self.print_board()

                if node.value == -1:
                    x, y = self.tmp_name(x, y, 9)

                else:
                    x, y = self.tmp_name(x, y, node.value - 1)

                x, y = self.step(x, y)

        self.print_board()
        return self.solution_board()

    def step(self, x, y):

        if x == 8:
            return 0, y + 1

        return x + 1, y

    def tmp_name(self, x, y, val):

        if val == 0:
            self.node_matrix[y][x].value = -1
            x, y = self.back_tmp(x, y)
            return self.tmp_name(x, y, self.node_matrix[y][x].value - 1)

        if self.constraint(x, y, val):
            self.node_matrix[y][x].value = val
            return x, y

        return self.tmp_name(x, y, val - 1)

    def back_tmp(self, x, y):

        if x == 0:
            x = 8
            y -= 1

        else:
            x -= 1

        if self.node_matrix[y][x].initial:
            return self.back_tmp(x, y)

        return x, y

    def constraint(self, x, y, val):

        node = self.node_matrix[y][x]

        for i in range(9):

            if self.node_matrix[i][x] != node:
                if self.node_matrix[i][x].value == val:
                    return False

            if self.node_matrix[y][i] != node:
                if self.node_matrix[y][i].value == val:
                    return False

        if x < 3:
            sx_start = 0
            sx_end = 3
        elif x < 6:
            sx_start = 3
            sx_end = 6
        else:
            sx_start = 6
            sx_end = 9

        if y < 3:
            sy_start = 0
            sy_end = 3
        elif y < 6:
            sy_start = 3
            sy_end = 6
        else:
            sy_start = 6
            sy_end = 9

        for i in range(sy_start, sy_end):
            for j in range(sx_start, sx_end):
                if self.node_matrix[i][j] != node:
                    if self.node_matrix[i][j].value == val:
                        return False


        if x > 0:
            pass

        if x > 1:
            pass

        if x < 8:
            pass

        if x < 7:
            pass

        if y > 0:
            pass

        if y > 1:
            pass


        return True

    def print_board(self):
        for y in range(9):
            for x in range(9):
                node = self.node_matrix[y][x]
                val = 0

                if node.value != -1:
                    val = node.value

                print(str(val) + " ", end="")

            print("")

        print("")

    def solution_board(self):
        sol = []

        for y in range(9):

            row = []
            for x in range(9):
                row.append(self.node_matrix[y][x].value)

            sol.append(row)

        return sol
