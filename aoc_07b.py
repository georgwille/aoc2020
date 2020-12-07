fin = open("input_07.txt")

target = "shiny gold"

outside_of = {}
whats_in = {}
may_contain_target = {}

for line in fin:
    line = line.strip()[:-1]
    outer, inner = line.split("bags contain")
    outer = outer.strip()
    inner = inner.split(",")
    # print(outer,inner)
    for element in inner:
        element = element.strip()
        parts = element.split(" ")
        innercolor = parts[1] + " " + parts[2]
        amount = 0 if parts[0] == "no" else int(parts[0])
        if outer in whats_in:
            whats_in[outer].append((amount, innercolor))
        else:
            whats_in[outer] = [(amount, innercolor)]

# print(whats_in)
# print(whats_in[target])


def bags_in(color):
    # print(color, whats_in[color])
    if whats_in[color][0][0] == 0:
        # print("End of recursion reached")
        return 1
    sum_ = 0
    for element in whats_in[color]:
        sum_ += element[0] * bags_in(element[1])
    return sum_ + 1

print(bags_in(target) - 1)
