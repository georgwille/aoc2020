fin = open("input_02.txt")

myinput = fin.readlines()

valid_count = 0

for line in myinput:
    range_ , letter, pw = line.strip().split(' ')
    range_low, range_high = range_.split('-')
    letter = letter.split(':')[0]
    print(line, range_low, range_high, letter, pw)
    if int(range_low) <= pw.count(letter) <= int(range_high):
        valid_count += 1
        print("*")

print(valid_count)