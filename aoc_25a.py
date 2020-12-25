# quick and dirty

core = 20201227

card_pk = 17115212
door_pk = 3667832

loops =[]

for pk in [card_pk, door_pk]:
    loopcount = 0

    subject = 7
    value = 1

    while True:
        loopcount += 1
        value *= subject
        value %= core

        if  value == pk:
            print(loopcount)
            loops.append(loopcount)
            break

card_loop, door_loop = loops[0], loops[1]

subject = door_pk
value = 1

for i in range(card_loop):
    value *= subject
    value %= core

print(value)

subject = card_pk
value = 1

for i in range(door_loop):
    value *= subject
    value %= core

print(value)

