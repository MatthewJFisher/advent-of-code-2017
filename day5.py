inFile = open("day5.in", "r")
#inFile = open("test.in", "r")
inList = inFile.read()
inList = inList.splitlines()
inList = list(map(int, inList))
index = 0
steps = 0
while index < len(inList):
    jump = inList[index]
    if jump > 2:
        inList[index]-=1
    else:
        inList[index]+=1
    steps += 1
    index += jump

print(steps)
