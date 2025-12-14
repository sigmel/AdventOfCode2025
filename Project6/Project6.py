with open('Project6/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

operations = text.pop().split()

numbers = [[]]
num_rows = len(text)
num_columns = len(text[0])
for i in range(num_columns - 1, -1, -1):
    num = ''
    for c in range(0, num_rows):
        num += text[c][i]
    
    num = num.strip()
    if len(num) > 0:
        numbers[-1].append(int(num))
    else:
        numbers.append([])

total = 0
for op_index, op in enumerate(reversed(operations)):
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