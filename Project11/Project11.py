with open('Project11/puzzle.txt', 'r') as f:
    text = [line.strip() for line in f]

nodes = {}
for line in text:
    in_outs = line.split(':')
    outs = in_outs[1].split()
    nodes[in_outs[0]] = outs

cache = {}

def search_nodes(curr_node, has_dac, has_fft):
    global nodes
    global cache

    if curr_node == 'out':
        return 1 if has_dac and has_fft else 0

    total = 0
    for node in nodes[curr_node]:
        key = (node, has_dac, has_fft)
        if key in cache:
            total += cache[key]
        else:        
            pass_dac = True if has_dac or node == 'dac' else False
            pass_fft = True if has_fft or node == 'fft' else False

            result = search_nodes(node, pass_dac, pass_fft)
            total += result
            cache[key] = result
    return total

total = search_nodes('svr', False, False)
print(total)