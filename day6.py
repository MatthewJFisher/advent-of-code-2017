inFile = open("day6.in", "r")
#inFile = open("test.in", "r")
inString = inFile.read()
inList = inString.split()
Tup0 = ()
for num in inList:
    tempTup = (int(num.strip()),)
    Tup0 = Tup0 + tempTup
#print(newTup)
#print(newTup.index(max(newTup)))
newTup = Tup0
tupList = []
step = 0
while newTup not in tupList:
    tupList.append(newTup)
    tempTup = tupList[step]
    i0 = tempTup.index(max(tempTup))
    pile = tempTup[i0]
    newList = list(tempTup)
    index = i0
    newList[index] = 0
    while pile > 0:
        index+=1
        if index == len(newList):
            index = 0
        newList[index] += 1
        pile -= 1

    newTup = tuple(newList)
    step +=1
#print(tupList)
cycles = len(tupList) - tupList.index(newTup)
print(cycles)
