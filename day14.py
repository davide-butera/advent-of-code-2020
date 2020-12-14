from load import load
import re


def apply_bitmask(number, mask):
    positive_pattern = int(mask.replace("X", "1"), 2)
    negative_pattern = int(mask.replace("X", "0"), 2)
    return number & positive_pattern | negative_pattern


def apply_mask_2(string_1, string_2):
    res = []
    for i in zip(string_1, string_2):
        if i[1] == "X":
            res.append(i[1])
        else:
            res.append(str(int(i[0], 2) | int(i[1], 2)))
    return "".join(res)


def get_addresses(string):
    x_count = string.count("X")
    strings = [string] * (2 ** x_count)
    zip_strings = list(
        map(
            list,
            zip(strings, [format(i, f"0{x_count}b") for i in range(0, len(strings))]),
        )
    )
    for i in zip_strings:
        for j in i[1]:
            i[0] = i[0].replace("X", j, 1)
    result = [int(i[0], 2) for i in zip_strings]
    return result


data = load()
memory = {}
current_mask = ""

for line in data:
    if line[:4] == "mask":
        current_mask = line[7:]
    else:
        address, content = re.match("mem\[(\d+)\] = (\d+)", line).groups()
        memory[int(address)] = apply_bitmask(int(content), current_mask)

print(sum(memory.values()))

# part 2
memory = {}
current_mask = ""

for line in data:
    if line[:4] == "mask":
        current_mask = line[7:]
    else:
        address, content = re.match("mem\[(\d+)\] = (\d+)", line).groups()
        address = int(address)
        content = int(content)
        results = get_addresses(
            apply_mask_2(format(address, f"0{len(current_mask)}b"), current_mask)
        )
        for i in results:
            memory[i] = content


print(sum(memory.values()))