ranges = []
with open("5.txt") as f:
    for x in f:
        x = x.strip()
        ranges.append(x.split('-'))

ranges = [[int(start), int(end)] for start, end in ranges]

ranges.sort(key=lambda x: x[0])

merged = []

for start, end in ranges:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
total = 0

for m in merged:
    total += m[1] - m[0] + 1
print(total)