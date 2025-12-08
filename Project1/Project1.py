dial = 50
password = 0

with open('Project1/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

for line in text:
    dir = line[:1]
    count = int(line[1:])

    move = 1 if dir == 'R' else -1

    dial += move * count

    dial = dial % 100

    if  dial == 0:
        password += 1

print(password)