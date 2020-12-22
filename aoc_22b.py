fin = open('input_22.txt')

digits = '0123456789'
p = {1:[],2:[]}

for line in fin:
    if line[0] in digits:
        p[1].append(int(line.strip()))
    if line=='\n':
        break

for line in fin:
    if line[0] in digits:
        p[2].append(int(line.strip()))

fin.close()

print(p[1])
print(p[2])

recdepth = 0

def winner(p):
    global recdepth
    recdepth += 1
    print(recdepth,end=" ")
    hashes = set()
    while True:
        thishash = ('.'.join([str(x) for x in p[1]]),'.'.join([str(x) for x in p[2]]))
        if thishash in hashes:
            recdepth -= 1
            return 1,p
        else:
            hashes.add(thishash)
        c1 = p[1][0]
        p[1] = p[1][1:]
        c2 = p[2][0]
        p[2] = p[2][1:]
        if c1 > len(p[1]) or c2 > len(p[2]):
            if c1 > c2:
                p[1].extend([c1,c2])
            elif c2 > c1:
                p[2].extend([c2,c1])
        else:
            newdeck = {1:p[1][:c1],2:p[2][:c2]}
            if winner(newdeck)[0] == 1:
                p[1].extend([c1,c2])
            else:
                p[2].extend([c2,c1])
        if len(p[1])==0:
                recdepth -= 1
                return 2,p
        if len(p[2])==0:
                recdepth -= 1            
                return 1,p

w, deck = winner(p)
print('\nWinner:',w)
print('Player 1:', deck[1])
print('Player 2:', deck[2])

score = 0

for c,el in enumerate(deck[w]):
    score += (len(deck[w])-c)*el

print('Score:',score)
