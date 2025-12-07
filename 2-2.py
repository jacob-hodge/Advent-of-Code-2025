with open("2.txt") as f:
    s = f.read()

ranges = s.split(',')
total = 0
for r in ranges:
    start_end = r.split('-')
    for x in range(int(start_end[0]), int(start_end[1]) + 1):
        s = str(x)
        for d in range(2, len(s) + 1):
            if len(s) % d == 0:
                chunk_size = len(s) // d
                parts = [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]
                if len(set(parts)) == 1:
                    total += x
                    break

print(total)
