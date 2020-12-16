fin = open('input_16.txt')

all = fin.readlines()

fin.close()
ntickets = all[25:]

fields = {
'departure location': [49,258,268,960],
'departure station': [37,117,128,968],
'departure platform': [31,70,78,974],
'departure track': [26,234,247,952],
'departure date': [49,625,635,969],
'departure time': [26,777,799,974],
'arrival location': [49,735,757,971],
'arrival station': [28,381,399,970],
'arrival platform': [49,77,95,957],
'arrival track': [29,467,477,950],
'class': [40,218,234,967],
'duration': [45,900,911,970],
'price': [42,442,452,966],
'route': [45,104,112,953],
'row': [49,877,884,957],
'seat': [40,168,184,953],
'train': [43,913,920,949],
'type': [43,292,315,955],
'wagon': [48,547,558,954],
'zone': [40,929,935,954],
}

myticket = [59,101,191,149,167,197,199,137,163,131,113,67,103,97,61,139,157,151,193,53]

def is_in_any_field(number):
    for field in fields:
        if is_in_range(number,field):
            return True
    return False

def is_in_range(number, field):
    c = fields[field]
    if c[0]<=number<=c[1] or c[2]<=number<=c[3]:
        return True
    return False

errorsum = 0
vtickets = []

for ticket in ntickets:
    dirty = False
    numbers = ticket.strip().split(',')
    for number in numbers:
        if not is_in_any_field(int(number)):
            errorsum += int(number)
            dirty = True
    if not dirty:
        vtickets.append(ticket)

print("Error sum:", errorsum)
print("Valid tickets:", len(vtickets))

couldbe = {}
for field in fields:
    couldbe[field] = [1 for i in range(len(fields))]

for field in fields:
    for position in range(len(fields)):
        for ticket in vtickets:
            numbers = ticket.strip().split(',')
            n = int(numbers[position])
            # print(fields[field],n)
            if not(is_in_range(n,field)):
                couldbe[field][position] = 0

truth = []

for field in fields:
    # print(couldbe[field], sum(couldbe[field]), field)
    truth.append((couldbe[field],field))

truth.sort(key=lambda truth: sum(truth[0]))

print(' ',end='')
for i in range(20):
    print(str(i).zfill(2),end=' ')
print()
for element in truth:
    print(element)

mapping = {}

for i,(poss,label) in enumerate(truth):
    for j,el in enumerate(poss):
        if i==0 and el==1:
            mapping[label]=j
            break
        elif el==1 and truth[i-1][0][j]==0:
            mapping[label]=j
            break

print(mapping)

product = 1

for el in mapping:
    if el.startswith('dep'):
        product *= myticket[mapping[el]]

print(product)
