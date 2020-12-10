from constraint import *


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

        self.knight = False
        self.king = False

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

        arr = []
        for i in range(len(self.node_matrix)):

            line = []
            for j in range(len(self.node_matrix[0])):
                if self.node_matrix[i][j].value == -1:
                    line.append(0)
                else:
                    line.append(self.node_matrix[i][j].value)

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
