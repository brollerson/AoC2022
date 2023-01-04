class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


def euclidean_distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def move(direction, location):
    new_loc = location
    if direction == "U":
        new_loc = location + Point(0, 1)
    elif direction == "D":
        new_loc = location + Point(0, -1)
    elif direction == "R":
        new_loc = location + Point(1, 0)
    elif direction == "L":
        new_loc = location + Point(-1, 0)
    return new_loc


with open("input09") as f:
    data = f.read().splitlines()

last_log = []
H = Point(0, 0)
T = Point(0, 0)
rope_length = 10
rope = [Point(0, 0) for i in range(rope_length)]

for line in data:
    direction, dist = line[0], int(line[1:])
    for i in range(dist):
        for j, point in enumerate(rope):
            if j == 0:
                previous = rope[j]
                rope[j] = move(direction, rope[j])

            elif manhattan_distance(rope[j], rope[j - 1]) == 4:
                rope[j].x = (rope[j].x + rope[j - 1].x) // 2
                rope[j].y = (rope[j].y + rope[j - 1].y) // 2

            elif euclidean_distance(rope[j], rope[j - 1]) >= 2:
                if abs(rope[j].x - rope[j - 1].x) == 2:
                    rope[j].y = rope[j - 1].y
                    rope[j].x = (rope[j].x + rope[j - 1].x) // 2
                elif abs(rope[j].y - rope[j - 1].y) == 2:
                    rope[j].x = rope[j - 1].x
                    rope[j].y = (rope[j].y + rope[j - 1].y) // 2

            if j == len(rope) - 1:
                last_log.append((rope[j].x, rope[j].y))
        # print(rope)

print(len(set(last_log)))
