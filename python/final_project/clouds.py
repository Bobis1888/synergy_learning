from utils import rand_bool


class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update_clouds(self, r=2, mxr=20, g=1, mxg=20):

        for i in range(self.h):
            for j in range(self.w):
                if rand_bool(r, mxr):
                    self.cells[i][j] = 1
                    if rand_bool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {
            "cells": self.cells,
            "w": self.w,
            "h": self.h
        }

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
