with open('Project5/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

ranges = []
check_range = False

fresh = 0
for line in text:
    if len(line) == 0:
        check_range = True
        continue # we found our blank line separator, so switch to evaluation

    if not check_range:
        ranges.append([int(num) for num in line.split('-')])
    else:
        value = int(line)
        for range in ranges:
            if value >= range[0] and value <= range[1]:
                fresh += 1
                break # we're fresh, no need to check more

print(fresh)