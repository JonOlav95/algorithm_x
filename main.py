import time
from matrix_constructor import construct_sudoku
from sudoku_solver import SudokuSolver


"""
Sudoku solver using Knuth's Algorithm X

Useful sources: 
https://en.wikipedia.org/wiki/Exact_cover
https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
https://www.geeksforgeeks.org/exact-cover-problem-algorithm-x-set-2-implementation-dlx/
https://medium.com/javarevisited/building-a-sudoku-solver-in-java-with-dancing-links-180274b0b6c1
https://www.kevinhooke.com/2019/01/22/revisiting-donald-knuths-algorithm-x-and-dancing-links-to-solve-sudoku-puzzles/
"""


if __name__ == '__main__':

    sudoku_small = [[3, 4, 1, 0],
                    [0, 2, 0, 0],
                    [0, 0, 2, 0],
                    [0, 1, 4, 3]]

    sudoku_small_2 = [[0, 0, 0, 0],
                      [1, 0, 2, 0],
                      [0, 4, 0, 3],
                      [0, 0, 0, 0]]

    sudoku_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku_medium_2 = [[9, 0, 3, 0, 0, 0, 0, 0, 8],
                       [0, 6, 0, 0, 0, 0, 0, 1, 0],
                       [0, 5, 0, 2, 0, 0, 0, 9, 0],
                       [0, 0, 0, 1, 6, 4, 5, 0, 2],
                       [0, 0, 0, 0, 3, 0, 0, 0, 0],
                       [6, 0, 1, 5, 8, 7, 0, 0, 0],
                       [0, 4, 0, 0, 0, 6, 0, 8, 0],
                       [0, 8, 0, 0, 0, 0, 0, 2, 0],
                       [2, 0, 0, 0, 0, 0, 3, 0, 7]]

    sudoku_medium_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 3, 0, 8, 5],
                       [0, 0, 1, 0, 2, 0, 0, 0, 0],
                       [0, 0, 0, 5, 0, 7, 0, 0, 0],
                       [0, 0, 4, 0, 0, 0, 1, 0, 0],
                       [0, 9, 0, 0, 0, 0, 0, 0, 0],
                       [5, 0, 0, 0, 0, 0, 0, 7, 3],
                       [0, 0, 2, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 4, 0, 0, 0, 9]]

    sudoku_large = [[8, 0, 9, 0, 10, 0, 0, 12, 16, 0, 15, 0, 0, 0, 0, 4],
                    [0, 0, 15, 0, 0, 0, 5, 0, 0, 7, 0, 10, 0, 0, 13, 0],
                    [2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 16, 0, 14],
                    [0, 6, 0, 3, 0, 0, 14, 0, 0, 0, 11, 0, 9, 0, 0, 0],
                    [0, 0, 0, 0, 0, 9, 0, 0, 1, 0, 0, 2, 0, 0, 0, 7],
                    [11, 0, 0, 0, 14, 0, 0, 6, 0, 0, 0, 0, 0, 13, 0, 0],
                    [0, 7, 0, 16, 0, 2, 0, 0, 12, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 5, 8, 0, 0, 13, 0, 3, 0, 0, 0, 0, 0, 9],
                    [12, 0, 4, 0, 0, 0, 7, 0, 13, 0, 8, 0, 11, 0, 0, 0],
                    [0, 5, 0, 8, 0, 13, 0, 10, 0, 16, 0, 4, 0, 0, 0, 0],
                    [0, 0, 14, 0, 0, 0, 9, 0, 6, 0, 0, 11, 0, 1, 0, 3],
                    [1, 0, 0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 6, 0, 16, 0],
                    [14, 0, 7, 0, 0, 0, 10, 0, 0, 12, 0, 9, 0, 8, 2, 0],
                    [0, 16, 0, 12, 0, 14, 0, 3, 0, 0, 0, 0, 13, 0, 0, 11],
                    [5, 10, 0, 0, 6, 0, 11, 0, 0, 0, 14, 0, 0, 7, 0, 0],
                    [15, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 5, 0, 0, 0, 12]]

    board = construct_sudoku(size=9)
    start = time.time()
    s = SudokuSolver(board, sudoku_medium_2)

    end = time.time()
    t_time = round(((end - start) * 1000), 2)
    print("TIME(ms): " + str(t_time))
