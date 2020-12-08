from load import load

data = load()
height = len(data)
width = len(data[0])


def descend_slope(right: int, down: int) -> int:
    x = y = 0
    trees = ""
    while y < height:
        # Add next point to trees array even if not all of them are trees
        trees += data[y][x]
        x = (x + right) % width
        y += down
    return trees.count("#")  # count the trees (#)


print(descend_slope(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1
for slope in slopes:
    product *= descend_slope(*slope)

print(product)
