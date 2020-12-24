# amazingly, this program ran
# without any error the first time

fin = open('input_24.txt')

def getdir(text):
    while text:
        direction = text[:2]
        if direction in ['nw','ne','sw','se']:
            text = text[2:]
            yield direction
        else:
            text = text[1:]
            yield direction[0]


ftiles = set() # (row,column)

# row, column
moves = {'nw':(-1,-1),'w':(0,-2),'sw':(1,-1),'se':(1,1),'e':(0,2),'ne':(-1,1)}

for line in fin:
    line = line.strip()
    r = c = 0
    for dir_ in getdir(line):
        r += moves[dir_][0]
        c += moves[dir_][1]
    if (r,c) in ftiles:
        ftiles.remove((r,c))
    else:
        ftiles.add((r,c))

fin.close()    

print("Black tiles:",len(ftiles))