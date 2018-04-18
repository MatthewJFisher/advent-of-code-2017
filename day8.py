# inFile = open("test.in", "r")
inFile = open("day8.in", "r")
inString = inFile.read()
inList = inString.splitlines()
registerDict = {}
instList = []

def create_register_instr(list):
    reg = list[0]
    change = int(list[2])
    if list[1]=='dec':
        change *= -1
    check_reg = list[4]
    symbol = list[5]
    condition = int(list[6])
    outList = [check_reg, symbol, condition, reg, change]
    return outList

for line in inList:
    lineList = line.split()
    #print(lineList)
    register = lineList[0]
    registerDict[register]=0
    instList.append(create_register_instr(lineList))

highest = 0
for inst in instList:

    if inst[1] == '==':
        if registerDict[inst[0]]==inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]
    elif inst[1] == '>':
        if registerDict[inst[0]]>inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]

    elif inst[1] == '<':
        if registerDict[inst[0]]<inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]

    elif inst[1] == '<=':
        if registerDict[inst[0]]<=inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]

    elif inst[1] == '>=':
        if registerDict[inst[0]]>=inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]

    elif inst[1] == '!=':
        if registerDict[inst[0]]!=inst[2]:
            registerDict[inst[3]]+=inst[4]
            if registerDict[inst[3]]>highest:
                highest=registerDict[inst[3]]

# print(max(registerDict.values()))
print(highest)
