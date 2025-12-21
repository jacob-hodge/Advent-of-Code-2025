coords = []
with open("8.txt") as f:
    for x in f:
        x = x.strip()
        coord = x.split(',')
        for c in range(len(coord)):
            coord[c] = int(coord[c])
        coords.append(coord)

distances = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        dist = (
            (coords[i][0] - coords[j][0])**2 +
            (coords[i][1] - coords[j][1])**2 +
            (coords[i][2] - coords[j][2])**2
        ) ** 0.5
        distances.append([i, j, dist])

distances.sort(key= lambda distance : distance[2])

circuits = []
for c in range(1000):
    circuits.append([c])

for j in range(1000):
    index1 = distances[j][0]
    index2 = distances[j][1]
    found1 = False
    found2 = False
    index1_loc = 0
    index2_loc = 0
    c = 0
    while not found1 or not found2:
        if index1 in circuits[c]:
            index1_loc = c
            found1 = True
        if index2 in circuits[c]:
            index2_loc = c
            found2 = True
        c += 1
    if index1_loc != index2_loc:
        circuits.append(circuits[index1_loc] + circuits[index2_loc])
        hi = max(index1_loc, index2_loc)
        lo = min(index1_loc, index2_loc)

        circuits.pop(hi)
        circuits.pop(lo)
lengths = []
for c in circuits:
    lengths.append(len(c))
lengths.sort()
print(lengths[-1]*lengths[-2]*lengths[-3])