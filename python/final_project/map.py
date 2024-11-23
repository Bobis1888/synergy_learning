from utils import rand_bool, rand_cell, rand_cell2

# 0 - поле  ⬛
# 1 - дерево 🌲
# 2 - река 🌊
# 3 - госпиталь 🏥
# 4 - апгрейд-шоп 🏦
# 5 - огонь 🔥
# 6 - вертолет 🚁
# 7 - жизни 💚
# 8 - ведро 🪣
# 9 - облако ☁
# 10 - молния ⚡
# 11 - кубок 🏆
# рамка ⬜

CELL_TYPES = "⬛🌲🌊🏥🏦🔥🚁"


class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def print_map(self, helicopter):
        print('⬜' * (self.w + 2))
        for ri in range(self.h):
            print('⬜', end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]

                if helicopter.x == ri and helicopter.y == ci:
                    print(CELL_TYPES[6], end="")
                elif 0 <= cell < len(CELL_TYPES):
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

    def generate_tree(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]

        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if rand_bool(r, mxr):
                    self.cells[ri][ci] = 1

    def add_fire(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]

        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0

        for i in range(5):
            self.add_fire()
