import sys

input_file = sys.argv[1]

with open(input_file, "r") as file:
    data = {int(number) for number in file}


def part1():
    for i in data:
        if (2020 - i) in data:
            return i * (2020 - i)


def part2():
    for i in data:
        for j in data:
            if (2020 - i - j) in data:
                return i * j * (2020 - i - j)


print(part1(), part2())
