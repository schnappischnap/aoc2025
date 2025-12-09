import itertools


def part_1(data):
    reds = [tuple(map(int, line.split(","))) for line in data]
    return max((abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
               for t1, t2 in itertools.combinations(reds, 2))


def part_2(data):
    reds = [tuple(map(int, line.split(","))) for line in data]
    reds.append(reds[0])
    answer = 0
    for (x1, y1), (x2, y2) in itertools.combinations(reds, 2):
        left, right = min(x1, x2), max(x1, x2)
        top, bottom = min(y1, y2), max(y1, y2)
        for (lx1, ly1), (lx2, ly2) in zip(reds, reds[1:]):
            if not (max(lx1, lx2) <= left or right <= min(lx1, lx2) or
                    max(ly1, ly2) <= top or bottom <= min(ly1, ly2)):
                break
        else:
            answer = max(answer, (right - left + 1) * (bottom - top + 1))
    return answer


if __name__ == "__main__":
    with open("09_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
