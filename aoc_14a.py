fin = open("input_14.txt")

def applymask(mask, number):
    binstr = str(bin(int(number)))[2:]
    binresult = ''
    for i,char in enumerate(mask[::-1]):
        try:
            bit = binstr[-(i+1)]
        except IndexError:
            bit = '0'
        if char == '0':
            bit = '0'
        elif char == '1':
            bit = '1'
        binresult += bit
    binresult = binresult[::-1]
    return int(binresult,base=2)

memory = {}

for line in fin:
    line = line.strip()
    if line.startswith('mask'):
        mask = line.split("=")[1].strip()
    elif line.startswith('mem'):
        address = int(line[line.index('[')+1:line.index(']')])
        value = int(line.split("=")[1].strip())
        memory[address] = applymask(mask,value)

total = 0

for key in memory:
    total += memory[key]

print(total)
