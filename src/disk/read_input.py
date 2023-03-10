from game.cell import Cell
from game.cell import Wormhole
from game.snake import Snake


def read_input(filename):
    with open(filename, 'r') as file:
        # read the first line of the file to get the number of columns and rows
        num_cols, num_rows, num_snakes = map(int, file.readline().strip().split())

        snakes = [Snake(s) for s in map(int, file.readline().strip().split())]

        # create a 2D array to store the cells
        cells: list(list(Cell | Wormhole)) = [[None for _ in range(num_cols)] for _ in range(num_rows)]

        wormholes_pos = []

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
                    wormholes_pos.append((row, col))
    print('read matrix')
    for wh in wormholes_pos:
        cells[wh[0]][wh[1]].set_wh_list(wormholes_pos)
    print('set wormholes')

    return cells, snakes
