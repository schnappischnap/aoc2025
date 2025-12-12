import re


def part_1(data):
    return sum(int(line[:2]) // 3 * int(line[3:5]) // 3 >= sum(int(i) for i in line[7:].split()) for line in data[30:])


if __name__ == "__main__":
    with open("12_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
