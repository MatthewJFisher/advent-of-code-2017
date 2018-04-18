# inFile = open("test.in", "r")
inFile = open("day13.in", "r")
inString = inFile.read()
inList = inString.splitlines()


fwDict = {}
for entry in inList:
    newEntry = entry.split(':')
    fwDict[int(newEntry[0])] = int(newEntry[1].strip())

timeEnd = max(fwDict.keys())

severity = 0
done = False
delay = 0
while not done:

    for t in range(delay, timeEnd + 1 + delay):
        rng = fwDict.get(t - delay, 0)
        if rng == 0:
            continue
        newLen = (rng - 1) * 2
        pos = t % newLen

        if pos == 0:

            break
            # severity += t * rng
    else:
        done = True
        break
    delay += 1
print(delay)
