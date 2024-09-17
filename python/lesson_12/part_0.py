class Kassa:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def top_up(self, amount):
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount


kass = Kassa(10000)
kass.top_up(1000)
kass.take_away(1000)
print(kass.count_1000())