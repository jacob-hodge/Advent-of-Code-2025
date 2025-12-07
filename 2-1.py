
with open("2.txt") as f:
    s = f.read()

ranges = s.split(',')
total = 0
for r in ranges:
    start_end = r.split('-')
    for x in range(int(start_end[0]), int(start_end[1]) + 1):
        if len(str(x)) % 2 == 0:
            half = int(len(str(x)) / 2)
            if str(x)[0:half] == str(x)[half:]:
                total += x

print(total)
