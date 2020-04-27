import numpy as np


def main():
    grid = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    solver(grid)


def isPossible(y, x, digit, grid):
    for i in range(0,9):
        if grid[y][i] == digit:
            return False
    for i in range(0,9):
        if grid[i][x] == digit:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == digit:
                return False
    return True

def solver(grid):
    m = len(grid)
    n = len(grid[0])

    for y in range(m):
        for x in range(n):
            if grid[y][x] == 0:
                for digit in range(1, 10):
                    if isPossible(y, x, digit, grid):
                        grid[y][x] = digit
                        solver(grid)
                        grid[y][x] = 0
                return # If no digit is possible it returns,
                       # because if it is completed, then the
                       # if grid == 0 condition will be false
                       # and will just end the 2 initial for loops.
    print(grid)
    input("More?")
    return

if __name__ == "__main__":
    main()
