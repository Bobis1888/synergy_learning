import math

def count_divisors(x):
  count = 0
  sqrt_x = int(math.sqrt(x))

  for i in range(1, sqrt_x + 1):
    if x % i == 0:
      count += 2

  if sqrt_x * sqrt_x == x:
    count -= 1

  return count

x = int(input("Введите натуральное число: "))

result = count_divisors(x)
print("Количество делителей числа", x, "равно", result)