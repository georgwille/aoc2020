fin = open("input_09.txt")

lines = fin.readlines()

numbers = [int(element) for element in lines]


def ispossible(pool, number):
    for i, element in enumerate(pool):
        complement = number - element
        if complement in pool and pool.index(complement) != i:
            return True
    return False


for i, number in enumerate(numbers[25:], 25):
    if not ispossible(numbers[i - 25:i], number):
        print("Part A:", i, number)
        target = number
        break

cumsum = [0]
for i, number in enumerate(numbers):
    cumsum.append(cumsum[i] + number)


def fastsum(i, j):
    if i > j:
        i, j = j, i
    return cumsum[j + 1] - cumsum[i]


for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if fastsum(i, j) == target:
            print("Part B:", i, j, min(
                numbers[i:j + 1]) + max(numbers[i:j + 1]))
