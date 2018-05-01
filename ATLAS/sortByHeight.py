import sys
import math

def rounded(s):
    f = float(s)
    i = round(f)
    if abs(f - i) <= abs(f)/10000:
        return '%d' % i
    return '%.2f' % f

#for x in [449.9988098, 588.1538086, 832.1530151, -0.9999998808, 0, 1]:
#    print x, rounded(x)
#sys.exit()

def printBrick(b):
    print '%1s %2s %8s %8s %8s %5s %5s %5s %5s %5s %5s %5s %5s %5s %s' % b

bricks = []

for line in open(sys.argv[1]).readlines():
    items = line.split()
    if len(items) == 0:
        continue
    if items[0] != "1":
        continue
    k, col, x, y, z, a, b, c, d, e, f, g, h, i, name = items
    x = rounded(x)
    y = rounded(y)
    z = rounded(z)
    a = rounded(a)
    b = rounded(b)
    c = rounded(c)
    d = rounded(d)
    e = rounded(e)
    f = rounded(f)
    g = rounded(g)
    h = rounded(h)
    i = rounded(i)
    bricks.append((k, col, x, y, z, a, b, c, d, e, f, g, h, i, name))

def addSortData(brick):
    k, col, x, y, z, a, b, c, d, e, f, g, h, i, fileName = brick
    z = float(z)+1000
    y = float(y)-110
    if z == 0:
        theta = copysign(math.pi/2, y)
    else:
        theta = math.atan(y/z)
    sortData = (int(round(3*math.pi/8+theta*8/math.pi)))
    #sortData = int(float(x)/10)*10
    return (brick, sortData)

bricks = map(addSortData, bricks)
bricks.sort(key=lambda brick: brick[1])

#for b in bricks:
#    printBrick(b)

#sys.exit(1)
printBrick(bricks[0][0])
h = bricks[0][1]
for b in bricks[1:]:
    nh = b[1]
    if nh != h:
        print '0 STEP'
        h = nh
    printBrick(b[0])
