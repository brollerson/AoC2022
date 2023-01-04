class Dir:
    def __init__(self, name, parent):
        self.name = name
        # self.parent = None
        # self.location = ""
        self.children = []
        self.files = []
        self.size = 0

        def get_parent(self, parent):
            if self.name == "/":
                self.parent = None
            else:
                self.parent = parent

        def get_location(self):
            if self.name == "/":
                self.location = "/"
            else:
                self.location = self.parent.location + "/" + self.name

        get_parent(self, parent)
        get_location(self)

    def __repr__(self):
        return f"Dir({self.name}, {self.parent})"

    def add_dir(self, dir_name):
        new_dir = Dir(dir_name, self)
        self.children.append(new_dir)

    def add_file(self, file_info):
        self.files.append(file_info)

    def clear_dirs(self):
        self.children = []

    def clear_files(self):
        self.files = []

    def calculate_size(self):
        self.size = 0
        for file_info in self.files:
            self.size += int(file_info[0])
        for child in self.children:
            self.size += child.calculate_size()
        return self.size

    def has_children(self):
        return len(self.children) > 0


dir_sizes = {}


def get_dir_sizes(cur_dir):
    cur_dir.calculate_size()
    global dir_sizes
    dir_sizes[cur_dir.location] = cur_dir.size
    if cur_dir.has_children():
        for child in cur_dir.children:
            get_dir_sizes(child)


with open("input07") as f:
    data = f.read().splitlines()

cur_dir = Dir("/", None)
# print(cur_dir.name, cur_dir.parent, cur_dir.location)
dir_list = []

for line in data:
    if line.startswith("$"):
        command = line[2:].split(" ")
        if command[0] == "cd":
            dir_name = command[1]
            if dir_name == "..":
                cur_dir = cur_dir.parent
            else:
                for child in cur_dir.children:
                    if child.name == dir_name:
                        cur_dir = child
                        break
                else:
                    new_dir = Dir(dir_name, cur_dir)
                    cur_dir.children.append(new_dir)
                    cur_dir = new_dir
        elif command[0] == "ls":
            cur_dir.clear_dirs()
            cur_dir.clear_files()
    elif line.startswith("dir"):
        dir_name = line.split(" ")[1]
        dir_list.append(dir_name)
        cur_dir.add_dir(dir_name)
    else:
        file_info = line.split(" ")
        cur_dir.add_file(file_info)
    cur_dir.calculate_size()
    # print(
    #     cur_dir.name,
    #     # cur_dir.parent.name,
    #     cur_dir.location,
    #     [child.name for child in cur_dir.children],
    #     cur_dir.files,
    #     cur_dir.size,
    # )


def goto_root(cur_dir):
    while cur_dir.name != "/":
        cur_dir = cur_dir.parent
    return cur_dir


root = goto_root(cur_dir)

get_dir_sizes(root)

target_list = [(k, v) for k, v in dir_sizes.items()]
# target_list = [(k, v) for k, v in dir_sizes.items() if v >= 8381165]
# total = 0
# for target in target_list:
#     total += target[1]
# print(total)

largest = target_list[0]
for item in target_list:
    if item[1] >= largest[1]:
        largest = item
print(largest)

unused_space = 70000000 - largest[1]
print(unused_space)
target_list = [(k, v) for k, v in dir_sizes.items() if v >= (30000000 - unused_space)]

smallest = target_list[0]
for item in target_list:
    if item[1] <= smallest[1]:
        smallest = item

print(smallest)
