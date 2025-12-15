unflipped = []
with open("6.txt") as f:
    for x in f:
        x = x.rstrip('\n')
        unflipped.append(x)

sums = [[]]
j = 0
for i in range(len(x)):
    digit1 = unflipped[0][len(x) - i - 1]
    digit2 = unflipped[1][len(x) - i - 1]
    digit3 = unflipped[2][len(x) - i - 1]
    digit4 = unflipped[3][len(x) - i - 1]

    if digit1 == digit2 == digit3 == digit4 == " ":
        j += 1
        sums.append([])
    else:
        numberToAdd = int(digit1 + digit2 + digit3 + digit4)
        sums[j].append(numberToAdd)
        if unflipped[4][len(x) - i - 1] != " ":
            sums[j].append(unflipped[4][len(x) - i - 1])

result = 0

for i in sums:
    if i[-1] == "*":
        toAdd = 1
        for j in range(len(i) - 1):
            toAdd *= int(i[j])
    else:
        toAdd = 0
        for j in range(len(i) - 1):
            toAdd += int(i[j])
    result += toAdd

print(result)
