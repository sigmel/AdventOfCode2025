with open('Project3/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

max_joltages = []
for line in text:
    max = []

    num_digits = 12
    line_length = len(line) + 1

    start = 0
    for digit_num in range(num_digits):
        max.append(line[start])

        new_start = start
        #print(line[start+1:line_length-num_digits+digit_num])
        for digit_index, digit in enumerate(line[start+1:line_length-num_digits+digit_num]):
            if int(digit) > int(max[-1]):
                max[-1] = digit
                new_start = start + digit_index + 1
        
        start = new_start + 1

    max_joltages.append(int(''.join(max)))

sum = 0
for joltage in max_joltages:
    sum += joltage
print(sum)