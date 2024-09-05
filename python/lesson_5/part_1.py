def shift(arr): return arr[-1:] + arr[:-1]

 # зачем N?
N = input("Введите число N: ")
print(*shift(input("Введите N чисел через пробел: ").split()))