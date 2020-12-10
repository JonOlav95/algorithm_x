import numpy as np


def constraint_pass(arr):

    for i in range(9):
        for j in range(9):
            cell = arr[i][j]

            if cell == 0:
                continue

            for k in range(j + 1, 9):
                row_cell = arr[i][k]

                if row_cell == cell:
                    return False

            for k in range(i + 1, 9):
                column_cell = arr[k][j]

                if column_cell == cell:
                    return False

    return True


def knight_constraint(arr, x, y, val):

    if x != 0:
        if y > 1:
            if val == arr[y - 2][x - 1]:
                return False

        if y < 7:
            if val == arr[y + 2][x - 1]:
                return False

    if x != 8:
        if y > 1:
            if val == arr[y - 2][x + 1]:
                return False

        if y < 7:
            if val == arr[y + 2][x + 1]:
                return False

    if y != 0:
        if x > 1:
            if val == arr[y - 1][x - 2]:
                return False

        if x < 7:
            if val == arr[y - 1][x + 2]:
                return False
    if y != 8:
        if x > 1:
            if val == arr[y + 1][x - 2]:
                return False

        if x < 7:
            if val == arr[y + 1][x + 2]:
                return False

    return True


def king_constraint(arr, x, y, val):

    pad_arr = np.pad(arr, [(1, 1), (1, 1)], mode="constant", constant_values=0)

    x += 1
    y += 1

    for i in range(-1, 2):
        if pad_arr[y - 1][x + i] == val:
            return False

        if pad_arr[y + 1][x + i] == val:
            return False

    if pad_arr[y][x + 1] == val:
        return False

    if pad_arr[y][x - 1] == val:
        return False

    return True


def constraint_pass_inv(arr, x, y, val):

    for i in range(9):
        if i != x:
            row_cell = arr[y][i]
            if row_cell == val:
                return False

        if i != y:
            column_cell = arr[i][x]
            if column_cell == val:
                return False

    i = int(x / 3)
    j = int(y / 3)

    for n in range(3 * j, 3 * j + 3):
        for k in range(3 * i, 3 * i + 3):
            if n != y and k != x and arr[n][k] == val:
                return False

    return True


def check_board(arr, king, knight):
    for i in range(9):
        for j in range(9):

            if arr[i][j] == 0:
                continue

            if not constraint_pass_inv(arr, j, i, arr[i][j]):
                print("regular constraint at x: " + str(j) + ", y: " + str(i))
                return False
            if king and not king_constraint(arr, j, i, arr[i][j]):
                print("king constraint at x: " + str(j) + ", y: " + str(i))
                return False
            if knight and not knight_constraint(arr, j, i, arr[i][j]):
                print("knight constraint at x: " + str(j) + ", y: " + str(i))
                return False

    return True
