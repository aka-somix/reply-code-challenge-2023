import sys

sys.path.append('..')

from game import Cell

def read_input(filename):
    with open(filename, 'r') as file:
        # read the first line of the file to get the number of columns and rows
        num_cols, num_rows = map(int, file.readline().strip().split())

        # create a 2D array to store the cells
        cells = [[None for _ in range(num_cols)] for _ in range(num_rows)]

        # read the rest of the lines to fill in the cells
        for row in range(num_rows):
            line = file.readline().strip().split()
            for col in range(num_cols):
                value = int(line[col])
                cells[row][col] = Cell(row, col, value)

    return cells