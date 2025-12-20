with open('Project7/puzzle.txt', 'r') as f:
    text = [list(line.strip()) for line in f]

paths = [0 for _ in range(0, len(text[0]))]

# start with our starting spot
paths[text[0].index('S')] = 1

# check each column, if we hit a ^ then all paths go to the side col values
for row, line in enumerate(text):
    for col, path in enumerate(paths):
        if text[row][col] == '^':
            paths[col-1] += paths[col]
            paths[col+1] += paths[col]
            paths[col] = 0

sum = 0
for path in paths:
    sum += path
print(sum)
