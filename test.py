inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()

comp_list = []

for line in inList:
    temp = line.strip().split("/")
    temp = list(map(int, temp))
    comp_list.append(tuple(temp))

starting_comps = []

for comp in comp_list:
    if 0 in comp:
        starting_comps.append(comp)

comp_dict = {}

for comp0 in comp_list:
    connections = {}
    connections[comp0[0]] = []
    connections[comp0[1]] = []
    for comp1 in comp_list:
        if comp0 == comp1 or comp1 in connections[comp0[0]] or comp1 in connections[comp0[1]]:
            continue
        else:
            for port in comp0:
                if port in comp1:
                    connections[port].append(comp1)
                if comp0[0] == comp0[1]:
                    break
    comp_dict[comp0] = connections

def get_max(comp_dict, comp0, target, weight, used_comps, max_weight, max_length, length):
    for comp in comp_dict[comp0][target]:
        if comp in used_comps:
            continue
        weight += comp[0] + comp[1]
        length += 1
        used_comps.append(comp)
        # print(used_comps)
        if length == max_length and weight > max_weight:
            max_weight = weight
        elif length > max_length:
            max_length = length
            max_weight = weight
            # print(length)
        if comp[0] == target:
            target = comp[1]
        else:
            target = comp[0]
        max_weight, max_length = get_max(comp_dict, comp, target, weight, used_comps, max_weight, max_length, length)

        last_comp = used_comps.pop()
        weight = weight - last_comp[0] - last_comp[1]
        length = length - 1
        if target == last_comp[0]:
            target = last_comp[1]
        else:
            target = last_comp[0]

    return max_weight, max_length

max_weight = 0
max_length = 0

for comp in starting_comps:
    if comp[0] == 0:
        target = comp[1]
    else:
        target = comp[0]
    weight = comp[0]+comp[1]
    length = 1
    used_comps = [comp]
    temp_weight, temp_length = get_max(comp_dict, comp, target, weight, used_comps, max_weight, max_length, length)
    if temp_length == max_length and temp_weight > max_weight:
        max_weight = temp_weight
    elif temp_length > max_length:
        max_length = temp_length
        max_weight = temp_weight



print(max_weight)
print(max_length)
