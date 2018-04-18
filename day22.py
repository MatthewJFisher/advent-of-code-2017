import math
inFile = open("day22.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()

size_y = len(inList)
size_x = len(inList[0])

start_x = -1*math.floor(size_x/2)
start_y = math.floor(size_y/2)

nodes = {}

for i,line in enumerate(inList):
    for j,char in enumerate(line):
        key = (start_x + j, start_y - i)
        if char == '#':
            nodes[key] = 1
        elif char == '.':
            nodes[key] = 0
        else:
            print("bad node read!")

v_dir = "N"
v_pos = (0,0)

def turn(v_dir, turn_dir):
    new_dir = ""
    if v_dir == "N":
        if turn_dir == "L":
            new_dir = "W"
            return new_dir
        elif turn_dir == "R":
            new_dir = "E"
            return new_dir
        else:
            print("Bad directions!")
            return False
    if v_dir == "E":
        if turn_dir == "L":
            new_dir = "N"
            return new_dir
        elif turn_dir == "R":
            new_dir = "S"
            return new_dir
        else:
            print("Bad directions!")
            return False
    if v_dir == "S":
        if turn_dir == "L":
            new_dir = "E"
            return new_dir
        elif turn_dir == "R":
            new_dir = "W"
            return new_dir
        else:
            print("Bad directions!")
            return False
    if v_dir == "W":
        if turn_dir == "L":
            new_dir = "S"
            return new_dir
        elif turn_dir == "R":
            new_dir = "N"
            return new_dir
        else:
            print("Bad directions!")
            return False

def move(v_dir, v_pos):
    old_pos = v_pos
    new_pos = ()
    if v_dir == "N":
        new_pos = (old_pos[0], old_pos[1]+1)
    if v_dir == "E":
        new_pos = (old_pos[0]+1, old_pos[1])
    if v_dir == "S":
        new_pos = (old_pos[0], old_pos[1]-1)
    if v_dir == "W":
        new_pos = (old_pos[0]-1, old_pos[1])

    return new_pos


def burst(v_dir, v_pos, nodes, inf_counter):
    if v_pos not in nodes:
        nodes[v_pos] = 0
    if nodes[v_pos] == 1:
        v_dir = turn(v_dir, "R")
        nodes[v_pos] = 0
    elif nodes[v_pos] == 0:
        v_dir = turn(v_dir, "L")
        nodes[v_pos] = 1
        inf_counter += 1
    v_pos = move(v_dir,v_pos)
    return v_dir, v_pos, inf_counter


temp_dir = v_dir
temp_pos = v_pos
inf_sum = 0
for i in range(10000):

    temp_dir, temp_pos, inf_sum = burst(temp_dir, temp_pos, nodes, inf_sum)

print(inf_sum)
