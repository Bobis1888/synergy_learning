import os

from clouds import Clouds
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
# 9 - облако ⛅
# 10 - молния ⚡
# 11 - кубок 🏆
# рамка ⬜

CELL_TYPES = "⬛🌲🌊🏥🏦🔥🚁⛅⚡"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 1000


class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(2, 10)
        self.generate_river(10)
        self.generate_river(15)
        self.generate_upgrade_shop()
        self.generate_hospital()
        self.clouds = Clouds(w, h)

    def print_map(self, helicopter):
        print('⬜' * (self.w + 2))
        for ri in range(self.h):
            print('⬜', end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]

                if self.clouds.cells[ri][ci] == 1:
                    print(CELL_TYPES[7], end="")
                elif self.clouds.cells[ri][ci] == 2:
                    print(CELL_TYPES[8], end="")
                elif helicopter.x == ri and helicopter.y == ci:
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

    def update_fires(self, helicopter):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    helicopter.score -= TREE_BONUS

        for i in range(10):
            self.add_fire()

    def generate_upgrade_shop(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = rand_cell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def process_helicopter(self, helicopter):
        hx = helicopter.x
        hy = helicopter.y

        c = self.cells[hx][hy]
        d = self.clouds.cells[hx][hy]

        if c == 2:
            helicopter.tank = helicopter.mx_tank
        if c == 5 and helicopter.tank > 0:
            helicopter.tank -= 1
            helicopter.score += TREE_BONUS
            self.cells[hx][hy] = 1
        if c == 4 and helicopter.score >= UPGRADE_COST:
            helicopter.mx_tank += 1
            helicopter.score -= UPGRADE_COST
        if c == 3 and helicopter.score >= LIFE_COST:
            helicopter.lives += 10
            helicopter.score -= LIFE_COST
        if d == 2:
            helicopter.lives -= 1
            if helicopter.lives == 0:
                os.system("clear")
                print("#" * 35)
                print("GAME OVER, YOUR SCORE IS", helicopter.score)
                print("#" * 35)
                exit(0)

    def export_data(self):
        return {
            "cells": self.cells,
            "w": self.w,
            "h": self.h,
            "clouds": self.clouds.export_data()
        }

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
        self.clouds.import_data(data["clouds"])
