with open("input", "rb") as fin:
    data = fin.read().decode("utf-8").splitlines()

sums = []
calories = 0
count = 1
for i, line in enumerate(data):
    if line == "":
        sums.append(calories)
        calories = 0
        count += 1
    else:
        calories += int(line)

s_sums = sorted(sums)
print(sum(s_sums[-3:]))
