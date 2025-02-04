from window import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

    def create_cells(self):
        self.cells = []
        for col in range(self.num_cols):
            self.cells.append(col)
            for row in range(self.num_rows):
                self.cells.append(row)

    def draw_cell(self, i, j):
        pass