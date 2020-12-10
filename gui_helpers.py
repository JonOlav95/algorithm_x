
def btn_to_arr(cells):
    arr = []
    for i in range(9):
        line = []
        for j in range(9):
            c = cells[i][j]

            if c.text() == "":
                line.append(0)
            else:
                line.append(int(c.text()))

        arr.append(line)

    return arr

