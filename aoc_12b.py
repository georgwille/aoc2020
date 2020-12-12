fin = open('input_12.txt')

p = 0+0j
w = 10+1j

offset = {'E':1+0j,'N':0+1j,'W':-1+0j,'S':0-1j}
rot = {'L':0+1j,'R':0-1j}

for line in fin:
    # print(p,o)
    line = line.strip()
    letter = line[0]
    number = int(line[1:])
    if letter in "ENWS":
        w += number*offset[letter]
    elif letter == "F":
        d = w-p
        p += number*d
        w += number*d
    elif letter in "RL":
        d = w-p
        d *= rot[letter]**(number//90)
        w = p+d

print(p,abs(p.real)+abs(p.imag))
