class Cell:

    def __init__(self, row, col, value, nrows, ncols):
        self.row = row
        self.col = col
        self.nrows = nrows
        self.ncols = ncols
        self.value = value

    def up(self):
        r = (self.row + 1) % self.nrows
        c = self.col
        return [(r, c)]

    def down(self):
        r = (self.row + self.nrows - 1) % self.nrows
        c = self.col
        return [(r, c)]

    def right(self):
        r = self.row
        c = (self.col + 1) % self.ncols
        return [(r, c)]

    def left(self):
        r = self.row
        c = (self.col - 1 + self.ncols) % self.ncols
        return [(r, c)]

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Wormhole(Cell):

    def __init__(self, row, col, value, nrows, ncols):
        super().__init__(row, col, value, nrows, ncols)

        self.wh_list = []

    def set_wh_list(self, wh_list):
        self.wh_list = []
        for val in wh_list:
            self.wh_list.append(val)

    def up(self):
        r = (self.row + 1) % self.nrows
        c = self.col
        return [(r, c)]

    def down(self):
        r = (self.row + self.nrows - 1) % self.nrows
        c = self.col
        return [(r, c)]

    def right(self):
        r = self.row
        c = (self.col + 1) % self.ncols
        return [(r, c)]

    def left(self):
        r = self.row
        c = (self.col - 1 + self.ncols) % self.ncols
        return [(r, c)]

    def __str__(self):
        return "*"

    def __repr__(self):
        return "*"
