max_area = 0
coords = []
with open("9.txt") as f:
    for x in f:
        x = x.strip()
        coord = x.split(',')
        for c in range(len(coord)):
            coord[c] = int(coord[c])
        
        coords.append(coord)

for i in range(len(coords)):
    for j in range(len(coords)):
        max_area = max( (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1), max_area)

print(max_area)