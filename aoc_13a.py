fin = open('input_13.txt')

start = int(fin.readline())
sched = fin.readline()
sched = sched.strip().split(',')

fin.close()

mindiff = 100000000000

for element in sched:
    if element == 'x':
        continue
    else:
        element = int(element)
    diff = element-start%element
    if diff < mindiff:
        mindiff = diff
        minelement = element

print(minelement*mindiff)