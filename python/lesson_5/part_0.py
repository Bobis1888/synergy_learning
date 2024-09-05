N = int(input("Введите количество чисел: "))
numbers = []

for _ in range(N):
    numbers.append(int(input("Введите число: ")))

numbers.reverse()

for num in numbers:
    print(num)