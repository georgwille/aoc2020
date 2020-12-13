fin = open('input_13.txt')

start = int(fin.readline())
sched = fin.readline()
sched = sched.strip().split(',')

fin.close()

rc = [] # remainder classes

for i,element in enumerate(sched):
    if element == 'x':
        continue
    else:
        element=int(element)
        rc.append((element,(element-i)%element))

rc.sort(key=lambda entry: entry[0])
rc = rc[::-1]
print(rc)

# Chinese remainder theorem
# we fill the requirements step by step
cumstep, current = rc[0]

for divisor,remainder in rc[1:]:
    print(divisor,remainder)
    while current%divisor != remainder:
        current += cumstep
    print(current)
    cumstep *= divisor

print('t=',current)