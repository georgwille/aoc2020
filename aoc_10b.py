fin = open("input_10.txt")
numbers = [int(line) for line in fin]
fin.close()

numbers.append(0)
numbers.append(max(numbers)+3)

# We calculate the sequence of differences
# when there is a difference of 3, none of the
# two numbers can be skipped
# these "3" posts separate islands where
# flexibility is possible. Inspections shows
# that there are runs of at most four 1's
# (and no 2's! which makes this much easier)
# the different lengths of 1-runs have each the
# following possibilities of arrangements
# 1                         1
# 11 2                      2
# 111 12 21 3               4
# 1111 112 121 211 22 13 31 7
# so an isolated 1 contributes a factor of 1
# two 1's contribute a factor of 2
# three 1's contribute a factor of 4
# four 1's contribute a factor of 7
# now count the number of the various runs
# and multiply the factors
# How could this number of variations be found
# programmatically?

numbers.sort()

factor = {0:1, 1:1, 2:2, 3:4, 4:7}
run = 0
product = 1

for i,number in enumerate(numbers[:-1]):
    diff = numbers[i+1]-number
    if diff == 1:
        run += 1
    else:
        product *= factor[run]
        run = 0


print(product)