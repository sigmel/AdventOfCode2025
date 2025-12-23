import math

with open('Project8/puzzle.txt', 'r') as f:
    points = [list(map(float, line.strip().split(','))) for line in f]

def computeDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

# find all the distances
pairs = []
for i in range(0, len(points) - 1):
    for j in range(i+1, len(points)):
        distance = computeDistance(points[i], points[j])
        pairs.append((tuple(points[i]), tuple(points[j]), distance))

sorted_pairs = sorted(pairs, key=lambda pair: pair[2])

def findContainingCircuit(point, circuits):
    for circuit in circuits:
        if point in circuit:
            return circuit
    return None

circuits = [set([tuple(point)]) for point in points]
num_connections = len(sorted_pairs)
last_connection = []
for connection in range(0, num_connections):
    pair = sorted_pairs[connection]
    circuit0 = findContainingCircuit(pair[0], circuits)
    circuit1 = findContainingCircuit(pair[1], circuits)

    circuit0.update([pair[0], pair[1]])
    circuit1.update([pair[0], pair[1]])

    if circuit0 == circuit1:
        if circuit0 is not circuit1:
            # remove duplicate circuits
            circuits.remove(circuit1)
    else:
        # if we are in two different junctions, then we should combine them
        circuit0.update(circuit1)
        circuits.remove(circuit1)
    
    if len(circuits) == 1:
        last_connection = [pair[0], pair[1]]
        break
    
key = int(last_connection[0][0]) * int(last_connection[1][0])
print(key)