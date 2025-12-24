with open('Project9/puzzle.txt', 'r') as f:
    tiles = [list(map(int, line.strip().split(','))) for line in f]

def cross(p0, p1):
    return p0[0]*p1[1] - p0[1]*p1[0]

def orient(a, b, c):
    return cross([b[0]-a[0], b[1]-a[1]], [c[0]-a[0], c[1]-a[1]])

def lineLineIntersects(a, b, c, d):
    oa = orient(c, d, a)
    ob = orient(c, d, b)
    oc = orient(a, b, c)
    od = orient(a, b, d)

    return oa*ob < 0 and oc*od < 0

area = 0
for i in range(0, len(tiles)-1):
    for j in range(i+1, len(tiles)):
        p0 = list(map(float, tiles[i]))
        p1 = list(map(float, tiles[j]))

        # only need the width and height, which are the distance between x and y
        w = abs(p0[0]-p1[0]) + 1
        h = abs(p0[1]-p1[1]) + 1

        if w == 1 or h == 1:
            continue # no chance a straight line will win, so skip further checks
        
        # compute the four corners of our rectangle
        # cheat slightly by moving them towards the center so we register the points inside correctly
        corners = []
        corners.append([min(p0[0], p1[0]) + 0.5, min(p0[1], p1[1]) + 0.5])
        corners.append([max(p0[0], p1[0]) - 0.5, min(p0[1], p1[1]) + 0.5])
        corners.append([min(p0[0], p1[0]) + 0.5, max(p0[1], p1[1]) - 0.5])
        corners.append([max(p0[0], p1[0]) - 0.5, max(p0[1], p1[1]) - 0.5])

        # see if all four line segments don't intersect
        inside = True
        for c in range(len(corners) - 1, -1, -1):
            for t in range(len(tiles) - 1, -1, -1):
                if lineLineIntersects(corners[c], corners[c-1], tiles[t], tiles[t-1]):
                    inside = False
                    break
            
            if not inside:
                break


        if inside:
            a = w * h
            if a > area:
                area = a

print(int(area))