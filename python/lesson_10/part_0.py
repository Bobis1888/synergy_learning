def print_list_recursively(array_list):

  if not array_list:
    print("Конец списка")
    return

  print(array_list[0])

  print_list_recursively(array_list[1:])

array_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list_recursively(array_list)