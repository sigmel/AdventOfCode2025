with open('Project5/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

fresh = []
for line in text:
    if len(line) == 0:
        break

    range_values = list(int(num) for num in line.split('-'))

    # find the unique range value
    for fresh_range in fresh:
        if range_values[0] >= fresh_range[0] and range_values[0] < fresh_range[1]:
            range_values[0] = fresh_range[1]
        if range_values[1] <= fresh_range[1] and range_values[1] > fresh_range[0]:
            range_values[1] = fresh_range[0]
            
    if range_values[0] <= range_values[1]:
        fresh.append(range_values)

    # sort our ranges
    fresh.sort()

    # see if we can combine any
    for fresh_index in range(len(fresh) - 2, -1, -1):
        if fresh[fresh_index][1] == fresh[fresh_index+1][0]:
            fresh[fresh_index][1] = fresh[fresh_index+1][1]
            fresh.pop(fresh_index+1)

        # see if this encompasses any of the prior ranges
        for compare_index in range(len(fresh) - 1, fresh_index, -1):
            if fresh[fresh_index][0] <= fresh[compare_index][0] and \
                 fresh[fresh_index][1] >= fresh[compare_index][1]:
                fresh.pop(compare_index)

total = 0
for fresh_range in fresh:
    total += fresh_range[1]+1 - fresh_range[0]
print(total)