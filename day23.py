from string import ascii_lowercase
inFile = open("day23.in", mode='r')
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


def set(X, Y, regDict=regDict):
    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X]=Y
    # print(regDict[X])

def sub(X, Y, regDict=regDict):
    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X] = regDict[X] - Y
    # print(regDict[X])

def mul(X, Y, regDict=regDict):

    if not isinstance(Y, int):
        Y = regDict[Y]
    regDict[X] = regDict[X]*Y
    # print(regDict[X])


def jnz(X, Y, regDict=regDict):
    if not isinstance(X, int):
        X = regDict[X]
    if not isinstance(Y, int):
        Y = regDict[Y]
    if X != 0:
        return Y
    else:
        return 1

nextI = 0

mul_count = 0

while nextI < len(instructions) and nextI >= 0:

    I = instructions[nextI]
    # print(I)
    if I[0] == "set":
        set(I[1],I[2])
    elif I[0] == "sub":
        sub(I[1],I[2])
    elif I[0] == "mul":
        mul(I[1],I[2])
        mul_count += 1
    if I[0] == "jnz":
        nextI += jnz(I[1],I[2])
    else:
        nextI += 1

print(mul_count)
