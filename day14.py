import math


def knot_hash(inString):

    lengthList = []
    suffix = [17, 31, 73, 47, 23]


    for char in inString:
        lengthList.append(ord(char))
    lengthList = lengthList + suffix
    # print(lengthList)
    circleSize = 256
    # lengthList = [3,4,1,5]
    # circleSize = 5
    circle = []

    for i in range(circleSize):
        circle.append(i)
    # print(circle)
    skipSize = 0
    index = 0
    for step in range(64):
        for length in lengthList:
            # print(circle)
            if length == 0 or length == 1:
                index += skipSize + length
                while index > 255:
                    index -= 256

                skipSize += 1
                continue
            start = index
            end = index + length
            while end > circleSize:
                end = end - circleSize
            if end <= start:
                sec1 = circle[start:]
                sec2 = circle[:end]
                loop = sec1 + sec2
                loop.reverse()
                loopIndex = 0
                for i in range(start,len(circle)):
                    circle[i]=loop[loopIndex]
                    loopIndex+=1
                for i in range(0,end):
                    circle[i]=loop[loopIndex]
                    loopIndex+=1
            else:
                loop = circle[start:end]
                loop.reverse()

                loopIndex = 0
                for i in range(start,end):
                    circle[i]=loop[loopIndex]
                    loopIndex+=1
            index += skipSize + length
            # print(index)
            while index > 255:
                index -= 256
            skipSize += 1

    dense = []

    for index1 in range(16):
        dense.append('')
        dense[index1] = circle[index1*16]
        # print(dense[index1])
        for index2 in range(1,16):
            dense[index1] = dense[index1]^circle[index1*16+index2]
    hexOut = ''
    # print(len(dense))
    for item in dense:
        # print(item)
        digits = hex(item)[2:]
        if len(digits) < 2:
            digits = '0' + digits
        hexOut += digits

    # if len(hexOut) < 32:
    #     print(dense)
    #     print(hexOut)

    return(hexOut)

inString = "oundnydw"
# inString = "flqrgnkx"
grid = ""
for i in range(128):
    arg = inString + '-' + str(i)
    knot = knot_hash(arg)
    line = ""
    # print(len(knot))
    for char in knot:
        block = "{0:04b}".format(int(char,16))
        line += block
    grid += line
    # print(line)
# print(grid.count('1'))
# print(len(grid))
gridIndex = 0
inGroup = []
groupLists = []

def get_index(coords):
    ind = coords[1]*128 + coords[0]

    return(ind)

def get_coords(index):
    x = index % 128
    y = math.floor(index/128)
    return((x,y))

def find_group(grid, coord, inGroup):
    x = coord[0]
    y = coord[1]

    group = []
    if coord in inGroup or x > 127 or x < 0 or y > 127 or y < 0 or grid[get_index((x,y))] == '0':
        return [group, inGroup]

    inGroup.append(coord)
    # print(coord)
    for i in range(x - 1, x + 2, 2):
        if i > 127 or i < 0:
            continue
        if grid[get_index((i,y))] == '0':
            continue
        group.extend(find_group(grid, (i, y), inGroup)[0])

    for j in range(y - 1, y + 2, 2):
        if j > 127 or j < 0:
            continue
        # print(get_index((x,j)))
        if grid[get_index((x,j))] == '0':
            continue
        group.extend(find_group(grid, (x, j), inGroup)[0])

    if not (x > 127 or x < 0 or y > 127 or y < 0) and grid[get_index((x,y))] == '1':
        group.append((x,y))

    return [group, inGroup]

# print(find_group(grid, (0,0), inGroup))

while gridIndex < 128*128:
    if grid[gridIndex] == '0':
        gridIndex += 1
        continue

    coord = get_coords(gridIndex)

    if coord not in inGroup:
        group = find_group(grid, coord, inGroup)[0]
        inGroup = find_group(grid, coord, inGroup)[1]
        groupLists.append(group)
    else:
        gridIndex += 1
        continue

print(len(groupLists))
