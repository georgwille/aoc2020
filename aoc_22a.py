from collections import deque

fin = open('input_22.txt')

digits = '0123456789'
p1 = deque()
p2 = deque()

for line in fin:
    if line[0] in digits:
        p1.append(int(line.strip()))
    if line=='\n':
        break

for line in fin:
    if line[0] in digits:
        p2.append(int(line.strip()))

print(p1)
print(p2)

while True:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1>c2:
        p1.append(c1)
        p1.append(c2)
    elif c1<c2:
        p2.append(c2)
        p2.append(c1)

    print(p1)
    print(p2,'\n')
    if len(p1)==0 or len(p2)==0:
        break


score1 = 0
score2 = 0

for c,el in enumerate(p1):
    score1 += (len(p1)-c)*el

for c,el in enumerate(p2):
    score2 += (len(p2)-c)*el

print(score1,score2)
