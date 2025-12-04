def part_1(data):
    answer = 0
    for y, line in enumerate(data):
        for x, character in enumerate(line):
            if character != "@":
                continue
            answer += sum(0 <= x + dx < len(line) and 
                          0 <= y + dy < len(data) and 
                          data[y+dy][x+dx] == "@"
                          for dx in range(-1, 2) for dy in range(-1, 2)) < 5
    return answer


def part_2(data):
    data = [list(line) for line in data]
    answer = 0
    while True:
        found_roll = False
        for y, line in enumerate(data):
            for x, character in enumerate(line):
                if character != "@":
                    continue
                if sum(0 <= x + dx < len(line) and 
                       0 <= y + dy < len(data) and 
                       data[y+dy][x+dx] == "@"
                       for dx in range(-1, 2) for dy in range(-1, 2)) < 5:
                    answer += 1
                    data[y][x] = "."
                    found_roll = True
        if not found_roll:
            break
    return answer


if __name__ == "__main__":
    with open("04_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
