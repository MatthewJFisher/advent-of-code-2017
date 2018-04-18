# inFile = open("test.in", "r")
inFile = open("day9.in", "r")
inString = inFile.read()
score = 0
score_sum = 0
index = 0
garbageSum = 0
while index < len(inString):
    char = inString[index]
    if char == '!':
        index += 2
        continue

    if char == '<':
        foundEnd = False
        garbageStart = index
        while not foundEnd:
            garbageEnd = inString.find('>', garbageStart + 1)
            # print(garbageEnd)
            if inString[garbageEnd - 1]=='!':
                checkChar = inString[garbageEnd - 1]
                countExclam = 0

                while checkChar == '!':
                    countExclam += 1
                    checkChar = inString[garbageEnd - 1 - countExclam]
                if countExclam%2==0:
                    foundEnd = True
                    break
                garbageStart = garbageEnd
                continue
            else:
                foundEnd = True
        garbageCount = 0
        garbageIndex = index + 1
        while garbageIndex < garbageEnd:
            # print(garbageIndex)
            if inString[garbageIndex] == '!':
                garbageIndex += 2
                continue
            garbageCount += 1
            garbageIndex += 1


        garbageSum += garbageCount
        index = garbageEnd + 1
        continue

    if char == '{':
        score += 1
        score_sum += score
        index += 1
        # print("found group ")
        continue

    if char == '}':
        score -= 1
        index += 1
        continue

    if char == ',':
        index += 1
        continue

    if char == '\n':
        print("end of input")
        break
    else:
        print("Error, unexpected character: " + char)
        break

print(garbageSum)
