with open("input12_test") as f:
    data = f.read().splitlines()
    data = [list(line.split()[0]) for line in data]


def find_S_or_E(data, letter):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == letter:
                return i, j


def find_neighbours(data, i, j):
    """find only neighbours which are within plus
    or minus one of the current value"""
    neighbours = []
    if i > 0:
        if data[i][j] - 1 <= data[i - 1][j] <= data[i][j] + 1:
            neighbours.append((i - 1, j))
    if i < len(data) - 1:
        if data[i][j] - 1 <= data[i + 1][j] <= data[i][j] + 1:
            neighbours.append((i + 1, j))
    if j > 0:
        if data[i][j] - 1 <= data[i][j - 1] <= data[i][j] + 1:
            neighbours.append((i, j - 1))
    if j < len(data[i]) - 1:
        if data[i][j] - 1 <= data[i][j + 1] <= data[i][j] + 1:
            neighbours.append((i, j + 1))
    return neighbours


def convert_to_int(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                data[i][j] = 1
            elif data[i][j] == "E":
                data[i][j] = 26
            else:
                data[i][j] = ord(data[i][j]) - 96
    return data


start = find_S_or_E(data, "S")
end = find_S_or_E(data, "E")
data = convert_to_int(data)
data_dict = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        data_dict[(i, j)] = find_neighbours(data, i, j)

print(data_dict)
