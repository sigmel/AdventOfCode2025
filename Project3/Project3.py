with open('Project3/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

max_joltages = []
for line in text:
    max = 0

    for i,first in enumerate(line[:-1]):
        for second in line[i+1:]:
            combine = int(first + second)
            if combine > max:
                max = combine

    max_joltages.append(max)

sum = 0
for joltage in max_joltages:
    sum += joltage
print(sum)