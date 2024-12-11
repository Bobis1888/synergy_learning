from utils import rand_cell


class Helicopter:

    def __init__(self, w, h):
        rc = rand_cell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.mx_tank = 1
        self.tank = 0
        self.score = 0

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y

        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x = nx
            self.y = ny

    def print_stats(self):
        print("🪣 ", self.tank, "/", self.mx_tank, sep="", end=" | ")
        print("🏆", self.score)
