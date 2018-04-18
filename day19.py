inFile = open("day19.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()
down = (0,1)
up = (0,-1)
left = (-1, 0)
right = (1,0)
Y = 0

max_length = 0

for line in inList:
    if len(line) > max_length:
        max_length = len(line)

tempList = []

for line in inList:
    tempLine = line.ljust(max_length)
    tempList.append(tempLine)

inList = tempList

def move(tup0, tup1):
    return (tup0[0]+tup1[0], tup0[1]+tup1[1])

X = inList[0].index("|")

finished = False

p = (X,Y)

direction = down

queue = ""

n_moves = 0

while not finished:
    p = move(p, direction)
    n_moves += 1
    c = inList[p[1]][p[0]]
    if  c.isalpha():
        queue += c
    elif c == " ":
        finished = True
        
        break
    elif c == "+":
        if direction == down or direction == up:
            check_left = move(p, left)
            if check_left[1] < 0:
                direction = right
            elif inList[check_left[1]][check_left[0]] == '-':
                direction = left
            else:
                direction = right

        else:
            check_up = move(p, up)

            if check_up[1] >= len(inList[0]) or check_up[0] >= len(inList):
                direction = down

            elif inList[check_up[1]][check_up[0]] == '|':
                direction = up
            else:
                direction = down

print(queue)
print(n_moves)
