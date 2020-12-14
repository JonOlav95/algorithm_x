from boards.pick_board import pick_board


class Node:

    def __init__(self):

        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.x = -1
        self.y = -1

    def set_value(self, val):
        self.values.clear()
        self.values.append(val)

    def remove_value(self, val):
        if val in self.values:
            self.values.remove(val)


def arr_to_node(arr):

    node_arr = [[Node() for i in range(len(arr))] for j in range(len(arr[0]))]

    for i in range(9):
        for j in range(9):

            node = Node()
            node.x = j
            node.y = i

            if arr[i][j] != 0:
                node.set_value(arr[i][j])

            node_arr[i][j] = node

    return node_arr


def print_board(matrix):
    for y in range(9):
        for x in range(9):
            node = matrix[y][x]
            val = 0

            if len(node.values) == 1:
                val = node.values[0]

            print(str(val) + " ", end="")

        print("")
    print("")


class CPS:

    def __init__(self):

        self.king = True

        board = pick_board(self.king, knight=False)
        self.node_arr = arr_to_node(board)

    def solve(self):

        while True:
            values_before = 0

            for i in range(9):
                for j in range(9):
                    values_before += len(self.node_arr[i][j].values)

            for i in range(9):
                for j in range(9):
                    self.reduction(self.node_arr[i][j])
                    self.is_zero()
                    if self.king:
                        self.king_reduce(self.node_arr[i][j])

            values_after = 0

            for i in range(9):
                for j in range(9):
                    values_after += len(self.node_arr[i][j].values)

            print_board(self.node_arr)

            if values_after == 81:
                print("found sol")
                break

            if values_before == values_after:
                print("failed")
                break

    def is_zero(self):
        for i in range(9):
            for j in range(9):
                if len(self.node_arr[i][j].values) == 0:
                    print("ZEERO")
                    return

    def reduction(self, node):

        if len(node.values) == 1:
            val = [node.values[0]]
            self.reduce(node, val)

        if len(node.values) == 2:
            self.naked_twins(node)

    def reduce(self, node, val, ign=None):

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

    def king_reduce(self, node):

        if len(node.values) != 1:
            return

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

    def naked_twins(self, node):

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


cps = CPS()
cps.solve()

