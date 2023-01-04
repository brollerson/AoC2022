with open("input2") as f:
    data = f.read().splitlines()


def rps(a, b):
    if a == b:
        return 3
    elif a == "A" and b == "B":
        return 6
    elif a == "B" and b == "C":
        return 6
    elif a == "C" and b == "A":
        return 6
    else:
        return 0


def shape_score(code):
    return ord(code) - 64


def convert_code(code):
    code = code.replace("X", "A")
    code = code.replace("Y", "B")
    code = code.replace("Z", "C")
    return code


def make_tuple(line):
    new_line = line.split(" ")
    # new_line[1] = convert_code(new_line[1])
    return tuple(new_line)


# A = rock, B = paper, C = scissors
def choose_result(a, b):
    if b == "Y":
        return a, a
    elif b == "Z":
        if a == "A":
            return a, "B"
        elif a == "B":
            return a, "C"
        elif a == "C":
            return a, "A"
    else:
        if a == "A":
            return a, "C"
        elif a == "B":
            return a, "A"
        elif a == "C":
            return a, "B"


score = 0
for line in data:
    new_line = make_tuple(line)
    new_line = choose_result(*new_line)
    score += rps(*new_line)
    score += shape_score(new_line[1])

print(score)
