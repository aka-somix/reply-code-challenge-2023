from game.cell import Cell, Wormhole


class Snake:

    def __init__(self, snake_length):
        self.snake_length = snake_length
        self.starting_cell = []
        self.moves = []
        self.cells = []

    def set_starting_cell(self, cell: Cell | Wormhole):
        self.starting_cell = (cell.col, cell.row)
        self.cells.append(cell)
        cell.free = False

    def move_snake(self, direction, cell: Cell | Wormhole):
        self.moves.append(direction)
        if cell.wh:
            self.moves.append((cell.col, cell.row))

        self.cells.append(cell)
        cell.free = False

    def compute_score(self):
        return sum([c.value for c in self.cells])

    def __repr__(self):
        return str(self.cells)
