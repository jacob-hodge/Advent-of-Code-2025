input = []
result = 0
with open("4.txt") as f:
    for x in f:
        x = x.strip()
        input.append(x)
nextInput = [list(row) for row in input]

def removeRolls():
    input = nextInput
    rollsOut = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            count = 0
            if input[i][j] == "@":
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        if (
                            0 <= i + dy < len(input) and
                            0 <= j + dx < len(input[0]) and
                            not (dx == 0 and dy == 0) and
                            input[i + dy][j + dx] == "@"
                        ):
                            count += 1
            if count <= 3 and input[i][j] == "@":
                rollsOut += 1
                nextInput[i][j] = "."
    return rollsOut

rollsRemoved = 1
while rollsRemoved > 0:
    rollsRemoved = removeRolls()
    result += rollsRemoved

    

print(result)