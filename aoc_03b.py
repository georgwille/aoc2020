fin = open("input_03.txt")

myinput = fin.readlines()

valid_count = 0

steps =[(1,1),(3,1),(5,1),(7,1),(1,2)]

xlen = len(myinput[0])-1
product = 1

for stepx, stepy in steps:
    print(stepx, stepy)
    treecounter = 0
    posx = 0
    posy = 0

    while posy < len(myinput):
        # print(myinput[posy][posx])
        if myinput[posy][posx] == "#":
            treecounter += 1
        posy += stepy
        posx += stepx
        posx %= xlen

    print(treecounter)
    product *= treecounter

print(product)