import numpy as np


class Monkey:
    def __init__(
        self, name, items, operation, operation_factor, test, test_true, test_false
    ):
        self.name = name
        self.items = items
        self.operation = operation
        self.operation_factor = operation_factor
        self.test = test
        self.test_true = int(test_true)
        self.test_false = int(test_false)
        self.inspections = 0

    def items_add(self, item):
        self.items.append(item)

    def has_items(self):
        if len(self.items) > 0:
            return True
        else:
            return False

    def operate(self, item):
        if self.operation_factor == "old":
            factor = item
        else:
            factor = int(self.operation_factor)
        if self.operation == "+":
            item += factor
        elif self.operation == "*":
            item *= factor
        return item

    def get_and_inspect_item(self, worry):
        old = self.items.pop(0)
        new = self.operate(old)  # // 3
        if new > worry:
            new %= worry
        self.inspections += 1
        return new

    def test_item(self, item):
        if item % self.test == 0:
            return self.test_true
        else:
            return self.test_false

    def __repr__(self):
        return f"{self.name}, {self.items}, {self.operation}, {self.operation_factor}, {self.test}, {self.test_true}, {self.test_false}"


with open("input11") as f:
    data = f.read().splitlines()

data.append("\n")

# Create the monkeys
monkeys = []
for line in data:
    if line.startswith("Monkey"):
        name = line.split(":")[0]
        # print(name)
    elif line.startswith("  Starting items:"):
        items = [int(item) for item in line.split(":")[1].split(",")]
        # print(items)
    elif line.startswith("  Operation:"):
        operation, operation_factor = line.split(":")[1].split()[-2:]
        # print(operation, operation_factor)
    elif line.startswith("  Test:"):
        test = int(line.split(":")[1].split(" ")[-1:][0])
        # print(test)
    elif line.startswith("    If true:"):
        test_true = line.split(":")[1][-1:][0]
        # print(test_true)
    elif line.startswith("    If false:"):
        test_false = line.split(":")[1][-1:][0]
        # print(test_false)
    else:
        # elif line == "":
        monkeys.append(
            Monkey(
                name=name,
                items=items,
                operation=operation,
                operation_factor=operation_factor,
                test=test,
                test_true=test_true,
                test_false=test_false,
            )
        )
# print([(monkey.name, monkey.items) for monkey in monkeys])

# Run the monkeys
rounds = 10000
worry = np.prod(np.array([monkey.test for monkey in monkeys]))

for i in range(rounds):
    for monkey in monkeys:
        # print(monkey.name)
        while monkey.has_items():
            item = monkey.get_and_inspect_item(worry)
            # print(item)
            new_monkey = monkey.test_item(item)
            monkeys[new_monkey].items_add(item)
    # print([(monkey.name, monkey.items) for monkey in monkeys])
    inspect_counts = sorted([(monkey.inspections) for monkey in monkeys])
    print(i)
    # print([monkey.items for monkey in monkeys])
    print([(monkey.inspections) for monkey in monkeys])
print(inspect_counts[-1] * inspect_counts[-2])
# print(worry)
