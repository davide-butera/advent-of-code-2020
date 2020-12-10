from load import load

data = load()
data = list(map(lambda x: int(x), data))
data = [0] + list(set(data)) + [max(data) + 3]

diffs = {1: 1, 3: 1}
for i in range(1, len(data)):
    diff = data[i] - data[i - 1]
    diffs[diff] += 1
print(diffs[1] * diffs[3])


def ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))


ranges = ranges(data)
product = 1
tribonacci = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}

for r in ranges:
    product *= tribonacci[r[1] - r[0]]
print(product)