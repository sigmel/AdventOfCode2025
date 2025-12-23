with open('Project9/puzzle.txt', 'r') as f:
    tiles = [list(map(int, line.strip().split(','))) for line in f]

area = 0
for i in range(0, len(tiles)-1):
    for j in range(i+1, len(tiles)):
        p0 = tiles[i]
        p1 = tiles[j]

        # only need the width and height, which are the distance between x and y
        w = abs(p0[0]-p1[0]) + 1
        h = abs(p0[1]-p1[1]) + 1

        a = w * h
        if a > area:
            area = a

print(area)