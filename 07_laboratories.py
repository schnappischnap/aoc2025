from collections import Counter


def part_1(data):
    splits = 0
    beams = set([data[0].index("S")])
    for line in data[1:]:
        new_beams = set()
        for index in beams:
            if line[index] == "^":
                splits += 1
                new_beams.add(index - 1)
                new_beams.add(index + 1)
            else:
                new_beams.add(index)
        beams = new_beams
    return splits


def part_2(data):
    beams = Counter([data[0].index("S")])
    for line in data[1:]:
        new_beams = Counter()
        for index, count in beams.items():
            if line[index] == "^":
                new_beams[index - 1] += count
                new_beams[index + 1] += count
            else:
                new_beams[index] += count
        beams = new_beams
    return beams.total()
                

if __name__ == "__main__":
    with open("07_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
