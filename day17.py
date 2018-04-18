end = 2017
slb = [0]
for i in range(1,end + 1):
    if i % 10000 == 0:
        print("working on " + str(i))
    step = 343
    pos = slb.index(i - 1)
    size = len(slb)
    if step > size:
        step = step % size
    if pos + step >= size:
        step = step - size
    insert = pos + step + 1
    if insert == size:

        insert = 1
    slb.insert(insert, i)

    # print("num = " + str(slb[slb.index(0)+1]) + ", step = " + str(i) + ", size = " + str(size))
    # print(str(slb) + ", step = " + str(i))
print("num = " + str(slb[slb.index(2017)+1]))
