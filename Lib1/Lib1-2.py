def find_numbers():
    result = []
    for num in range(1, 1000):
        if num % 13 == 0 or str(num).startswith('13'):
            result.append(num)
    print("符合条件的数字:", result)
    print("总数:", len(result))

find_numbers()