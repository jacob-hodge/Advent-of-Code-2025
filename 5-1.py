ranges = []
fruits = []
with open("5.txt") as f:
    for x in f:
        x = x.strip()
        if '-' in x:
            ranges.append(x.split('-'))
        else:
            fruits.append(x)

fruits.pop(0)
result = 0

def freshCheck(f):
    for r in ranges:
        if int(r[0]) <= int(f) <= int(r[1]):
            return True
    return False

for f in fruits:
    if freshCheck(f):
        result += 1
print(result)