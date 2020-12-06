fin = open("input_04.txt")

def passports(pfile):
    plist = []
    current_passport = {}
    for line in pfile:
        line = line.strip()
        if line == '':
            plist.append(current_passport)
            current_passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            current_passport[key] = value
    if current_passport != {}:
        plist.append(current_passport)
    return plist


def isvalid(p):
    requiredkeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if len(p) not in [7, 8]:
        return False, 'len'
    for rk in requiredkeys:
        if rk not in p:
            return False, 'key'
    for key in p:
        if key not in requiredkeys and key != 'cid':
            return False, 'cid'
    if not(1920 <= int(p['byr']) <= 2002):
        return False, 'byr'
    if not(2010 <= int(p['iyr']) <= 2020):
        return False, 'iyr'
    if not(2020 <= int(p['eyr']) <= 2030):
        return False, 'eyr'
    if p['hgt'].endswith('cm') and not(150 <= int(p['hgt'][:-2]) <= 193):
        return False, 'cm'
    if p['hgt'].endswith('in') and not(59 <= int(p['hgt'][:-2]) <= 76):
        return False, 'in'
    if p['hgt'][-2:] not in ['in', 'cm']:
        return False, 'hgt'
    try:
        hcl = int(p['hcl'][1:], base=16)
    except:
        return False, 'hcl'
    for digit in p['hcl'][1:]:
        if digit not in 'abcdef0123456789':
            return False, 'dig'
    if p['hcl'][0] != '#' or len(p['hcl']) != 7:
        return False, 'hcl'
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False, 'ecl'
    if len(p['pid']) != 9 or not(p['pid'].isdigit()):
        return False, 'pid'
    return True, '###'


mypassports = passports(fin)
fail = {}
valid_count = 0

for p in mypassports:
    # print(p, isvalid(p))
    if isvalid(p)[0]:
        valid_count += 1
    else:
        print(isvalid(p), p)
        if isvalid(p)[1] in fail:
            fail[isvalid(p)[1]] += 1
        else:
            fail[isvalid(p)[1]] = 1

print(valid_count, fail, len(fail))
