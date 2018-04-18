# inFile = open("test.in", "r")
inFile = open("day12.in", "r")
inString = inFile.read()
inList = inString.splitlines()
Pdict = {}
for line in inList:
    tempLine = line.split('<->')
    pID = int(tempLine[0].strip())
    IDList = tempLine[1].strip().split(',')
    IDList = list(map(int, IDList))
    Pdict[pID] = IDList
# print(pID_dict)

def groupList(ID, Pdict):
    inGroup0 = []
    usedKeys = []
    end = False
    while not end:
        if ID not in usedKeys:
            usedKeys.append(ID)
        else:
            continue
        if ID not in inGroup0:
            inGroup0.append(ID)
        for entry in Pdict[ID]:
            if entry not in inGroup0:
                inGroup0.append(entry)
        for entry in inGroup0:
            if entry not in usedKeys:
                ID = entry
                break
        else:
            end = True
    return inGroup0



groupCount = 0

keyList = []

for key in Pdict:

    if key not in keyList:
        print(key)
        keyList += groupList(key, Pdict)
        groupCount += 1

print("count = " + str(groupCount))
