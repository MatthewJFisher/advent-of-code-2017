import math
inFile = open("day21.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()

temp_rules = {}

for line in inList:

    temp_line = line.split("=>")
    temp_key = temp_line[0].strip().split("/")
    key = []

    for i,row in enumerate(temp_key):
        temp_row = []
        for j,node in enumerate(row):
            if node == ".":
                temp_row.append(0)
            elif node == "#":
                temp_row.append(1)
            else:
                print("Error translating rules!")
                break

        key.append(tuple(temp_row))

    temp_entry = temp_line[1].strip().split("/")
    entry = []

    for row in temp_entry:
        temp_row = []
        for node in row:
            if node == ".":
                temp_row.append(0)
            elif node == "#":
                temp_row.append(1)
            else:
                print("Error translating rules!")
                break
        entry.append(temp_row)

    temp_rules[tuple(key)] = entry

def rotate(block, degrees):

    if degrees % 90 != 0:
        print("Bad rotation angle! No rotation done.")
        return block

    new_block = []
    size = len(block)
    num_r = int(degrees / 90)
    temp_block = []

    for n in range(num_r):

        for i in range(size):
            temp_row = []
            for j in range(size):
                temp_row.append(block[i][j])
            temp_block.append(temp_row)

        for i in range(size):
            new_block.append([])
            for j in range(size):
                new_block[i].append(temp_block[abs(j-size+1)][i])

        for i,row in enumerate(new_block):
            new_block[i] = tuple(row)

    return tuple(new_block)

def flip(block, udlr):

    size = len(block)
    temp_block = []
    new_block = []

    for i in range(size):
        temp_block.append(block[i])

    if udlr == "ud":

        for i in range(size):
            new_block.append(temp_block[abs(i - size + 1)])

    elif udlr == "lr":

        for i in range(size):
            new_block.append([])
            for j in range(size):
                new_block[i].append(temp_block[i][abs(j-size+1)])

    else:
        print("Bad flip direction! No flip done.")
        return False

    for i,row in enumerate(new_block):
        new_block[i] = tuple(row)

    return tuple(new_block)

rules = {}

for key in temp_rules:
    temp_key = key
    for i in range(4):
        temp_key = rotate(temp_key, 90)
        if temp_key not in rules:
            rules[temp_key] = temp_rules[key]
        temp_key = flip(temp_key, "ud")
        if temp_key not in rules:
            rules[temp_key] = temp_rules[key]
        temp_key = flip(temp_key, "ud")
        temp_key = flip(temp_key, "lr")
        if temp_key not in rules:
            rules[temp_key] = temp_rules[key]
        temp_key = flip(temp_key, "lr")
    if temp_key != key:
        print("Error doing rule transformations!")

input_block = [[0,1,0],[0,0,1],[1,1,1]]

for i in range(18):
    print("Working on iteration " + str(i))
    size = len(input_block)
    if size % 2 == 0:
        n_div = int(size / 2)
        bigger_block = []
        for j in range(n_div):
            offset_x = j*int(size/n_div)
            for k in range(n_div):
                offset_y = k*int(size/n_div)
                block = []
                for l in range(int(size/n_div)):
                    row = []
                    for m in range(int(size/n_div)):
                        row.append(input_block[l+offset_y][m+offset_x])
                    block.append(row)
                for i,row in enumerate(block):
                    block[i] = tuple(row)
                new_block = tuple(block)
                bigger_block.append(rules[new_block])
        input_block = []
        size = size + n_div
        for j in range(size):
            row = []
            for k in range(n_div):

                offset_y = 0
                j_new = j
                if j >= size/n_div:
                    while j_new >= size/n_div:
                        j_new = j_new - int(size/n_div)
                    offset_y = math.floor(j/(size/n_div))
                row += bigger_block[k*n_div+offset_y][j_new]
            input_block.append(row)

    elif size % 3 == 0:
        n_div = int(size / 3)
        bigger_block = []
        for j in range(n_div):
            offset_x = j*int(size/n_div)
            for k in range(n_div):
                offset_y = k*int(size/n_div)
                block = []
                for l in range(int(size/n_div)):
                    row = []
                    for m in range(int(size/n_div)):
                        row.append(input_block[l+offset_y][m+offset_x])
                    block.append(row)
                for i,row in enumerate(block):

                    block[i] = tuple(row)
                new_block = tuple(block)
                bigger_block.append(rules[new_block])
        input_block = []
        size = size + n_div
        for j in range(size):
            row = []
            for k in range(n_div):

                offset_y = 0
                j_new = j
                if j >= size/n_div:
                    while j_new >= size/n_div:
                        j_new = j_new - int(size/n_div)
                    offset_y = math.floor(j/(size/n_div))
                row += bigger_block[k*n_div+offset_y][j_new]
            input_block.append(row)

sum_on = 0
for row in input_block:
    for pixel in row:
        sum_on += pixel
print(sum_on)
