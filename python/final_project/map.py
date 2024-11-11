# 0 - поле  ⬛
# 1 - дерево 🌲
# 2 - река 🌊
# 3 - госпиталь 🏥
# 4 - апгрейд-шоп 🏦
from final_project.utils import rand_bool, rand_cell, rand_cell2

# рамка ⬜

CELL_TYPES = "⬛🌲🌊🏥🏦"


class Map:

    def print_map(self):
        print('⬜' * (self.w + 2))
        for row in self.cells:
            print('⬜', end="")
            for cell in row:
                if 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
                else:
                    print(CELL_TYPES[0], end="")
            print('⬜')
        print('⬜' * (self.w + 2))

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def generate_river(self, l):
        rc = rand_cell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = rand_cell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if rand_bool(r, mxr):
                    self.cells[ri][ci] = 1

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(15, 10)
tmp.generate_forest(2, 10)
tmp.generate_river(10)
tmp.generate_river(15)
tmp.print_map()
