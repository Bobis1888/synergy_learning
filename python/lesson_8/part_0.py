def factorial(n):

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def factorial_list(num):
  result = []

  while num >= 1:
    result.append(factorial(num))
    num -= 1
  return result

number = int(input("Введите число: "))

result_list = factorial_list(number)

print(result_list)