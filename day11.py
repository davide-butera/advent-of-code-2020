import numpy as np
import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = file.read()

data = data.replace("\n", "")
# assign 1 for empty seat, 0 for floor (2 will be used for occupied seat)
binary_data = [1 if x == "L" else 0 for x in data]
binary_data = np.array(binary_data).reshape(-1, 99)
binary_data = np.pad(binary_data, pad_width=1, mode="constant", constant_values=0)
# ad padding to avoid aasdasdad problems at edges
width = binary_data.shape[1]


def first_seat(row, pos):
    right_half = row[pos + 1 :]
    first = right_half[right_half != 0]
    left_half = row[:pos]
    second = left_half[left_half != 0]
    if len(first) != 0:
        first = first[0]
    else:
        first = 0
    if len(second) != 0:
        second = second[-1]
    else:
        second = 0
    return first, second


def seen_seats(data, i, j):
    up, down = first_seat(data[:, j], i)
    left, right = first_seat(data[i], j)
    diag_up, diag_down = first_seat(np.diagonal(data, j - i), min(i, j))
    antidiag_up, antidiag_down = first_seat(
        np.diagonal(np.fliplr(data), width - i - 1 - j),
        min(i, abs(width - 1 - j)),
    )

    return np.array(
        [up, down, left, right, diag_up, diag_down, antidiag_up, antidiag_down]
    )


def step_part_2(data):
    copy_binary_data = np.copy(data)
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            if data[i, j] != 0:
                view = seen_seats(data, i, j)
                if (data[i, j] == 1) and (len(view[view == 2]) == 0):
                    copy_binary_data[i, j] = 2
                elif (data[i, j] == 2) and (len(view[view == 2]) >= 5):
                    copy_binary_data[i, j] = 1
    return copy_binary_data


def solve_part_2(data):
    temp = step_part_2(data)
    while not np.array_equal(data, temp):
        data = temp
        temp = step_part_2(data)

    return len(data[data == 2])


def step_part_1(data):
    copy_binary_data = np.copy(data)
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            if data[i, j] != 0:
                view = data[i - 1 : i + 2, j - 1 : j + 2]
                # If a seat is empty (1) and there are no occupied seats adjacent to it, the seat becomes occupied.
                if (data[i, j] == 1) and (len(view[view == 2]) == 0):
                    copy_binary_data[i, j] = 2
                # If a seat is occupied (2) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                elif (data[i, j] == 2) and (len(view[view == 2]) >= 5):
                    copy_binary_data[i, j] = 1
    return copy_binary_data


def solve_part_1(data):
    temp = step_part_1(data)
    while not np.array_equal(data, temp):
        data = temp
        temp = step_part_1(data)

    return len(data[data == 2])


print(solve_part_1(binary_data))
print(solve_part_2(binary_data))