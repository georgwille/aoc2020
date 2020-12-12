fin = open('input_12.txt')

p = 0+0j
o = 1+0j

offset = {'E':1+0j,'N':0+1j,'W':-1+0j,'S':0-1j}
rot = {'L':0+1j,'R':0-1j}

for line in fin:
    letter = line[0]
    number = int(line[1:-1])
    if letter in "ENWS":
        p += number*offset[letter]
    elif letter == "F":
        p += number*o
    elif letter in "RL":
        o *= rot[letter]**(number//90)

print(p,abs(p.real)+abs(p.imag))
