tree = []
with open("7.txt") as f:
    for x in f:
        x = x.strip()
        tree.append(x)
result = 0
for i in range(len(tree) - 1):
    for j in range(1, len(tree[0]) - 1):
        if (tree[i][j] == 'S' or tree[i][j] == '|') and (tree[i + 1][j] != '^'):
            row = tree[i + 1]
            tree[i + 1] = row[:j] + '|' + row[j + 1:]
        elif tree[i][j] == '|' and tree[i + 1][j] == '^':
            row = tree[i + 1]
            row = row[:j + 1] + '|' + row[j + 2:]
            row = row[:j - 1] + '|' + row[j:]
            tree[i + 1] = row
            result += 1
    print(tree[i])

print(result)