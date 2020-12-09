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
        print(i,number)

