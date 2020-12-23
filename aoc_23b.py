start = "487912365"
# start = "389125467"

max = 10**6

rn = {} # contains the right neighbor of x

for i,c in enumerate(start,1):
    try:
        rn[int(c)] = int(start[i])
    except IndexError:
        rn[int(c)] = 10
        break

for i in range(10,max):
    rn[i] = i+1

rn[max] = int(start[0])

curr = int(start[0])

movecount = 10000000

while movecount:
    if movecount%10000 ==0:
        print(movecount,end="        \r")
    movecount -= 1
    a = rn[curr]
    b = rn[a]
    c = rn[b]
    d = rn[c]
    # print(a,b,c,d)
    rn[curr] = d
    dest = curr-1
    if dest == 0:
        dest = max
    while dest in [a,b,c]:
        dest -= 1
        if dest == 0:
            dest = max

    destrn = rn[dest]
    rn[dest] = a
    rn[c]=destrn
    curr = rn[curr]

print("\n")
k = 1
for i in range(10):
    print(k,end=" ")
    k = rn[k]

print("\n",rn[1]*rn[rn[1]])