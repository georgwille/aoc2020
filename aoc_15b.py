numbers = [0, 1, 4, 13, 15, 12, 16]
# numbers = [0,3,6]

last_seen = {0: 1, 1: 2, 4: 3, 13: 4, 15: 5, 12: 6}
current_value = 16

# last_seen = {0:1,3:2}
# current_value = 6

current_pos = len(last_seen) + 1

target_pos = 30000000

while True:
    if current_value in last_seen:
        next_value = current_pos - last_seen[current_value]
    else:
        next_value = 0
    last_seen[current_value] = current_pos
    if current_pos == target_pos:
        print(current_pos, current_value)
        break
    current_pos += 1
    current_value = next_value
