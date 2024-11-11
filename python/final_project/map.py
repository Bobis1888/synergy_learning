# 0 - поле  ⬛
# 1 - дерево 🌲
# 2 - река 🌊
# 3 - госпиталь 🏥
# 4 - апгрейд-шоп 🏦

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
        if x< 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    # def generate_rivers(self):

    # def generate_forest(self):

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(20, 10)

tmp.cells[1][1] = 1
tmp.cells[2][2] = 2
tmp.cells[3][3] = 7

tmp.print_map()