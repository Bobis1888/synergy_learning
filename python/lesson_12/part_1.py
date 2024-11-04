class Cherepashka:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Черепашка не может двигаться медленнее")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        return (dx // self.s) + (dy // self.s)

cherepashka = Cherepashka(0, 0, 1)
cherepashka.evolve()
cherepashka.go_left()
cherepashka.go_left()
cherepashka.go_up()
cherepashka.go_up()

# скорость 1, сделали 4 шага из начальной точки
# ожидаемый результат 4 до начальной точки
print(cherepashka.count_moves(0, 0))

cherepashka.degrade()
try:
    cherepashka.degrade()
except ValueError:
    print("Черепашка не может двигаться медленнее")