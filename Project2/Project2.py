with open('Project2/puzzle.txt', 'r') as f:
    text = f.read().split(',')

invalid_ids = []
for line in text:
    range_ids = line.split('-')

    for id in range(int(range_ids[0]), int(range_ids[1])+1):
        text_id = str(id)

        id_length = len(text_id)
        midpoint = id_length // 2
        for pattern_length in range(1, midpoint+1):
            if id_length % pattern_length != 0:
                continue

            pattern_chunks = [text_id[i:i+pattern_length] for i in range(0, id_length, pattern_length)]
            pattern_set = set(pattern_chunks)
            if len(pattern_set) == 1:
                invalid_ids.append(id)
                break

sum = 0
for invalid_id in invalid_ids:
    sum += invalid_id
print(sum)