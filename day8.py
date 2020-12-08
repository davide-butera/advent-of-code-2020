import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = [line.strip() for line in file]


def value_to_int(value):
    v = int(value[1:])
    return v if (value[0] == "+") else -v


def read_instructions(cursor, acc, parsed_lines, data, *args):
    if cursor in parsed_lines:
        if args:
            return acc
    elif cursor == len(data):
        return acc
    else:
        parsed_lines.add(cursor)
        instruction, value = data[cursor].split()
        value = value_to_int(value)
        if instruction == "nop":
            cursor += 1
        elif instruction == "jmp":
            cursor += value
        elif instruction == "acc":
            acc += value
            cursor += 1
        return read_instructions(cursor, acc, parsed_lines, data, *args)
    return False


print(read_instructions(0, 0, set(), data, True))

# part 2
swap_dict = {"jmp": "nop", "nop": "jmp"}
for i in range(len(data)):
    parsed_lines = set()
    instruction, value = data[i].split()
    if instruction in swap_dict:
        data[i] = f"{swap_dict[instruction]} {value}"
        found = read_instructions(0, 0, set(), data)
        print(found) if found else 0
        data[i] = f"{instruction} {value}"
