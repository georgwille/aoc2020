fin = open("input_01.txt")

myinput = fin.readlines()

mynumbers = [int(entry) for entry in myinput]

mynumbers.sort()

print(mynumbers)

for i in range(len(mynumbers)):
    for j in range(i+1,len(mynumbers)):
        diff = 2020-mynumbers[i]-mynumbers[j]
        if diff in mynumbers:
            print(i,j,diff,mynumbers[i]*mynumbers[j]*diff)