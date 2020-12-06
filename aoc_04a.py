fin = open("input_04.txt")

valid_count = 0

def passports(pfile):
    plist = []
    current_passport = {}
    for line in pfile:
        line=line.strip()
        if line == '':
            plist.append(current_passport)
            current_passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            key,value=field.split(':')
            current_passport[key]=value
    if current_passport != {}:
        plist.append(current_passport)
    return plist

def isvalid(p):
    requiredkeys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    return all(rk in p for rk in requiredkeys)


mypassports = passports(fin)

for p in mypassports:
    print(p, isvalid(p))
    if isvalid(p):
        valid_count += 1

print(valid_count)