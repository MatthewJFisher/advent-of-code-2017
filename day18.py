from string import ascii_lowercase
inFile = open("day18.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()
instructions = []
for line in inList:
    line = line.strip()
    lineList = line.split()
    inst = []
    for entry in lineList:
        if not entry.isalpha():
            entry = int(entry)
        inst.append(entry)
    instructions.append(inst)

regDict = {}

for c in ascii_lowercase:
    regDict[c]=0

freqList = []

def snd(X, regDict=regDict, freqList=freqList):
    if not isinstance(X, int):
        X = regDict[X]
    freqList.append(X)
    return X

def set(X, Y, regDict=regDict):
    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X]=Y
    # print(regDict[X])

def add(X, Y, regDict=regDict):
    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X]+=Y
    # print(regDict[X])

def mul(X, Y, regDict=regDict):

    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X] = regDict[X]*Y
    # print(regDict[X])

def mod(X, Y, regDict=regDict):

    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X] = regDict[X] % Y

def rcv(X, freqList=freqList):
    if X != 0:
        return(freqList[-1])

def jgz(X, Y, regDict=regDict):
    if not isinstance(X, int):
        X = regDict[X]
    if not isinstance(Y, int):
        Y = regDict[Y]
    if X > 0:
        return Y
    else:
        return 1

nextI = 0


while nextI < len(instructions) and nextI >= 0:

    I = instructions[nextI]
    print(I)
    if I[0] == "snd":
        snd(I[1])
    elif I[0] == "set":
        set(I[1],I[2])
    elif I[0] == "add":
        add(I[1],I[2])
    elif I[0] == "mul":
        mul(I[1],I[2])
    elif I[0] == "mod":
        mod(I[1],I[2])
    elif I[0] == "rcv":
        if I[1]!=0:
            print(rcv(I[1]))
            break
        rcv(I[1])

    if I[0] == "jgz":
        nextI += jgz(I[1],I[2])
    else:
        nextI += 1
