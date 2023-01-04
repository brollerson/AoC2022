with open("input10") as f:
    data = f.read().splitlines()

# print(data[:20])

cycle = 0
X = 1
test_points = [20, 60, 100, 140, 180, 220]
signal_strengths = []
CRT = []
for row in range(6):
    for col in range(40):
        CRT.append("MM")

for i in range(len(CRT)):
    print(CRT[i], end="\n" if i % 40 == 39 else "")

for i, line in enumerate(data):
    cycle += 1
    if cycle in test_points:
        signal_strengths.append(cycle * X)
    if line == "noop":
        # print(f"{cycle}: {cycle % 40}: {X}")
        target = cycle % 40
        print(target)
        window = [target - 1, target, target + 1]
        if X in window:
            CRT[cycle - 1] = "██"
        else:
            CRT[cycle - 1] = "░░"
        # pass
    else:
        instruction, value = line.split(" ")
        # print(f"{cycle}: {line}: {X}")
        target = cycle % 40
        print(target)
        window = [target - 1, target, target + 1]
        if X in window:
            CRT[cycle - 1] = "██"
        else:
            CRT[cycle - 1] = "░░"
        cycle += 1
        target = cycle % 40
        print(target)
        window = [target - 1, target, target + 1]
        if X in window:
            CRT[cycle - 1] = "██"
        else:
            CRT[cycle - 1] = "░░"
        if cycle in test_points:
            # print(f"{cycle}: {X}")
            signal_strengths.append(cycle * X)
        X += int(value)
        # print(f"{cycle}: {line}: {X}")
        target = cycle % 40
        window = [target - 1, target, target + 1]
        if X in window:
            CRT[cycle - 1] = "██"
        else:
            CRT[cycle - 1] = "░░"


print(signal_strengths, sum(signal_strengths))

for i in range(len(CRT)):
    print(CRT[i], end="\n" if i % 40 == 39 else "")


# code = """##..##..##..##..##..##..##..##..##..##..
# ###...###...###...###...###...###...###.
# ####....####....####....####....####....
# #####.....#####.....#####.....#####.....
# ######......######......######......####
# #######.......#######.......#######....."""

# print(code)
# import re

# code = re.sub(r"\.", "░░", code)
# code = re.sub(r"#", "██", code)
# print(code)
