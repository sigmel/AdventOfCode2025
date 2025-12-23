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

circuits = []
num_connections = 1000
for connection in range(0, num_connections):
    pair = sorted_pairs[connection]
    # see if either of the two points are already in a circuit
    circuit0 = findContainingCircuit(pair[0], circuits)
    circuit1 = findContainingCircuit(pair[1], circuits)

    # if they aren't, then add a new circuit
    if circuit0 == None and circuit1 == None:
        circuits.append(set([pair[0], pair[1]]))
        continue

    if circuit0 != None:
        circuit0.update([pair[0], pair[1]])
    if circuit1 != None:
        circuit1.update([pair[0], pair[1]])

    # if we are in two different junctions, then we should combine them
    if circuit0 != None and circuit1 != None and circuit0 != circuit1:
        circuit0.update(circuit1)
        circuits.remove(circuit1)
        continue
    
sorted_circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)

key = len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])
print(key)