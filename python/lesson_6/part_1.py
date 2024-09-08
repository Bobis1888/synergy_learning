def find_elements(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  common_elements = set1.intersection(set2)
  return len(common_elements)

n1 = int(input("Введите количество чисел в первом списке: "))
list1 = []

while n1 > 0:
    n1 -= 1
    list1.append(int(input("Введите следующее число: ")))

n2 = int(input("Введите количество чисел во втором списке: "))
list2 = []

while n2 > 0:
    n2 -= 1
    list2.append(int(input("Введите следующее число: ")))

result = find_elements(list1, list2)

print(result)
