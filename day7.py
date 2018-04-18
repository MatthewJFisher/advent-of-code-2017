#inFile = open("test.in", "r")
inFile = open("day7.in", "r")
inString = inFile.read()
inList = inString.splitlines()
nameList = []
weightsDict = {}
childDict = {}
for line in inList:
    lineList = line.split(" ", 3)
    name = lineList[0]
    nameList.append(name)
    weightsDict[name]=int(lineList[1].rstrip(")").lstrip("("))
    if len(lineList)>2:
        childDict[name]=lineList[3].split(", ")

name0 = ""
for name in nameList:
    foundName = False
    if name in childDict:
        for key, item in childDict.items():
            if name in item:
                foundName = True
                break
        if not foundName:
            name0 = name
            break
def sum_weights(name, weightsDict, childDict):
    towerSum = 0
    childWeightList = []
    outList = []
    if name in childDict:

        for childName in childDict[name]:
            weight = sum_weights(childName, weightsDict, childDict)
            childWeightList.append(weight)
            outList.append((childName, weightsDict[childName], weight))
            towerSum += weight
        if childWeightList.count(childWeightList[0]) != len(childWeightList):
            print("Imbalanced")
            print(outList)

    towerSum += weightsDict[name]
    return towerSum
sum_weights(name0, weightsDict, childDict)
