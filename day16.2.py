import math
# s0 = 'abcdefghijklmnop'
# s1 = 'kpbodeajhlicngmf'
# counter = 0
# for i in range(4):
#     iList = []
#     sTemp = s0
#     for x in s1:
#         i1 = s0.index(x)
#         iList.append(i1)
#
#     for j in range(10):
#         # sNew = s1[iList[0]]+s1[iList[1]]+s1[iList[2]]+s1[iList[3]]+s1[iList[4]]\
#         #         +s1[iList[5]]+s1[iList[6]]+s1[iList[7]]+s1[iList[8]]+s1[iList[9]]\
#         #         +s1[iList[10]]+s1[iList[11]]+s1[iList[12]]+s1[iList[13]]\
#         #         +s1[iList[14]]+s1[iList[15]]
#         sNew = ''
#         for k in range(16):
#             sNew += sTemp[iList[k]]
#         sTemp = sNew
#         counter += 1
#     s1 = sTemp
#
# print(s1)
# print(counter)

inFile = open("test.in", "r")
# inFile = open("day16.in", "r")
inString = inFile.read()
inList = inString.split(',')

pString = 'abcdefghijklmnop'
# pString = 'abcde'


def dance(inList, pString, useP):

    Ns = 0
    Nx = 0
    Np = 0
    for com in inList:
        tempString = pString
        sxp = com[0]
        move = com[1:]
        if sxp == 's':
            move = int(move)
            tempString = pString[-move:] + pString[0:-move]
            Ns +=1
        elif sxp == 'x':
            Nx += 1
            moveList = move.split('/')
            move0 = int(moveList[0])
            move1 = int(moveList[1].strip())
            if move0 < move1:
                tempString = pString[:move0] + pString[move1]\
                             + pString[move0+1:move1] + pString[move0]\
                             + pString[move1+1:]
            else:
                tempString = pString[:move1] + pString[move0]\
                             + pString[move1+1:move0] + pString[move1]\
                             + pString[move0+1:]

        elif sxp == 'p' and useP:
            Np += 1
            moveList = move.split('/')
            # print(moveList)
            move0 = pString.index(moveList[0])
            move1 = pString.index(moveList[1].strip())
            if move0 < move1:
                tempString = pString[:move0] + pString[move1]\
                             + pString[move0+1:move1] + pString[move0]\
                             + pString[move1+1:]
            else:
                tempString = pString[:move1] + pString[move0]\
                             + pString[move1+1:move0] + pString[move1]\
                             + pString[move0+1:]
        pString = tempString
    return pString
pString2 = pString
s0 = pString
print("s0 = " + s0)
convAt = 0
for i in range(100):
    pString = dance(inList, pString, True)
    # print(pString)
    pString2 = dance(inList, pString2, False)
    # print(pString2)
    # print('\n')
    if pString == pString2:
        print("converge after " + str(i + 1) + " steps")
        print("to: " + pString)
        convAt = i + 1
        break
pString3 = s0
for i in range(32):
    pString3 = dance(inList, pString3, True)

print("pString after ?? cycles: " + str(pString3))

s1 = pString2
counter = 0
num = 1000000000
extraNum = num%convAt
cycles = math.floor(num/convAt)

for i in range(1):
    iList = []
    sTemp = s0
    for x in s1:
        i1 = s0.index(x)
        iList.append(i1)

    for j in range(3):
        sNew = ''
        for k in range(16):
            sNew += sTemp[iList[k]]
        sTemp = sNew
        counter += 1
    s1 = sTemp

print("s1 after ?? cycles: " + str(s1))
