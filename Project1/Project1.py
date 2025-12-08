dial = 50
password = 0

with open('Project1/puzzle.txt', 'r') as f:
    text = f.read().splitlines()

for line in text:
    dir = line[:1]
    count = int(line[1:])

    move = 1 if dir == 'R' else -1
    adjust = move * count

    # count how many full rotations we do
    password += abs(int(adjust / 100))
    adjust = int(abs(adjust) % 100) * move

    old_dial = dial
    dial += adjust

    # I wonder if you could do this without renormalizing to 0-99 range, but I bet
    # there are edge cases around 0 anyway, so just sticking with this
    if dial >= 100 or dial == 0 or \
        old_dial < 0 and dial > 0 or \
        dial < 0 and old_dial > 0:
        password += 1
    
    dial = dial % 100

print(password)