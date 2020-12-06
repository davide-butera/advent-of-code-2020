import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = file.read()
    data_2 = [d for d in data.split("\n\n")]
    data_1 = [d.replace("\n", "") for d in data_2]


def part_1(data):
    sum = 0
    for d in data:
        sum += len(set(d))
    return sum


def part_2(data_2):
    sum = 0
    for d in data_2:
        d_list = d.split("\n")
        answer_set = set(d_list[0])
        for i in d_list:
            answer_set = answer_set.intersection(set(i))
        sum += len(answer_set)
    return sum


print(part_1(data_1))
print(part_2(data_2))