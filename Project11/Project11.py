with open('Project11/puzzle.txt', 'r') as f:
    text = [line.strip() for line in f]

nodes = {}
for line in text:
    in_outs = line.split(':')
    outs = in_outs[1].split()
    nodes[in_outs[0]] = outs

total = 0
path_stack = ["you"]
traversed_stack = []
while len(path_stack) > 0:
    curr_node = path_stack.pop()
    if curr_node == "out":
        total += 1
        continue

    for node in nodes[curr_node]:
        path_stack.append(node)

print(total)