fin = open("input_18.txt")

digits = '1234567890'

def prep(text):
    text = text.strip().replace(' ','')
    text = text[::-1]
    text = text.replace('(','X')
    text = text.replace(')','(')
    text = text.replace('X',')')
    return text

def geval(text):
    # print(text)

    if text[0] == '(':
        plevel = 1
        for i,char in enumerate(text[1:],1):
            if char == '(':
                plevel += 1
            elif char == ')':
                plevel += -1
            if plevel == 0:
                leftop = text[1:i]
                parsepos=i
                break
        # print('parsepos',parsepos,len(text),leftop)
        if parsepos == len(text)-1:
            return int(geval(leftop))
        else:
            op=text[parsepos+1]
            rightop=text[parsepos+2:]
    elif text[0] in digits:
        if len(text) == 1:
            return int(text)
        else:
            leftop = text[0]
            op = text[1]
            rightop = text[2:]
    # print(leftop,':',op,':',rightop)
    if op=='+':
        return int(geval(leftop))+int(geval(rightop))
    elif op=='*':
        return int(geval(leftop))*int(geval(rightop))

total = 0

for line in fin:
    print(line,end='')
    pline = prep(line)
    result = int(geval(pline))
    total += result
    print(pline,'=',result,'\n')

fin.close()

print(total)