max_area = 0
coords = []
with open("9.txt") as f:
    for x in f:
        x = x.strip()
        coord = list(map(int, x.split(',')))
        coords.append(coord)

red = set((x, y) for x, y in coords)

edges = []
for i in range(len(coords)):
    x1, y1 = coords[i]
    x2, y2 = coords[(i + 1) % len(coords)]
    edges.append((x1, y1, x2, y2))

def point_in_polygon(px, py, polygon):
    cnt = 0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if y1 == y2:
            continue
        if py < min(y1, y2) or py >= max(y1, y2):
            continue
        xint = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
        if xint > px:
            cnt += 1
    return cnt % 2 == 1

def rectangle_inside_polygon(xmin, ymin, xmax, ymax, edges, polygon):
    for x1, y1, x2, y2 in edges:
        if x1 == x2:
            if xmin < x1 < xmax and not (ymax <= min(y1,y2) or ymin >= max(y1,y2)):
                return False
        else:
            if ymin < y1 < ymax and not (xmax <= min(x1,x2) or xmin >= max(x1,x2)):
                return False
    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2
    return point_in_polygon(cx, cy, polygon)

n = len(coords)
for i in range(n):
    x1, y1 = coords[i]
    for j in range(i + 1, n):
        x2, y2 = coords[j]
        if (x1, y1) not in red or (x2, y2) not in red:
            continue
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        if xmin == xmax or ymin == ymax:
            continue
        if rectangle_inside_polygon(xmin, ymin, xmax, ymax, edges, coords):
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            max_area = max(max_area, area)

print(max_area)
