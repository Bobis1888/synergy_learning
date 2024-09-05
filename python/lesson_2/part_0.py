def describe_number(number):

  if number == 0:
    return "нулевое число"
  elif number % 2 == 0:
    return "положительное четное число" if number > 0 else "отрицательное четное число"
  else:
    return "число не является четным"

if __name__ == "__main__":
  while True:
    try:
      number = int(input("Введите целое число: "))
      print(describe_number(number))
      break
    except ValueError:
      print("Ошибка: Введите целое число.")