# new attempt: try to generate allowed strings
# one after the other and check against the message pool
# on the fly
# but how to make the generator?
# it is tree traversal!
# I generate an ongoing sequence of binary numbers
# 0 and 1 represent taking the left or the right option
# when a decision is required

# Afterthought: this works, but is very slow. Probably
# this cannot be avoided in the general case.
# But taking the very special structure of the input
# into account can make this much faster!
# I say 31 and 42...


fin = open('input_19.txt')

digits = '0123456789'

rules = {}
msgs = []

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

# print('Messages with 24 letters:',count24)

rules['a'] = []
rules['b'] = []
rules[''] = []

# print(rules)
# print(msgs)

dec = 0
finished = False
valid = set()
counter = 0
openbranch = set()

while not finished:
    if not dec%10000:
        print("decision:",dec,"open branches:", len(openbranch), "found:", len(valid),end='          \r')
    finished = True
    declist = list(str(bin(dec))[2:].zfill(30))
    declist = [int(x) for x in declist]
    # print(declist)

    seq = ' 0 '

    has_changed = True
    branch = ''

    while has_changed:
        has_changed = False
        for ele in seq.split(' '):
            if ele not in ['a','b','']:
                has_changed = True
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


for msg in msgs:
    if msg in valid:
        counter += 1

print('\n\ncounter:',counter)