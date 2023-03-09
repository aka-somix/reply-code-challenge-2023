from typing import Union, Tuple
from game.cell import Cell
from game.cell import Wormhole


def read_input(filename):
    with open(filename, 'r') as file:
        # read the first line of the file to get the number of columns and rows
        num_cols, num_rows, num_snakes = map(int, file.readline().strip().split())

        snakes = map(int, file.readline().strip().split())

        # create a 2D array to store the cells
        cells = [[None for _ in range(num_cols)] for _ in range(num_rows)]

        wormholes = []

        # read the rest of the lines to fill in the cells
        for row in range(num_rows):
            line = file.readline().strip().split()
            for col in range(num_cols):
                try:
                    value = int(line[col])
                    cells[row][col] = Cell(row, col, value, num_rows, num_cols)
                except:
                    value = 0
                    cells[row][col] = Wormhole(row, col, value, num_rows, num_cols)
                    wormholes.append((row, col))

    return cells, snakes
