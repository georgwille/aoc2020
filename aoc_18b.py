fin = open("input_18.txt")

digits = '1234567890'


def end_of_operand(text):
    if text[0] == '(':
        plevel = 1
        for i, char in enumerate(text[1:], 1):
            if char == '(':
                plevel += 1
            elif char == ')':
                plevel += -1
            if plevel == 0:
                leftop = text[1:i]
                parsepos = i
                break
    elif text[0] in digits:
        leftop=text[0]
        parsepos=1
    # print('insert parens after', leftop, parsepos)
    return parsepos

def insertparens(text, operator):
    num_operator = text.count(operator)
    for cur_operator in range(1,num_operator+1):
        tick = 0
        for c_i,char in enumerate(text):
            if char == operator:
                tick += 1
                if tick == cur_operator:
                    break
        left = text[:c_i]
        left = invert(left)
        right = text[c_i+1:]
        # print('left: ',left)
        # print('right:',right)
        eol = end_of_operand(left)
        eor = end_of_operand(right)
        left = left[:eol]+')'+left[eol:]
        right = right[:eor]+')'+right[eor:]
        # print('left: ',left)
        # print('right:',right)
        text = invert(left)+operator+right
    # print('Parenthesis inserted:',text)
    return text


def invert(text):
    text = text[::-1]
    text = text.replace('(', 'X')
    text = text.replace(')', '(')
    text = text.replace('X', ')')
    return text

def prep(text):
    text = text.strip().replace(' ', '')
    # text = invert(text)
    text = insertparens(text,'+')
    return text


def geval(text):
    # print(text)

    if text[0] == '(':
        plevel = 1
        for i, char in enumerate(text[1:], 1):
            if char == '(':
                plevel += 1
            elif char == ')':
                plevel += -1
            if plevel == 0:
                leftop = text[1:i]
                parsepos = i
                break
        # print('parsepos', parsepos, len(text), leftop)
        if parsepos == len(text) - 1:
            return int(geval(leftop))
        else:
            op = text[parsepos + 1]
            rightop = text[parsepos + 2:]
    elif text[0] in digits:
        if len(text) == 1:
            return int(text)
        else:
            leftop = text[0]
            op = text[1]
            rightop = text[2:]
    # print(leftop, op, rightop)
    if op == '+':
        return int(geval(leftop)) + int(geval(rightop))
    elif op == '*':
        return int(geval(leftop)) * int(geval(rightop))


total = 0

for line in fin:
    pline = prep(line)
    print(line,end='')
    result = int(geval(pline))
    print(pline, '=', result,'\n')
    total += result

fin.close()

print(total)
