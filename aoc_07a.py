fin = open("input_07.txt")

target = "shiny gold"

outside_of = {}
whats_in = {}
may_contain_target = {}

for line in fin:
    line = line[:-1]
    outer, inner = line.split("bags contain")
    outer = outer.strip()
    inner = inner.split(",")
    # print(outer, inner)
    for element in inner:
        element = element.strip()
        parts = element.split(" ")
        innercolor = parts[1] + " " + parts[2]
        if innercolor in outside_of:
            outside_of[innercolor].append(outer)
        else:
            outside_of[innercolor] = [outer]
        may_contain_target[outer] = False

# print(outside_of)

counter = 0

for color in outside_of[target]:
    # print(color)
    may_contain_target[color] = True
    counter += 1

# print(may_contain_target)

incomplete = True

while incomplete:
    incomplete = False
    for color in may_contain_target:
        if may_contain_target[color] and color in outside_of:
            for element in outside_of[color]:
                if not may_contain_target[element]:
                    may_contain_target[element] = True
                    counter += 1
                    incomplete = True

# print(may_contain_target)
print(counter)
