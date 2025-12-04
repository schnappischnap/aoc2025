def part_1(data):
    return sum(int(max(bank[:-1]) + max(bank[bank.index(max(bank[:-1])) + 1:])) for bank in data)


def part_2(data):
    max_joltage = 0
    for bank in data:
        joltage = max(bank[:-11])
        start = bank.index(joltage) + 1
        for i in range(-10, 0):
            joltage += max(bank[start:i])
            start += bank[start:i].index(max(bank[start:i])) + 1
        joltage += max(bank[start:])
        max_joltage += int(joltage)
    return max_joltage


if __name__ == "__main__":
    with open("03_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp))) 