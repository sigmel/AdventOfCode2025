with open('Project2/puzzle.txt', 'r') as f:
    text = f.read().split(',')

invalid_ids = []
for line in text:
    range_ids = line.split('-')

    for id in range(int(range_ids[0]), int(range_ids[1])+1):
        text_id = str(id)

        # can likely optimize by incrementing to next range that can be split
        id_length = len(text_id)
        if id_length % 2 == 0:
            midpoint = id_length // 2
            right, left = text_id[:midpoint], text_id[midpoint:]
            if right == left:
                invalid_ids.append(id)

sum = 0
for invalid_id in invalid_ids:
    sum += invalid_id
print(sum)