from load import load

data = load()
starting_numbers = [int(x) for x in data[0].split(",")]


def compute(numbers, end):
    number_record = {n: i + 1 for i, n in enumerate(numbers[:-1])}
    last_number = numbers[-1]
    for turn in range(len(numbers), end):
        last_spoken_number = number_record.get(last_number, -1)
        number_record[last_number] = turn
        new_number = 0
        if last_spoken_number > 0:
            new_number = turn - last_spoken_number
        last_number = new_number
    return last_number


print(compute(starting_numbers, 2020))
print(compute(starting_numbers, 30000000))