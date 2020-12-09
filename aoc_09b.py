fin = open("input_09.txt")

lines = fin.readlines()

numbers = [int(element) for element in lines]

def ispossible(pool, number):
    for i,element in enumerate(pool):
        complement = number-element
        if complement in pool and pool.index(complement) != i:
            return True
    return False

for i,number in enumerate(numbers[25:],25):
    if not ispossible(numbers[i-25:i],number):
        print("Part A:",i,number)
        target = number
        break

for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if sum(numbers[i:j+1]) == target:
            print("Part B:",i,j,min(numbers[i:j+1])+max(numbers[i:j+1]))



