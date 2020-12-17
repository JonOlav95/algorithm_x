import time
import matplotlib.pyplot as plt

from backtracking.backtrack import Backtrack
from exact_cover.algorithmx import AlgorithmX

puzzles = []
puzzle = []
with open("puzzles.txt", mode="r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("Grid"):
            if puzzle:
                puzzles.append(puzzle)
                puzzle = []

        else:

            row = []
            for num in line:
                row.append(int(num))

            puzzle.append(row)


s = AlgorithmX()

algx_time = []
for p in puzzles:
    start = time.time()
    s.solve(p)

    end = time.time()
    t_time = round(((end - start) * 1000), 2)
    algx_time.append(t_time)


plt.plot(algx_time)
plt.ylabel("Time in MS")
plt.show()

backtrack_time = []
for p in puzzles:
    start = time.time()

    bc = Backtrack(p)
    bc.solve()

    end = time.time()
    t_time = round(((end - start) * 1000), 2)
    backtrack_time.append(t_time)

plt.plot(backtrack_time)
plt.ylabel("Time in MS")
plt.show()
