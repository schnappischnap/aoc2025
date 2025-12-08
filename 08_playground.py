import itertools
import math


def part_1(data):
    junctions = [tuple(map(int, line.split(","))) for line in data]
    pairs = sorted(((a, b) for a, b in itertools.combinations(junctions, 2)), 
                   key=lambda x: (x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2 + (x[0][2] - x[1][2]) ** 2)
    circuits = []
    for junction1, junction2 in pairs[:1000]:
        circuit1 = None
        circuit2 = None
        for circuit in circuits:
            if junction1 in circuit and junction2 in circuit:
                break
            if junction1 in circuit:
                circuit1 = circuit
            if junction2 in circuit:
                circuit2 = circuit
        else:
            if circuit1 and circuit2:
                circuit1.update(circuit2)
                circuits.remove(circuit2)
            elif circuit1:
                circuit1.add(junction2)
            elif circuit2:
                circuit2.add(junction1)
            else:
                circuits.append(set([junction1, junction2]))
    return math.prod(len(circuit) for circuit in sorted(circuits, key=len, reverse=True)[:3])


def part_2(data):
    junctions = [tuple(map(int, line.split(","))) for line in data]
    pairs = sorted(((a, b) for a, b in itertools.combinations(junctions, 2)), 
                   key=lambda x: (x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2 + (x[0][2] - x[1][2]) ** 2)
    circuits = []
    for junction1, junction2 in pairs:
        circuit1 = None
        circuit2 = None
        for circuit in circuits:
            if junction1 in circuit and junction2 in circuit:
                break
            if junction1 in circuit:
                circuit1 = circuit
            if junction2 in circuit:
                circuit2 = circuit
        else:
            if circuit1 and circuit2:
                if circuit1 == circuit2:
                    continue
                circuit1.update(circuit2)
                circuits.remove(circuit2)
            elif circuit1:
                circuit1.add(junction2)
            elif circuit2:
                circuit2.add(junction1)
            else:
                circuits.append(set([junction1, junction2]))
        if len(circuits[0]) == 1000:
            return junction1[0] * junction2[0]                


if __name__ == "__main__":
    with open("08_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
