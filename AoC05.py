from collections import defaultdict

with open("input05") as f:
    data = f.read().splitlines()

crates = data[:9]  # 9
moves = data[10:]  # 10


# positions = 1, 5, 9, 13, 17, 21, 25, 29, 33

crates_dict = defaultdict(list)

for line in crates[:-1]:
    for i, index in enumerate(range(1, len(line), 4)):
        if line[index] != " ":
            crates_dict[i + 1].append(line[index])

# for i in range(1, len(crates_dict) + 1):
#     crates_dict[i].reverse()
#     print(crates_dict[i])
# print(" ")

for line in moves:
    nums = [int(i) for i in line.split(" ") if i.isdigit()]
    # for i in range(nums[0]):
    #     crates_dict[nums[2]].append(crates_dict[nums[1]].pop())

    out = crates_dict[nums[1]][: nums[0]]
    # out.reverse()
    crates_dict[nums[1]] = crates_dict[nums[1]][nums[0] :]
    crates_dict[nums[2]] = out + crates_dict[nums[2]]


answer = ""
for i in range(1, len(crates_dict) + 1):
    answer += crates_dict[i][0]

for i in range(1, len(crates_dict) + 1):
    print(crates_dict[i])


print(answer)
