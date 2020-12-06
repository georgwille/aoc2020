fin = open("input_06.txt")

def groups(gfile):
    current_group = []
    for line in gfile:
        line=line.strip()
        if line == '':
            yield current_group
            current_group = []
            continue
        current_group.append(line)
    if current_group != []:
        yield current_group

yes_sum = 0

for group in groups(fin):
    yes_num = len(set(''.join(group)))
    print(group, yes_num)
    yes_sum += yes_num

print(yes_sum)
