with open("input04") as f:
    data = f.read().splitlines()


def tidy_data(line):
    line = line.split(",")
    line[0] = [int(num) for num in line[0].split("-")]
    line[1] = [int(num) for num in line[1].split("-")]
    return line


def compare(list1, list2):
    if list2[0] <= list1[0] <= list2[1]:
        return True
    elif list2[0] <= list1[1] <= list2[1]:
        return True
    elif list1[0] <= list2[0] <= list1[1]:
        return True
    elif list1[0] <= list2[1] <= list1[1]:
        return True
    else:
        return False


score = 0
for line in data:
    new_line = tidy_data(line)
    if compare(new_line[0], new_line[1]):
        score += 1


print(score)

# sample1 = "6-6,4-6"
# sample2 = "2-8,3-7"

# S1 = tidy_data(sample1)
# S2 = tidy_data(sample2)
# print(compare(S1[0], S1[1]))
# print(compare(S1[1], S1[0]))
# print(compare(S2[0], S2[1]))
# print(compare(S2[1], S2[0]))
