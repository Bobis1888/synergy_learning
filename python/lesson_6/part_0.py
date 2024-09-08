def count_unique(numbers):
  return len(set(numbers))

# зачем n?
n = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))

print(count_unique(numbers))