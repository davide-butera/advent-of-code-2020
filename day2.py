import re
import sys

input_file = sys.argv[1]

with open(input_file, "r") as file:
    data = [line for line in file]

regex = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"


def rule_1(line):
    low, high, letter, password = re.search(regex, line).groups()
    low = int(low)
    high = int(high) + 1

    return password.count(letter) in range(low, high)


def rule_2(line):
    low, high, letter, password = re.search(regex, line).groups()
    low = int(low) - 1
    high = int(high) - 1

    return (password[low] == letter) ^ (password[high] == letter)


count_1 = 0
count_2 = 0
for line in data:
    if rule_1(line):
        count_1 += 1
    if rule_2(line):
        count_2 += 1

print(count_1, count_2)
