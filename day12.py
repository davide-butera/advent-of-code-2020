from load import load

data = load()


current_pos = [0, 0]
current_dir = "E"

direction_dict = {"E": "W", "S": "N"}
direction_degrees = {"E": 0, "N": 90, "W": 180, "S": 270}
degrees_direction = {0: "E", 90: "N", 180: "W", 270: "S"}


def move(pos, direction, steps):
    if direction == "W":
        pos[0] += steps
    elif direction == "N":
        pos[1] += steps
    elif direction == "E":
        pos[0] -= steps
    elif direction == "S":
        pos[1] -= steps
    return pos


def move_forward(pos, steps):
    return move(pos, current_dir, steps)


def turn(current_dir, degrees):
    current_dir = direction_degrees[current_dir]
    current_dir = degrees_direction[(current_dir + degrees) % 360]
    return current_dir


def manhattan(a, b):
    return abs(a) + abs(b)


def part_1(current_pos, current_dir, data):
    for line in data:
        if (line[0]) in direction_degrees:
            current_pos = move(current_pos, line[0], int(line[1:]))
        elif line[0] == "R":
            current_dir = turn(current_dir, -1 * int(line[1:]))
        elif line[0] == "L":
            current_dir = turn(current_dir, int(line[1:]))
        elif line[0] == "F":
            current_pos = move(current_pos, current_dir, int(line[1:]))
    return manhattan(current_pos[0], current_pos[1])


def part_2(current_pos, data):
    current_pos = [0, 0]
    way_pos = [-10, 1]
    for line in data:
        if (line[0]) in direction_degrees:

            way_pos = move(way_pos, line[0], int(line[1:]))
        elif line[0] == "R":
            way_pos = rotate(
                way_pos[0],
                way_pos[1],
                current_pos[0],
                current_pos[1],
                math.radians(int(line[1:])),
            )
        elif line[0] == "L":
            way_pos = rotate(
                way_pos[0],
                way_pos[1],
                current_pos[0],
                current_pos[1],
                math.radians(int(line[1:])) * -1,
            )
        elif line[0] == "F":
            next_x = (way_pos[0] - current_pos[0]) * int(line[1:])
            next_y = (way_pos[1] - current_pos[1]) * int(line[1:])
            current_pos[0] += next_x
            current_pos[1] += next_y
            way_pos[0] += next_x
            way_pos[1] += next_y
    return int(manhattan(current_pos[0], current_pos[1]))


def manhattan(a, b):
    return abs(a) + abs(b)


import math


def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
    xr = math.cos(theta) * (x - xo) - math.sin(theta) * (y - yo) + xo
    yr = math.sin(theta) * (x - xo) + math.cos(theta) * (y - yo) + yo
    return [xr, yr]


print(part_1(current_pos, current_dir, data))
print(part_2(current_pos, data))