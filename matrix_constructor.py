import math
import pandas as pd
import xlrd

import xlsxwriter


def construct_sudoku(size):
    king = True

    down_left = []
    down_right = []
    for i in range(size - 1):
        down_right.append([i, 2])
        down_right.append([i, 5])

        down_left.append([i, 3])
        down_left.append([i, 6])

        if i != 2 and i != 5:
            down_right.append([2, i])
            down_right.append([5, i])

            down_left.append([2, i + 1])
            down_left.append([5, i + 1])



    king_len = (len(down_left) * size) + (len(down_right) * size)
    total_rows = size * size * size

    if king:
        total_columns = size * size * 4 + king_len
    else:
        total_columns = size * size * 4

    total_nodes = size * size


    matrix = [[0 for i in range(total_columns)] for j in range(total_rows)]

    ''' matrix[ROW][COL]'''

    multiplier = 0

    for col in range(total_nodes):
        for row in range(multiplier * size, multiplier * size + size):
            matrix[row][col] = 1

        multiplier += 1

    multiplier = 0

    for x in range(0, size):
        for y in range(x * total_nodes, x * total_nodes + total_nodes, size):
            for n in range(0, size):
                r = y + n
                c = x * size + total_nodes + n
                matrix[r][c] = 1

    tmp = 0
    for col in range(0, total_nodes):
        for row in range(size):
            matrix[row * total_nodes + tmp][col + total_nodes * 2] = 1

        tmp += 1

    counter_3 = 0
    counter_4 = 0
    total_columns_old = size * size * 4
    for i in range(0, size):
        counter = 0

        if i % int(math.sqrt(size)) == 0 and i != 0:

            counter_3 += size * size * int(math.sqrt(size))
            counter_2 = 0
            counter = 0
            counter_4 = 1

        else:
            counter_2 = (counter_4 * int(math.sqrt(size) * size))
            counter_4 += 1

        for j in range(0, size):

            if j % int(math.sqrt(size)) == 0 and j != 0:
                counter += size * (size - int(math.sqrt(size)))

            for k in range(0, size):
                q = k + j * size + counter + counter_2 + counter_3
                w = k + (i * size) + (total_columns_old - (size * size))

                matrix[q][w] = 1

    # KING CONSTRAINT
    if king:
        col_tmp = size * size * 4

        for i in range(size - 1):
            for j in range(size - 1):

                if [i, j] in down_right:
                    for k in range(size):
                        row = k + (j * size) + (i * size * size)

                        matrix[row][col_tmp + k] = 1
                        matrix[row + (size * size) + size][col_tmp + k] = 1
                    col_tmp += size

                if [i, j] in down_left:
                    for k in range(size):
                        row = k + (j * size) + (i * size * size)

                        matrix[row][col_tmp + k] = 1
                        matrix[row + (size * size) - size][col_tmp + k] = 1
                    col_tmp += size

    #save_matrix(matrix)

    return matrix


def save_matrix(m):
    m = [[r[col] for r in m] for col in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                m[i][j] = ""

    workbook = xlsxwriter.Workbook("arrays.xls")
    worksheet = workbook.add_worksheet()

    row = 0

    for col, data in enumerate(m):
        worksheet.write_column(row, col, data)

    workbook.close()


def read_xls():
    workbook = xlrd.open_workbook('arrays.xls')
    # worksheet = workbook.sheet_by_name("Sheet1")
    worksheet = workbook.sheet_by_index(0)

    rows = worksheet.nrows
    cols = worksheet.ncols

    matrix = [[0 for x in range(cols)] for y in range(rows)]

    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            if worksheet.cell(i, j).value != "":
                matrix[i][j] = 1

    return matrix
