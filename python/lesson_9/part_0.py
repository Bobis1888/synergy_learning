import random

def create_matrix(rows, cols):

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = random.randint(1, 100)

    return matrix


def sum_matrix(matrix1, matrix2, rows, cols):

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix1 = create_matrix(rows, cols)

print("Создана матрица 1:")

for row in matrix1:
    print(row)

matrix2 = create_matrix(rows, cols)

print("Создана матрица 2:")

for row in matrix2:
    print(row)

print("Результат сложения:")

result = sum_matrix(matrix1, matrix2, rows, cols)

for row in result:
  print(row)
