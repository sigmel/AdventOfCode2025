with open('Project12/puzzle.txt', 'r') as f:
    text = [line.strip() for line in f]

read_grid = False
index = -1
shapes = []
grids = []
for line in text:
    if index < 0:
        if 'x' in line:
            read_grid =  True
        else:
            index = int(line.strip(':'))
            shapes.append([])
            continue
    elif len(line) > 0:
        shapes[-1].append(line)
    else:
        index = -1

    if read_grid:
        sections = line.split(' ')
        dimensions = [int(x) for x in sections[0].strip(':').split('x')]
        counts = [int(x) for x in sections[1:]]
        grids.append((dimensions, counts))

# gather the space each takes up to determine if we can possible fit these later
present_areas = []
for present in shapes:
    area = 0
    for line in present:
        for char in line:
            if char == '#':
                area += 1
    present_areas.append(area)

total = 0

# first determine which ones can't have a solution or have a trivial solution and eliminate those
for i in range(len(grids)-1, -1, -1):
    grid = grids[i]
    total_area = grid[0][0]*grid[0][1]

    num_presents = sum(grid[1])
    if num_presents * 9 <= total_area: # assuming that all presents don't need to overlap any
        grids.pop(i)
        total += 1
        continue

    present_area = 0
    for j, present_num in enumerate(grid[1]):
        present_area += present_areas[j] * present_num
    if present_area > total_area: # if the space presents need assuming perfect placement is greater than the grid, we can't fit them
        grids.pop(i)

# now I would normally calculate which ones can still work
# but it turns out I don't need to

print(total)
