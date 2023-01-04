import numpy as np

with open("input08") as f:
    data = f.read().splitlines()

width = len(data[0])
height = len(data)

matrix = np.zeros((height, width), dtype=int)
bools = np.zeros((height, width), dtype=bool)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        matrix[i, j] = int(char)


def check_left(i, j):
    target = matrix[i, j]
    for k in range(0, j):
        if matrix[i, k] >= target:
            return False
    return True


def check_right(i, j):
    target = matrix[i, j]
    for k in range(j + 1, width):
        if matrix[i, k] >= target:
            return False
    return True


def check_up(i, j):
    target = matrix[i, j]
    for k in range(0, i):
        if matrix[k, j] >= target:
            return False
    return True


def check_down(i, j):
    target = matrix[i, j]
    for k in range(i + 1, height):
        if matrix[k, j] >= target:
            return False
    return True


for i in range(height):
    for j in range(width):
        bools[i, j] = (
            check_left(i, j) or check_right(i, j) or check_up(i, j) or check_down(i, j)
        )

print(bools.sum())

count_matrix = np.zeros((height, width), dtype=int)


def count_left(i, j):
    target = matrix[i, j]
    count = 1
    for k in range(j - 1, 0, -1):
        if matrix[i, k] >= target:
            return count
        elif k == 0:
            return count
        count += 1
    return count


def count_right(i, j):
    target = matrix[i, j]
    count = 1
    for k in range(j + 1, width):
        if matrix[i, k] >= target:
            return count
        elif k == width - 1:
            return count
        count += 1
    return count


def count_up(i, j):
    target = matrix[i, j]
    count = 1
    for k in range(i - 1, 0, -1):
        if matrix[k, j] >= target:
            return count
        elif k == 0:
            return count
        count += 1
    return count


def count_down(i, j):
    target = matrix[i, j]
    count = 1
    for k in range(i + 1, height):
        if matrix[k, j] >= target:
            return count
        elif k == height - 1:
            return count
        count += 1
    return count


for i in range(height):
    for j in range(width):
        count_matrix[i, j] = (
            count_left(i, j) * count_right(i, j) * count_up(i, j) * count_down(i, j)
        )

print(count_matrix[97, 6])
print(count_left(97, 6))
print(count_right(97, 6))
print(count_up(97, 6))
print(count_down(97, 6))

print(count_matrix.max())
