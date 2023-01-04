with open("input06") as f:
    data = f.read().strip()

# data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
window = []
count = 0
while len(window) < 14:
    window.append(data[count])
    count += 1

print(window, count)

while len(set(window)) != 14:
    window.pop(0)
    window.append(data[count])
    count += 1

print(window, count)
