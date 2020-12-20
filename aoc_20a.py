import numpy as np

fin = open('input_20.txt')
lines = fin.readlines()
fin.close()

tiles={} # ndarrays with the tile data
borders = {} # two lists with four numbers each for each tile
tile_with_border = {} # for each border-id a list of tiles with this id

def getnumber(row):
    bits = '0b'
    for i in row:
        bits += str(i)
    return int(bits,base=2)

def getborders(arr):
    thisarr = arr.copy()
    list1 = []
    list2 = []
    for i in range(4):
        toprow = thisarr[0]
        worpot = toprow[::-1]
        list1.append(getnumber(toprow))
        list2.append(getnumber(worpot))
        thisarr = np.rot90(thisarr)
    return list1,list2

for lc,line in enumerate(lines):
    if line.startswith('Tile'):
        thistile = np.zeros((10,10),dtype='int8')
        tile_id=int(line[5:9])
        for i in range(1,11):
            tline = lines[lc+i]
            for c,char in enumerate(tline):
                if char == '#':
                    thistile[i-1,c]=1
        tiles[tile_id]=thistile
        print(thistile)
        borders[tile_id]=getborders(thistile)
        print(borders[tile_id])
        for orientation in borders[tile_id]:
            for element in orientation:
                try:
                    tile_with_border[element].append(tile_id)
                except KeyError:
                    tile_with_border[element] = [tile_id]

edgetiles = set()
edgeborders = set()

for border in tile_with_border:
    tiles = tile_with_border[border]
    if len(tiles) ==1:
        edgetiles.add(tiles[0])
        edgeborders.add(border)

print(edgetiles)
print(edgeborders)

for tile in borders:
    b = borders[tile]
    cornercount = 0
    for orientation in b:
        for bid in orientation:
            if bid in edgeborders:
                cornercount +=1
    if cornercount == 4:
        print(tile)


