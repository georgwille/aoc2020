numbers = [0, 1, 4, 13, 15, 12, 16]
# numbers = [0,3,6]
consider = len(numbers) - 1
counter = 0
target = 2020
# target = 30000000
max = target + 1

while True:
    if numbers[-1] not in numbers[:-1]:
        new = 0
    else:
        new = numbers[-2::-1].index(numbers[-1]) + 1
    numbers.append(new)
    # print(counter, numbers)
    counter += 1
    if counter == max:
        break
    if not counter % 10000:
        print(counter)

print(target, numbers[target - 1])
