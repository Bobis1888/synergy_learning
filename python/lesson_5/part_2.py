def min_boats(weights, max_weight):
    weights.sort()
    count = 0
    i = 0
    j = len(weights) - 1

    while i <= j:
        if weights[i] + weights[j] <= max_weight:
            i += 1
            j -= 1
        else:
            j -= 1
        count += 1

    return count

max_weight = int(input("Введите максимальный вес: "))
n = int(input("Введите количество пассажиров: "))
weights = [int(input("Введите вес: ")) for _ in range(n)]

result = min_boats(weights, max_weight)
print(result)