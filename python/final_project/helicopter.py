from utils import rand_cell

class Helicopter:

    def __init__(self, w, h):
        rc = rand_cell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry