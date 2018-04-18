infile = open("day1.in", "r")
inString = infile.read()
inString = inString.strip()
inLen = len(inString)
offset = int(inLen/2)
#print(offset)
#print(inString)
pos = 0
digList = []
digSum = 0
for digit in inString:
    if int(digit) == int(inString[pos - offset]):
        digList.append(int(inString[pos - offset]))
        digSum += int(digit)
    pos +=1
print(digSum)
