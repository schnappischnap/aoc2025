import functools


def part_1(data):
    devices = {line[:3]: list(line[5:].split()) for line in data}

    def dfs(device):
        if device == "out":
            return 1
        return sum(dfs(output) for output in devices[device])
    
    return dfs("you")


def part_2(data):
    devices = {line[:3]: list(line[5:].split()) for line in data}

    @functools.cache
    def dfs(device, dac=False, fft=False):
        if device == "dac":
            dac = True
        elif device == "fft":
            fft = True
        elif device == "out":
            return dac and fft
        return sum(dfs(output, dac, fft) for output in devices[device])

    return dfs("svr")


if __name__ == "__main__":
    with open("11_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
