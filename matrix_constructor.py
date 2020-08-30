import math
import xlsxwriter


def construct_sudoku(size):
    total_rows = size * size * size
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
                w = k + (i * size) + (total_columns - (size * size))

                matrix[q][w] = 1

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