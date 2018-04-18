inFile = open("day4.in", "r")
inString = inFile.read()
inString = inString.splitlines()

count = 0
for row in inString:
    valid = True
    row = row.split()
    newRow = []
    for word in row:
        word = word.strip()
        newRow.append(word)
    ana = True
    for i in range(len(newRow)-1):
        for j in range(i + 1, len(newRow)):
            ana = True
            if len(newRow[i])!=len(newRow[j]):
                ana = False
                continue
            for letter in newRow[i]:
                if newRow[i].count(letter) != newRow[j].count(letter):
                    ana = False
                    break
            if ana:
                valid = False
                break
            else:
                continue

        if not valid:
            break
    if valid:
        count += 1

#     if newRow.count(word) != 1:
#         valid = False
#         break
# if (valid):
#     count  += 1
print(count)
