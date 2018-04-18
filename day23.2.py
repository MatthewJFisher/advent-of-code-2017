b = 106500
c = 123500
d = 0
e = 0
f = 0
h = 0


while(True):
    f = 1
    d = 2
    while(True):
        e = 2
        while(True):

            if d*e == b: # f = 0 when d is a factor of b
                f = 0
            e += 1
            if e != b: # break if e = b
                continue
            else:
                break
        d += 1
        if d != b: # break if d = b
            continue
        else:
            break
    if f == 0: # this is True except when b is prime
        h += 1
        print(h)
    if b == c: # finish when b = c
        break
    else:
        b += 17
        continue
