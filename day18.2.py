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

regDict = [{},{}]
for p in range(0,2):
    for c in ascii_lowercase:
        regDict[p][c]=p

queue = [[],[]]

waiting = [False, False]

def snd(X, regDict=regDict, queue=queue, p=0):
    if not isinstance(X, int):
        X = regDict[p][X]
    queue[p].append(X)
    return X

def set(X, Y, regDict=regDict, p=0):
    if not isinstance(Y, int):
        Y = regDict[p][Y]
    regDict[p][X]=Y
    # print(regDict[X])

def add(X, Y, regDict=regDict, p=0):
    if not isinstance(Y, int):
        Y = regDict[p][Y]
    regDict[p][X]+=Y
    # print(regDict[X])

def mul(X, Y, regDict=regDict, p=0):

    if not isinstance(Y, int):
        Y = regDict[p][Y]
    regDict[p][X] = regDict[p][X]*Y
    # print(regDict[X])

def mod(X, Y, regDict=regDict, p=0):

    if not isinstance(Y, int):
        Y = regDict[p][Y]
    regDict[p][X] = regDict[p][X] % Y

def rcv(X, queue=queue, regDict=regDict, p=0):

    regDict[p][X] = queue[abs(p-1)].pop(0)

def jgz(X, Y, regDict=regDict, p=0):
    if not isinstance(X, int):
        X = regDict[p][X]
    if not isinstance(Y, int):
        Y = regDict[p][Y]
    if X > 0:
        return Y
    else:
        return 1

nextI = [0,0]


terminated = [False, False]

both_terminated = False

p1SndCount = 0

cycle = 0

while not both_terminated:
    cycle += 1
    if cycle % 10000 == 0:
        print("working on cycle " + str(cycle))
        print("p1 has sent a value " + str(p1SndCount) + " times")
        print("waiting values" + str(waiting))
        print("terminated values" + str(terminated))
        print(regDict[0]['a'])
        
    I = [instructions[nextI[0]], instructions[nextI[1]]]
    for p in range(2):
        if not terminated[p]:
            if not waiting[p] or queue[abs(p-1)]:
                if waiting[p] and queue[abs(p-1)]:
                    print("p = " + str(p) + " no longer waiting")
                    print(queue[abs(p-1)])
                    waiting[p] = False
                if I[p][0] == "snd":
                    snd(I[p][1], p=p)
                    if p == 1:
                        p1SndCount+=1
                elif I[p][0] == "set":
                    set(I[p][1],I[p][2], p=p)
                elif I[p][0] == "add":
                    add(I[p][1],I[p][2], p=p)
                elif I[p][0] == "mul":
                    mul(I[p][1],I[p][2], p=p)
                elif I[p][0] == "mod":
                    mod(I[p][1],I[p][2], p=p)
                elif I[p][0] == "rcv":
                    if queue[abs(p-1)] != []:
                        rcv(I[p][1], p=p)
                    else:
                        print("p = " + str(p) + " waiting")
                        print(queue[abs(p-1)])
                        waiting[p] = True

                if I[p][0] == "jgz":
                    nextI[p] += jgz(I[p][1],I[p][2], p=p)
                elif not waiting[p]:
                    nextI[p] += 1

    if nextI[0] >= len(instructions) or nextI[0] < 0:
        terminated[0] = True
        print("p0 terminated")

    if nextI[1] >= len(instructions) or nextI[1] < 0:
        terminated[1] = True
        print("p1 terminated")
    if (waiting[0] and waiting[1]) or (terminated[0] and terminated[1]):
       both_terminated = True


print(p1SndCount)
print('\n')
print(regDict[0]['a'])
print(regDict[0]['b'])
print(regDict[0]['c'])
print(regDict[0]['d'])
print('\n')
print(regDict[1]['a'])
print(regDict[1]['b'])
print(regDict[1]['c'])
print(regDict[1]['d'])
