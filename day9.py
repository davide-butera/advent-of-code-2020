from load import load

data = load()
data = list(map(lambda x: int(x), data))


def isSumNotInList(number, sublist):
    for n in sublist:
        if number - n in sublist:
            return False
    return number


def compute(data):
    preamble = 25
    for i in range(preamble, len(data)):
        first_num = isSumNotInList(data[i], data[i - preamble : i])
        if first_num:
            return first_num


def subArraySum(data, givensum):
    for i in range(len(data)):
        for j in range(len(data)):
            if sum(data[i:j]) > givensum:
                break
            elif sum(data[i:j]) == givensum:
                return min(data[i:j]) + max(data[i:j])


first_num = compute(data)
print(first_num)
print(subArraySum(data, first_num))
