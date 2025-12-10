import scipy


def part_1(data):
    def bfs(initial_state, goal, buttons):
        seen = set([initial_state])
        queue = [(initial_state, 0)]
        while queue:
            diagram, steps = queue.pop(0)
            if diagram == goal:
                return steps
            for button in buttons:
                new_state = tuple(not b if i in button else b for i, b in enumerate(diagram))
                if new_state not in seen:
                    queue.append((new_state, steps + 1))
                    seen.add(new_state)

    answer = 0
    for line in data:
        diagram, *buttons, _ = line.split()
        diagram = tuple(c == "#" for c in diagram[1:-1])
        buttons = [tuple(map(int, s[1:-1].split(","))) for s in buttons]
        answer += bfs(tuple([False]) * len(diagram), diagram, buttons)
    return answer


def part_2(data):
    answer = 0
    for line in data:
        _, *buttons, joltages = line.split()
        buttons = sorted([tuple(map(int, s[1:-1].split(","))) for s in buttons], key=sum, reverse=True)
        joltages = tuple(map(int, joltages[1:-1].split(",")))
        c = [1] * len(buttons)
        A = [[i in b for b in buttons] for i in range(len(joltages))]
        answer += scipy.optimize.milp(c, integrality=c, constraints=[A, joltages, joltages]).fun
    return int(answer)


if __name__ == "__main__":
    with open("10_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
