# import math
# num = 347991
# squarert = math.ceil(math.sqrt(float(num)))
# print(squarert)
# if squarert%2==0:
#     squarert +=1
# radius = int((squarert - 1)/2)
# print(radius)
# offset = squarert*squarert-num
# pathlength = 0
# while offset > radius:
#     offset -= radius
# else:
#     pathlength = radius + radius - offset
#
# print(pathlength)

radius = 0
perimeter = 1
corner = False
lastCorner = False
x = 0
y = 0
num = 0
valsDict = {}
valsDict[(0,0)] = 1
x += 1
radius += 1
highnum = 0
while highnum < 347991:
    pos = 0
    perimeter = radius * 2 * 4
    while perimeter > pos:
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1, y+2):
                count += valsDict.get((i,j), 0)
                #print(count)
        valsDict[(x,y)] = count
        if pos < radius * 2 - 1:
            y += 1
        elif pos < radius * 2 * 2 - 1:
            x -= 1
        elif pos < radius * 2 * 3 - 1:
            y -= 1
        elif pos < radius * 2 * 4 - 1:
            x += 1
        num = count
        if num > highnum:
            highnum = num
            if highnum > 347991:
                print(" highnum = " + str(highnum))
                #print(valsDict.items())
                break

        pos += 1
    x += 1
    radius += 1
    out = "radius = " + str(radius)
    print(out)
print(valsDict[(2,3)])
