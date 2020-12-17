def exact_to_arr(size, solution):
    """Parse the dancing links matrix to a matrix of integers after solving.

    Args:
        size: The size of the puzzle.
        solution: The rows which are part of the solution.

    Returns:
        A matrix of integers which shows the solution of the puzzle. Returns an empty
        list if no solution was found.
    """
    if not solution:
        return []

    arr = []
    row = []
    subarray = []

    for n in range(size):
        subarray.append(n)

    counter = 0
    for i in range(size * size):

        value = 0

        for k in range(len(subarray)):
            if subarray[k] in solution:
                value = subarray[k] + 1
                break

        if value != 0:
            value = int(value - size * i)

        counter += 1
        row.append(value)

        for j in range(size):
            subarray[j] += size

        if counter == size:
            counter = 0
            arr.append(row)
            row = []

    return arr


def print_solution(size, solution):
    """Used to print the solution, good for debugging."""
    subarray = []
    for n in range(size):
        subarray.append(n)

    counter = size
    for i in range(size * size):

        if counter == size:
            print("[", end="")
            counter = 0

        value = 0

        for k in range(len(subarray)):
            if subarray[k] in solution:
                value = subarray[k] + 1
                break

        if value != 0:
            value = int(value - size * i)

        counter += 1
        if counter == size:
            print(" " + str(value) + " ", end="")
            print("]")
        else:
            print(" " + str(value) + " ", end="")

        for j in range(size):
            subarray[j] += size
