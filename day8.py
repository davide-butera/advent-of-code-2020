from load import load

data = load()


def read_line(line):
    value = int(line[5:])
    if line[4] == "-":
        value *= -1
    return (line[:3], value)


def exec_instruction(code, instruction, value, count, acc, flag):
    if code[count][1]:
        flag = False
    else:
        code[count][1] = True
        if instruction == "jmp":
            count += value
        elif instruction == "acc":
            acc += value
            count += 1
        elif instruction == "nop":
            count += 1
    return count, acc, flag


def exec_program(data):
    code = list(map(lambda x: [x, False], data))
    count, acc, flag = (0, 0, True)
    while flag:
        # part 2
        if len(code) == count:
            print(acc)
            return count, acc
        count, acc, flag = exec_instruction(
            code, *read_line(code[count][0]), count, acc, flag
        )
    return count, acc


print(exec_program(data)[1])

swap_dict = {"jmp": "nop", "nop": "jmp"}
for i in range(len(data)):
    instruction, value = data[i].split()
    if instruction in swap_dict:
        data[i] = f"{swap_dict[instruction]} {value}"
        exec_program(data)
        data[i] = f"{instruction} {value}"