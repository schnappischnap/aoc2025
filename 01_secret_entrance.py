def part_1(data):
    positions = [50]
    for line in data:
        positions.append(positions[-1] + int(line[1:]) * (-1 if line[0] == "L" else 1))
    return sum(p % 100 == 0 for p in positions)


def part_2(data):
    position = 50
    password = 0
    for line in data:
        for i in range(int(line[1:])):
            position += (-1 if line[0] == "L" else 1)
            if position % 100 == 0:
                password += 1
    return password


if __name__ == "__main__":
    with open("01_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp))) 