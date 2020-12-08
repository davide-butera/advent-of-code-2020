from load import load

data = load()
data.append("")

eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
valid_attributes = {"eyr", "iyr", "byr", "hcl", "hgt", "ecl", "pid"}


def isValid(key, value):
    if value.isnumeric():
        if key == "pid":
            return len(value) == 9
        year = int(value)
        if key == "byr":
            return 1920 <= year <= 2002
        elif key == "iyr":
            return 2010 <= year <= 2020
        elif key == "eyr":
            return 2020 <= year <= 2030
    elif key == "hgt":
        height = int(value[:-2])
        if value[-2:] == "cm":
            return 150 <= height <= 193
        elif value[-2:] == "in":
            return 59 <= height <= 76
    elif key == "hcl":
        return value[0] == "#" and value[1:].isalnum()
    elif key == "ecl":
        return value in eye_colors
    else:
        return False


def countValid(data, rules):
    attributes = set()
    count = 0
    for line in data:
        for attr in line.split(" "):
            attr = attr.split(":")
            if attr[0] != "":
                if attr[0] != "cid":
                    if rules:
                        if isValid(attr[0], attr[1]):
                            attributes.add(attr[0])
                    else:
                        attributes.add(attr[0])
        if line == "":
            if attributes == valid_attributes:
                count += 1
            attributes = set()
    return count


print(countValid(data, False))
print(countValid(data, True))
