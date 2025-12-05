def part_1(data):
    ranges, available = data.split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in ranges.splitlines()]
    return sum(any(i <= int(ingredient) <= j for i, j in ranges) 
               for ingredient in available.splitlines())


def part_2(data):
    ranges = set([tuple(map(int, line.split("-"))) for line in data.split("\n\n")[0].splitlines()])
    while True:
        new_ranges = set()
        for (start1, stop1) in ranges:
            for (start2, stop2) in ranges:
                if (start1, stop1) == (start2, stop2):
                    continue
                if max(start1, start2) <= min(stop1, stop2):
                    new_ranges.add((min(start1, start2), max(stop1, stop2)))
                    break
            else:
                new_ranges.add((start1, stop1))
        if ranges == new_ranges:
            return sum(stop - start + 1 for start, stop in ranges)
        ranges = new_ranges
                

if __name__ == "__main__":
    with open("05_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
