class Snake:
    starting_cell = list()
    moves = list()

    def __init__(self, snake_length):
        self.snake_length = snake_length

    def set_starting_cell(self, col, row):
        self.starting_cell = [col, row]

    def move_snake(self, direction, wormhole_coords=None):
        if wormhole_coords is not None:
            self.moves.apppend([direction, wormhole_coords])
        else:
            self.moves.append(direction)
