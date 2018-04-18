# inFile = open("test.in", "r")
inFile = open("day16.in", "r")
inString = inFile.read()
inList = inString.split(',')

pString = 'abcdefghijklmnop'
# pString = 'abcde'

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

    elif sxp == 'p':
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

print(pString)
print('s: ' + str(Ns) + ' x: ' + str(Nx) + ' p: ' + str(Np))
