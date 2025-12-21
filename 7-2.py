tree = []
with open("7.txt") as f:
    for x in f:
        tree.append(x.rstrip("\n"))

rows = len(tree)
cols = len(tree[0])

start_col = tree[0].index("S")

memo = {}

def count_paths(r, c):
    if c < 0 or c >= cols:
        return 0
    if r == rows:
        return 1
    if (r, c) in memo:
        return memo[(r, c)]

    cell = tree[r][c]
    total = 0

    if cell == "^":
        total += count_paths(r + 1, c - 1)
        total += count_paths(r + 1, c + 1)
    elif cell == "." or cell == "S" or cell == "|":
        total += count_paths(r + 1, c)

    memo[(r, c)] = total
    return total

result = count_paths(1, start_col)
print(result)
