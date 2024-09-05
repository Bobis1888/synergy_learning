from random import random


def investment_scenario(michael_funds, ivan_funds, min_investment):

  if michael_funds >= min_investment and ivan_funds >= min_investment:
    return "2"  # Оба могут инвестировать
  elif michael_funds >= min_investment:
    return "Mike"  # Только Майкл может инвестировать
  elif ivan_funds >= min_investment:
    return "Ivan"  # Только Иван может инвестировать
  elif michael_funds + ivan_funds >= min_investment:
    return "1"  # Вместе могут инвестировать
  else:
    return "0"  # Никто не может инвестировать

for i in range(5):

  min_required = round(random() * 10000)
  print(f"Минимальная сумма инвестиции: {min_required}")

  michael_money = round(random() * 10000)
  print(f"Бюджет Майкла: {michael_money}")

  ivan_money = round(random() * 10000)
  print(f"Бюджет Ивана: {ivan_money}")

  result = investment_scenario(michael_money, ivan_money, min_required)
  print(result)
