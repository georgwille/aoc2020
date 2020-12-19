# But taking the very special structure of the input
# into account can make this much faster!
# I say 31 and 42...
# We see that the ruleset will produce output
# of the structure YYX, with Y a valid expansion
# of rule 42, and X a valid expansion of rule 31
# we can generate those first (only 128 possibilities
# in each case!, with each 8 characters long),
# and then we can analyse the messages in 8-letter chunks


fin = open('input_19.txt')

digits = '0123456789'

rules = {}
msgs = []
count24 =0

for line in fin:
    if line[0] in digits:
        rule,replace = line.strip().split(': ')
        if replace in ['"a"','"b"']:
            rules[rule] = [replace.strip('"')+' ']
        elif ' | ' in replace:
            x1,x2 = replace.split(' | ')
            rules[rule] = [x1+' ', x2+' ']
        else:
            rules[rule] = [replace+' ']
    if line[0] in 'ab':
        msgs.append(line.strip())
        if len(msgs[-1]) == 24:
            count24 += 1

# print('Messages with 24 letters:',count24)
# input()

rules['a'] = []
rules['b'] = []
rules[''] = []

# print(rules)
# print(msgs)


def get_all(start):
    dec = 0
    finished = False
    valid = set()
    counter = 0
    openbranch = set()
    rulesseen = set()

    while not finished:
        if not dec%1000:
            print("decision:",dec,"open branches:", len(openbranch), "found:", len(valid),end='          \r')
        finished = True
        declist = list(str(bin(dec))[2:].zfill(30))
        declist = [int(x) for x in declist]
        # print(declist)

        seq = ' '+str(start)+' '

        has_changed = True
        branch = ''

        while has_changed:
            has_changed = False
            for ele in seq.split(' '):
                if ele not in ['a','b','']:
                    has_changed = True
                    rulesseen.add(ele)
                    # print('seq:',seq)
                    # print('ele:',ele, 'rules:',rules[ele])
                    if len(rules[ele])>1:
                        turn = declist.pop()
                        # print('turn:',turn)
                        if turn==0:
                            openbranch.add(branch)
                        elif turn==1:
                            openbranch.remove(branch)
                        branch += str(turn)
                        # print('branch:',branch)
                        # print('openbranch:',openbranch)
                        seq=seq.replace(' '+ele+' ',' '+rules[ele][turn],1)
                    else:
                        seq=seq.replace(' '+ele+' ',' '+rules[ele][0],1)
                    break
        # input()
        # print(seq)
        compressed = seq.replace(' ','')
        valid.add(compressed)
        # print(compressed)
        # print(len(compressed))
        dec += 1
        if len(openbranch) > 0:
            finished = False

    return valid

valid31 = get_all(31)
valid42 = get_all(42)

# print(valid31,len(valid31))
# print(valid42,len(valid42))

# print(valid31.intersection(valid42))

counter = 0

for msg in msgs:
    parts = [msg[8*i:8*i+8] for i in range(len(msg)//8)]
    # print(msg, parts)
    struct = ''
    countX = 0
    countY = 0
    for part in parts:
        if part in valid31:
            struct += 'X'
            countX += 1
        elif part in valid42:
            struct += 'Y'
            countY += 1
        else:
            struct += 'Z'
    print(struct)
    if struct == "YYX":
        counter += 1


print(counter)