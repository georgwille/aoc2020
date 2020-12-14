fin = open("input_14.txt")

def applymask(mask, base_address):
    base = str(bin(int(base_address)))[2:]
    addresses = ['']
    for i,mchar in enumerate(mask[::-1]):
        try:
            bit = base[-(i+1)]
        except IndexError:
            bit = '0'
        if mchar == '0':
            for j in range(len(addresses)):
                addresses[j] += bit
        elif mchar == '1':
            for j in range(len(addresses)):
                addresses[j] += '1'
        elif mchar == 'X':
            temp = []
            for j in range(len(addresses)):
                temp.append(addresses[j]+'1')
                addresses[j] += '0'
            addresses.extend(temp)
    # print(addresses)
    final = []
    for address in addresses:
        final.append(int(address[::-1],base=2))
    # print(final)
    return final

memory = {}

for line in fin:
    line = line.strip()
    if line.startswith('mask'):
        mask = line.split("=")[1].strip()
    elif line.startswith('mem'):
        base_address = int(line[line.index('[')+1:line.index(']')])
        value = int(line.split("=")[1].strip())
        alist = applymask(mask,base_address)
        for address in alist:
            memory[address] = value

total = 0

for key in memory:
    total += memory[key]

print(len(memory),total)
