infile = open("day2.in", "r")
inString = infile.read()
inStringList = inString.splitlines()
#print(inStringList[0])
checksum = 0
for row in inStringList:
    newRow = row.split()
    newRow = list(map(int, newRow))
    #print(newRow)
    #checksum += (max(newRow) - min(newRow))
    found = False
    for i in range(len(newRow) - 1):
        for j in range(i + 1, len(newRow)):
            if newRow[i] % newRow[j] == 0:
                found = True
                checksum += int(newRow[i]/newRow[j])
                break
            elif newRow[j] % newRow[i] == 0:
                found = True
                checksum += int(newRow[j]/newRow[i])
                break
        if found:
            break



print(checksum)
