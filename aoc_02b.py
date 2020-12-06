fin = open("input_02.txt")

myinput = fin.readlines()

valid_count = 0

for line in myinput:
    range_ , letter, pw = line.strip().split(' ')
    range_low, range_high = range_.split('-')
    letter = letter.split(':')[0]
    print(line, range_low, range_high, letter, pw)
    pos1 = (pw[int(range_low)-1] == letter)
    pos2 = (pw[int(range_high)-1] == letter)
    if pos1 + pos2 == 1:
        valid_count += 1
        print("*")

print(valid_count)