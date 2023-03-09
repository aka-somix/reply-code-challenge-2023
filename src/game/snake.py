from cell import Cell, Wormhole
class Snake:
    starting_cell = list()
    moves = list()
    cells = list()

    def __init__(self, snake_length):
        self.snake_length = snake_length

    def set_starting_cell(self, col, row):
        self.starting_cell = (col, row)
        self.cells.append(self.starting_cell)

    def move_snake(self, direction, cell: Cell | Wormhole):
        if cell.wh:
            self.moves.append(direction)
            self.moves.append((cell.col, cell.row))
        else:
            self.moves.append(direction)
        self.cells.append(cell)
    
    def compute_score(self):
        return sum([c.value for c in self.cells])

    def __repr__(self):
        return str(self.snake_length)
