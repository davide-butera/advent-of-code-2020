import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = [line.strip() for line in file]

dictionary = {}
for d in data:
    outer_bag = " ".join(d.split(" ")[:2])
    inner_bag = " ".join(d.split(" ")[4:])
    dictionary[outer_bag] = {}
    inner_dict = {}
    for v in inner_bag.split(","):
        v = v.strip().split(" ")
        v_key = " ".join(v[1:3])
        inner_dict[v_key] = v[0]
        dictionary[outer_bag] = inner_dict


def can_contain(outer, inner):
    if dictionary.get(outer) == {"other bags.": "no"}:
        return False
    elif inner in dictionary.get(outer):
        return True
    else:
        for key in dictionary.get(outer):
            if can_contain(key, inner):
                return True
    return False


count = 0
for outer_bag in dictionary:
    count += can_contain(outer_bag, "shiny gold")

print(count)


def compute(key):
    if dictionary[key] == {"other bags.": "no"}:
        return 1
    else:
        list = [compute(i[0]) * int(i[1]) for i in dictionary[key].items()]
        return sum(list) + 1


print(compute("shiny gold") - 1)
