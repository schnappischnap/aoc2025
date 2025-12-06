import operator as op
import functools
import itertools


def part_1(data):
    operators = {"+": op.add, "*": op.mul}
    return sum(functools.reduce(operators[operation[-1]], map(int, operation[:-1])) 
               for operation in zip(*[line.split() for line in data]))


def part_2(data):
    operands = ["".join(a) for a in zip(*data[:-1]) ]
    operators = [{"+": op.add, "*": op.mul}[s] for s in data[-1].split()]

    answer = 0
    numbers = []
    i = 0
    for operand in operands:
        if operand.isspace():
            answer += functools.reduce(operators[i], numbers)
            numbers = []
            i += 1
        else:
            numbers.append(int(operand))
    return answer
                

if __name__ == "__main__":
    with open("06_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
