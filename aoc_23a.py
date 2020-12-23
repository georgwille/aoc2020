start = "487912365"
# start = "389125467"

cups = [int(c) for c in start]
mincup = min(cups)
maxcup = max(cups)

current = cups[0]

moves = 100


def pick3(cups,current):
    # print(cups, current)
    temp = cups.copy()
    temp.extend(cups)
    # print(temp, current)
    # print(current in temp)
    curr_index = temp.index(current)
    triplet = temp[curr_index+1:curr_index+4]
    new = [i for i in temp if i not in triplet]
    new = new[:len(cups)-3]
    return triplet, new


for move in range(moves):
    print(cups,current)
    triplet, rest = pick3(cups,current)
    print(triplet, rest)
    dest = current-1
    if dest == 0:
        dest = 9
    while dest in triplet:
        dest -= 1
        if dest == 0:
            dest = 9
    print("Destination:",dest,"\n")
    d_i = rest.index(dest)
    cups = rest[:d_i+1]+triplet+rest[d_i+1:]
    c_i = cups.index(current)
    if c_i == len(cups)-1:
        current = cups[0]
    else:
        current = cups[c_i+1]

print(cups)

