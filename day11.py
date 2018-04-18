# inFile = open("test.in", "r")
inFile = open("day11.in", "r")
inString = inFile.read()
inString = inString.strip()
inList = inString.split(',')
# # print(inList)
# nCount = inList.count('n')
# sCount = inList.count('s')
# neCount = inList.count('ne')
# seCount = inList.count('se')
# nwCount = inList.count('nw')
# swCount = inList.count('sw')
#
# netN = nCount - sCount + 0.5*(neCount + nwCount - seCount - swCount)
# netE = 0.5*(neCount - nwCount + seCount - swCount)
#
# total = abs(netN)+abs(netE)
# print(total)
totalN = 0.0
totalE = 0.0
distance = 0.0
maxDist = 0.0
for step in inList:
    if step == 'n':
        totalN += 1.0
    if step == 'ne':
        totalN += 0.5
        totalE += 0.5
    if step == 'nw':
        totalN += 0.5
        totalE -= 0.5
    if step == 's':
        totalN -= 1.0
    if step == 'se':
        totalN -= 0.5
        totalE += 0.5
    if step == 'sw':
        totalN -= 0.5
        totalE -= 0.5
    distance = abs(totalN)+abs(totalE)
    if distance > maxDist:
        maxDist = distance

print(maxDist)
