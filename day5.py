import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = [line.strip() for line in file]


# BFFFBBFRRR -> 1000110111 -> 567
def seat_to_int(seat):
    binary_seat = ""
    for i in seat:
        if i in {"F", "L"}:
            binary_seat += "0"
        else:
            binary_seat += "1"
    return int(binary_seat, 2)


# alternative one liner
def seat_to_int(seat):
    return int("".join(["0" if i in {"F", "L"} else "1" for i in seat]), 2)


max = 0
seat_set = {0, 1}
print
for line in data:
    current_line = seat_to_binary(line)
    seat_set.add(current_line)
    if current_line > max:
        max = current_line

print(max)

i = min(seat_set)
while i in seat_set:
    i += 1
print(i)