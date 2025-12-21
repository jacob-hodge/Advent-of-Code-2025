unflipped = []
with open("6.txt") as f:
    for x in f:
        unflipped.append(x.split())

flipped = [list(row) for row in zip(*unflipped)]
result = 0

for i in flipped:
    if i[4] == "*":
        toAdd = 1
        for j in range(4):
            toAdd *= int(i[j])
    else:
        toAdd = 0
        for j in range(4):
            toAdd += int(i[j])
    result += toAdd

print(result)
