import xlrd
import xlsxwriter


"""This file is not part of the solution, functions are used to inspect the DL matrix in excel."""
def save_matrix(m):
    m = [[r[col] for r in m] for col in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                m[i][j] = ""

    workbook = xlsxwriter.Workbook("../arrays.xls")
    worksheet = workbook.add_worksheet()

    row = 0

    for col, data in enumerate(m):
        worksheet.write_column(row, col, data)

    workbook.close()


def read_xls():
    workbook = xlrd.open_workbook('../arrays.xls')
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
