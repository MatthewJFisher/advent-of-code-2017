inFile = open("day20.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()

p_dict = {}

def dist0(pos):
    return abs(pos[0])+abs(pos[1])+abs(pos[2])

for p_num, line in enumerate(inList):
    temp_line = line.split()

    pos = temp_line[0].lstrip("p=< ")
    pos = pos.rstrip(">,")
    pos = pos.split(",")
    pos = list(map(int, pos))

    vel = temp_line[1].lstrip("v=< ")
    vel = vel.rstrip(">,")
    vel = vel.split(",")
    vel = list(map(int, vel))

    acc = temp_line[2].lstrip("a=< ")
    acc = acc.rstrip(">")
    acc = acc.split(",")
    acc = list(map(int, acc))

    p_dict[p_num] = {"p": pos, "v": vel, "a": acc, "d0": 0, "d1": dist0(pos), "s": 0}


# print(p_dict)

def tick(num_ticks, p_dict=p_dict):
    for t in range(num_ticks):
        for part in p_dict:
            for x in range(3):
                p_dict[part]["v"][x] += p_dict[part]["a"][x]
                p_dict[part]["p"][x] += p_dict[part]["v"][x]
            p_dict[part]["d0"] = p_dict[part]["d1"]
            p_dict[part]["d1"] = dist0(p_dict[part]["p"])
            p_dict[part]["s"] = p_dict[part]["d1"] - p_dict[part]["d0"]

def get_closest(p_dict=p_dict):
    min_dist = p_dict[0]["d1"]
    closest = -1
    for part in p_dict:
        if p_dict[part]["d1"] <= min_dist:
            min_dist = p_dict[part]["d1"]
            closest = part
    print(str("particle " + str(closest) + " is " + str(min_dist) + " away from the origin"))
    return closest, min_dist

tick(10000)

get_closest()
