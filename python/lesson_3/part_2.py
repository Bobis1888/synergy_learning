def print_even_numbers(a, b):

  if a > b:
    print("Некорректный ввод: A должно быть меньше или равно B.")
    return

  for num in range(a, b + 1):
    if num % 2 == 0:
      print(num, end=' ')

a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))

print_even_numbers(a, b)