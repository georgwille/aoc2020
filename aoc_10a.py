fin = open("input_10_test.txt")

numbers = [int(line) for line in fin]

numbers.append(0)
numbers.append(max(numbers)+3)

fin.close()

numbers.sort()

count1 = 0
count3 = 0

for i,number in enumerate(numbers[:-1]):
    diff = numbers[i+1]-number
    if diff == 3:
        count3 += 1
    elif diff == 1:
        count1 += 1

print(count1, count3, count1*count3)