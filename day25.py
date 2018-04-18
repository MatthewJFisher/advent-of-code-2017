inFile = open("day25.in", mode='r')
# inFile = open("test.in", mode='r')
inString = inFile.read()
inList = inString.splitlines()

state_dict = {}
state0 = ""
n_check = 0

state = ""
val = 0
next_val = 0
next_state = ""
direction = 0


for i,line in enumerate(inList):

    temp_line = line.strip()
    if "Begin" in temp_line:
        state0 = temp_line.lstrip("Begin in state ")
        state0 = state0.rstrip(".")
    elif "Perform" in temp_line:
        n_check = int(temp_line.lstrip("Perform a diagnostic checksum after ").rstrip(" steps."))
    elif "Write" in temp_line:
        if "1" in temp_line:
            next_val = 1
        else:
            next_val = 0
    elif "Move" in temp_line:
        if "right" in temp_line:
            direction = 1
        elif "left" in temp_line:
            direction = -1
    elif "current value" in temp_line:
        if "1" in temp_line:
            val = 1
        else:
            val = 0
    elif "In state" and ":" in temp_line:

        state = temp_line.lstrip("In state ")
        state = state.rstrip(":")


    elif "Continue" in temp_line:
        next_state = temp_line[22:].strip().rstrip(".")
        temp_list = [next_val, direction, next_state]
        if val == 0:
            state_dict[state] = {0: temp_list}
        if val == 1:
            state_dict[state][1] = temp_list
print(state_dict)
tape_dict = {}
pos = 0
state = state0

for i in range(n_check):
    if pos not in tape_dict:
        tape_dict[pos] = 0
    old_pos = pos
    old_val = tape_dict[pos]
    val = state_dict[state][old_val][0]
    tape_dict[old_pos] = val
    if val == 0:
        del tape_dict[old_pos]
    pos = old_pos + state_dict[state][old_val][1]
    state = state_dict[state][old_val][2]
    # print("old pos = " + str(old_pos))
    # print("old val = " + str(old_val))
    # print("new val = " + str(val))
    # print("new pos = " + str(pos))
    # print("new state = " + state)
    # print(tape_dict)

print(len(tape_dict))
