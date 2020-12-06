fin = open("input_01.txt")

myinput = fin.readlines()

mynumbers = [int(entry) for entry in myinput]

for number in mynumbers:
    if 2020-number in mynumbers:
        print(number*(2020-number))
