fin = open("input_03.txt")

myinput = fin.readlines()

xlen = len(myinput[0])-1

treecounter = 0
posx = 0
posy = 0

while posy < len(myinput):
    # print(myinput[posy][posx])
    if myinput[posy][posx] == "#":
        treecounter += 1
    posy += 1
    posx += 3
    posx = posx % xlen

print(treecounter)
