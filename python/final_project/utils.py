from random import randrange as rand


def rand_bool(r, mxr):
    t = rand(0, mxr)
    return t <= r


def rand_cell(w, h):
    tw = rand(0, w)
    th = rand(0, h)
    return th, tw

# 0 - верх, 1 - право, 2 - низ, 3 - лево


def rand_cell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return x + dx, y + dy