from load import load

data = list(map(lambda l: int(l), load()))


def part1():
    for i in data:
        if (2020 - i) in data:
            return i * (2020 - i)


def part2():
    for i in data:
        for j in data:
            if (2020 - i - j) in data:
                return i * j * (2020 - i - j)


print(part1())
print(part2())
