import math
endPos = 0
size = endPos + 1
maxSize = 50000000

pos = 0
onZero = True
numSteps = 0
afterZero = 0

while size < maxSize:
    if size % 1000000 == 0:
        print("working on " + str(size))

    step = 343
    if step > size:
        step = step % size
    if pos + step >= size:
        step = step - size
    pos = pos + step
    # if pos + 1 == size:
    #     pos = 0
    numSteps += 1
    out = "numSteps = " + str(numSteps) + " position = " + str(pos) + " step = " + str(step)
    # print(out)
    if pos == 0:
        afterZero = numSteps
    pos += 1

    endPos += 1
    size = endPos + 1

print(afterZero)
