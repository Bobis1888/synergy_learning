def calculate_result(number):

  units = number % 10
  tens = (number // 10) % 10
  hundreds = (number // 100) % 10
  thousands = (number // 1000) % 10
  ten_thousands = number // 10000

  result = tens**units * hundreds / (ten_thousands - thousands)

  return result

# test
# number = 46275
# result = calculate_result(number)
# print(result)

if __name__ == "__main__":
  while True:
    try:
      number = int(input("Введите пятизначное число: "))
      if not 10000 <= number <= 99999:
        raise ValueError
      break
    except ValueError:
      print("Ошибка: Введите пятизначное целое число.")

  result = calculate_result(number)
  print(f"Результат вычислений: {result}")