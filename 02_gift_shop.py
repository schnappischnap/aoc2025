def part_1(data):
    id_ranges = data[0].split(",")
    answer = 0
    for id_range in id_ranges:
        start, stop = (int(i) for i in id_range.split("-"))
        for id in range(start, stop + 1):
            str_id = str(id)
            if len(str_id) % 2 == 0 and str_id[len(str_id)//2:] == str_id[:len(str_id)//2]:
                answer += id
    return answer


def part_2(data):
    id_ranges = data[0].split(",")
    answer = 0
    for id_range in id_ranges:
        start, stop = (int(i) for i in id_range.split("-"))
        for id in range(start, stop + 1):
            str_id = str(id)
            for slice_length in range(1, len(str_id) // 2 + 1):
                if len(str_id) % slice_length == 0:
                    if str_id == str_id[:slice_length] * (len(str_id) // slice_length):
                        answer += id
                        break
    return answer


if __name__ == "__main__":
    with open("02_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp))) 