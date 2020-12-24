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

dirs = ((-1,-1),(0,-2),(1,-1),(1,1),(0,2),(-1,1))

def neighbors_of(tile):
    global ftiles
    global dirs
    ncount = 0
    for dir_ in dirs:
        r,c = (tile[0]+dir_[0],tile[1]+dir_[1])
        if (r,c) in ftiles:
            ncount += 1
    return ncount

def tick():
    global ftiles
    global dirs
    newtiles = set()
    for tile in ftiles:
        # check on survival
        if neighbors_of(tile) in [1,2]:
            newtiles.add(tile)
        # check all *its* neighbors for new flips
        for dir_ in dirs:
            r,c = (tile[0]+dir_[0],tile[1]+dir_[1])
            if neighbors_of((r,c)) == 2:
                newtiles.add((r,c))
    ftiles = newtiles

tickcount = 100
print("Start with:",len(ftiles))

while tickcount:
    tickcount -= 1
    tick()
    print(len(ftiles))

