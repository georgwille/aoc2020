# all this is unnecessary
# search and replace in a good text editor with
# line sorting is enough

fin = open("input_05.txt")

seatlist = []

for line in fin:
    line = line.strip()
    line = line.replace("B","1")
    line = line.replace("F","0")
    line = line.replace("R","1")
    line = line.replace("L","0")
    seatlist.append(int(line,base=2))

seatlist.sort()
print(seatlist[-1])

for i,number in enumerate(seatlist[:-1]):
    if seatlist[i+1]-number !=1:
        print(number+1)
