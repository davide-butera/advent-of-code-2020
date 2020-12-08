import sys


def load():
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        data = list(map(lambda l: l.strip(), file))
    return data