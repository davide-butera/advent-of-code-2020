import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = [line.strip() for line in file]


# BFFFBBFRRR -> 1000110111 -> 567
def seat_to_int_classic(seat):
    binary_seat = ""
    for i in seat:
        if i in {"F", "L"}:
            binary_seat += "0"
        else:
            binary_seat += "1"
    return int(binary_seat, 2)


def seat_to_int(seat):
    rules = {"B": "1", "F": "0", "R": "1", "L": "0"}
    binary_seat = [rules[i] for i in seat]
    return int("".join(binary_seat), 2)


max = 0
seat_set = {0, 1}
print
for line in data:
    current_line = seat_to_int(line)
    seat_set.add(current_line)
    if current_line > max:
        max = current_line

print(max)

i = min(seat_set)
while i in seat_set:
    i += 1
print(i)