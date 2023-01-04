with open("input03") as f:
    data = f.read().splitlines()


def part_one(data):
    score = 0
    for line in data:
        len_line = int(len(line) / 2)
        first = set(list(line[:len_line]))
        second = set(list(line[len_line:]))
        common_item = list(first & second)[0]
        score += get_priority(common_item)
        # if common_item.islower():
        #     score += ord(common_item) - 96

        # else:
        #     score += ord(common_item) - 38

    return score


def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def part_two(data):
    score = 0
    chunks = [data[i : i + 3] for i in range(0, len(data), 3)]
    for chunk in chunks:
        first = set(list(chunk[0]))
        second = set(list(chunk[1]))
        third = set(list(chunk[2]))
        common_item = list(first & second & third)[0]
        score += get_priority(common_item)
    return score


print(part_two(data))
