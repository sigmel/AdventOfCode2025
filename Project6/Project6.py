with open('Project6/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

operations = text.pop().split()

numbers = []
for line in text:
    numbers.append([int(value) for value in line.split()])

# transpose our array to make it easier to parse
numbers = list(zip(*numbers))

total = 0
for op_index, op in enumerate(operations):
    if op == '*':
        sum = 1
        for num in numbers[op_index]:
            sum *= num
        total += sum
    elif op == '+':
        sum = 0
        for num in numbers[op_index]:
            sum += num
        total += sum

print(total)