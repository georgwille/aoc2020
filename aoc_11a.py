import copy

fin = open('input_11.txt')

boat = []

for line in fin:
    line = ' '+line.strip()+' '
    boat.append(list(line))

fin.close()

l = len(boat[0])
emptyrow = list(' '*l)

boat.insert(0,emptyrow)
boat.append(emptyrow)

def iterate():
    global boat
    newboat = copy.deepcopy(boat)
    rnum = len(boat)-2
    cnum = len(boat[0])-2
    occ = 0
    for r in range(1,rnum+1):
        for c in range(1,cnum+1):
            n = neighborcount(r,c)
            if n == 0 and boat[r][c]=="L":
                newboat[r][c]='#'
            elif n >= 4 and boat[r][c]=="#":
                newboat[r][c]="L"
        occ += newboat[r].count('#')
    boat = newboat
    return occ

def neighborcount(r,c):
    global boat
    n = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr==0 and dc==0:
                continue
            n += (boat[r+dr][c+dc] == '#')
    return n

def printboat():
    global boat
    for line in boat:
        for char in line:
            print(char,end="")
        print()
    print()

printboat()

for i in range(100):
    occseats = iterate()
    # printboat()
    print(occseats)

