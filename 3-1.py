result = 0
with open("3.txt") as f:
    for x in f:
        rowMax = 11
        for a in range(0,len(x) - 1):
            for b in range(a + 1, len(x)):
                rowMax = max(rowMax, int(x[a] + x[b]))
        result += rowMax
print(result)