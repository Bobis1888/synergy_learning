def check_duplicates(sequence):
    seen = set()
    for num in sequence:
        if num in seen:
            print(f"{num} - YES")
        else:
            seen.add(num)
            print(f"{num} - NO")


numbers = list(map(int, input("Введите последовательность через пробел: ").split()))
check_duplicates(numbers)