fin = open("input_17.txt")

start = fin.readlines()
fin.close()

import numpy as np 

maxdim = 50

a = np.zeros((maxdim,maxdim,maxdim))
# b = np.zeros((maxdim,maxdim,maxdim))

for r,line in enumerate(start):
    line = line.strip()
    for c,char in enumerate(line):
        if char == '#':
            a[r+maxdim//2,c+maxdim//2,maxdim//2] = 1

def tick():
    global a
    b = a.copy()
    for r in range(1,maxdim-1):
        for c in range(1,maxdim-1):
            for z in range(1,maxdim-1):
                ncount = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        for dz in [-1,0,1]:
                            if dr == 0 and dc == 0 and dz == 0:
                                continue
                            ncount += a[r+dr,c+dc,z+dz]
                if a[r,c,z] == 1 and ncount not in [2,3]:
                    b[r,c,z] = 0
                if a[r,c,z] == 0 and ncount==3:
                    b[r,c,z] = 1
    a = b

for i in range(7):
    print(np.sum(a))
    tick()


