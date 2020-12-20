# all this relies on the borders being unique
# no backtracking! monsters don't overlap

import numpy as np

fin = open('input_20.txt')
lines = fin.readlines()
fin.close()

tiles={} # ndarrays with the tile data
tiles[0]=np.zeros((10,10),dtype='int8')
borders = {} # two lists with four numbers each for each tile
tile_with_border = {} # for each border-id a list of tiles with this id

image = np.zeros((12*8,12*8),dtype='int8')

tileorder = np.zeros((12,12),dtype='int16')

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

def find_matching_tile(row,col,match='up'):
    if match=='up':
        nrow,ncol,where,twhere=row-1,col,2,0
    elif match=='left':
        nrow,ncol,where,twhere=row,col-1,1,3

    target = borders[tileorder[nrow][ncol]][1][where]
    matchingtiles = tile_with_border[target]
    # print(matchingtiles)
    newtile = matchingtiles[0] if matchingtiles[0] != tileorder[nrow][ncol] else matchingtiles[1]
    if target in borders[newtile][1]:
        tiles[newtile] = np.fliplr(tiles[newtile])
        borders[newtile] = getborders(tiles[newtile])
    while True:
        if not(borders[newtile][0][twhere]==target):
            tiles[newtile] = np.rot90(tiles[newtile])
            borders[newtile] = getborders(tiles[newtile])
        else:
            break
    return newtile

def print_image(image):
    for r in range(8*12):
        for c in range(8*12):
            if image[r,c]==1:
                print('.',end='')
            elif image[r,c]==0:
                print(' ',end='')
            else:
                print(image[r,c],end='')
        print()

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
        # print(thistile)
        borders[tile_id]=getborders(thistile)
        # print(borders[tile_id])
        for orientation in borders[tile_id]:
            for element in orientation:
                try:
                    tile_with_border[element].append(tile_id)
                except KeyError:
                    tile_with_border[element] = [tile_id]

edgeborders = set()

for border in tile_with_border:
    btiles = tile_with_border[border]
    if len(btiles) ==1:
        edgeborders.add(border)

# print(edgeborders)

for tile in borders:
    b = borders[tile]
    cornercount = 0
    for orientation in b:
        for bid in orientation:
            if bid in edgeborders:
                # print(tile,bid)
                cornercount +=1
    if cornercount == 4:
        topleft = tile
        break

# print(tiles[topleft])
# print(borders[topleft])

while True:
    if not(borders[topleft][0][0] in edgeborders and borders[topleft][0][3] in edgeborders):
        tiles[topleft] = np.rot90(tiles[topleft])
        borders[topleft] = getborders(tiles[topleft])
    else:
        break

# print(tiles[topleft])
# print(topleft)

tileorder[0][0] = topleft
# print(tileorder)


for row in range(12):
    for col in range(12):
        # print('row:',row,'col:',col)
        # topleft is placed alread
        if row==0 and col==0:
            continue
        # if we are very left, match top border to row above
        if col == 0:
            direction = 'up'
        # otherwise, match left border to column on left
        else:
            direction = 'left'
        tileorder[row][col] = find_matching_tile(row,col,direction)

print(tileorder)

for r in range(12):
    for c in range(12):
        image[r*8:r*8+8,c*8:c*8+8]=tiles[tileorder[r][c]][1:9,1:9]


print_image(image)

monster = np.asarray(
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
     [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]],dtype='int8')

# print(monster)

monsterimage = image.copy()

for flip in [False,True]:
    for rot in [0,1,2,3]:
        checkmonster = monster.copy()
        if flip:
            checkmonster = np.fliplr(checkmonster)
        checkmonster = np.rot90(checkmonster,rot)
        h,w = checkmonster.shape
        for r in range(8*12-h):
            for c in range(8*12-w):
                testimage = image.copy()
                testimage[r:r+h,c:c+w] -= checkmonster
                if (testimage[r:r+h,c:c+w] >= 0).all():
                    monsterimage[r:r+h,c:c+w] += checkmonster

print_image(monsterimage)

print(np.count_nonzero(monsterimage==1))