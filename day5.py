from load import load

data = load()

rules = {"L": "0", "R": "1", "F": "0", "B": "1"}

# BFFFBBFRRR -> 1000110111 -> 567
def seat_to_int(seat, rules):
    binary_seat = [rules[i] for i in seat]
    return int("".join(binary_seat), 2)


seat_list = [seat_to_int(line, rules) for line in data]
print(max(seat_list))

i = min(seat_list)
while i in seat_list:
    i += 1
print(i)


"""
max = 0
seat_set = set()

for line in data:
    current_line = seat_to_int(line, rules)
    seat_set.add(current_line)
    if current_line > max:
        max = current_line

print(max)
"""