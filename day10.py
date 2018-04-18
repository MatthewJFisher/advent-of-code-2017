inFile = open("day10.in", "r")
inString = inFile.read()
inString = inString.strip()

# lengthList = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
lengthList = []
suffix = [17, 31, 73, 47, 23]


for char in inString:
    lengthList.append(ord(char))
lengthList = lengthList + suffix
print(lengthList)
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
        print(circle)
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
# print(circle)
for index1 in range(16):
    dense.append('')
    dense[index1] = circle[index1*16]
    # print(dense[index1])
    for index2 in range(1,16):
        dense[index1] = dense[index1]^circle[index1*16+index2]
hexOut = ''
for item in dense:
    # print(item)
    hexOut += hex(item).lstrip('0x')
    # print(hexOut)
print(hexOut)
