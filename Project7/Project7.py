with open('Project7/puzzle.txt', 'r') as f:
    text = [list(line.strip()) for line in f]

beams = [] # (col, start_row, end_row)

# start with our starting spot
spawns = [(0, text[0].index('S'))]

split = 0

def add_beam(beam):
    beams.append(beam)

    for i in range(beam[1], beam[2]):
        text[i][beam[0]] = '|'
    
    #for line in text:
    #    print(''.join(line))

while len(spawns) > 0:
    spawn = spawns.pop()

    col = spawn[1]
    start = spawn[0]
    end = start + 1
    
    # see how far down we can go
    while end < len(text) and text[end][col] != '^':
        end += 1

    # see if we are a duplicate
    duplicate = False
    for beam in beams:
        if beam[0] == col and beam[2] == end:
            if beam[1] > start: # we want to take the longer beam
                beams.remove(beam)
                add_beam((col, start, end))
            duplicate = True
            break

    if duplicate:
        continue

    # otherwise, add as a valid beam
    add_beam((col, start, end))

    # if we hit a splitter we need to split
    if end < len(text) and text[end][col] == '^':
        spawns.append((end, col-1))
        spawns.append((end, col+1))
        split += 1

print(split)