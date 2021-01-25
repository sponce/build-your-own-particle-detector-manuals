import sys
import math

def rounded(s):
    f = float(s)
    i = round(f)
    if abs(f - i) <= abs(f)/100 or abs(f) < 0.05:
        return i
    return round(f,2)

def roundedh(s):
    return round(float(s))

def pF(f, t):
    return format(f, t).strip('0').strip('.')
def pF8(f):
    return pF(f, '8.2f')
def pF5(f):
    return pF(f, '5.2f')

def printBrick(k, col, x, y, z, a, b, c, d, e, f, g, h, i, name):
    print '%1s %2s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (k, col, pF8(x), pF8(y), pF8(z), pF5(a), pF5(b), pF5(c), pF5(d), pF5(e), pF5(f), pF5(g), pF5(h), pF5(i), name)

bricks = []

for line in open(sys.argv[1]).readlines():
    items = line.split()
    if len(items) == 0:
        continue
    if items[0] != "1":
        continue
    k, col, x, y, z, a, b, c, d, e, f, g, h, i, name = items
    x = roundedh(x)
    y = roundedh(y)
    z = roundedh(z)
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
    z = float(z)
    y = float(y)
    if z == 0:
        theta = math.copysign(math.pi/2, y)
    else:
        theta = math.atan(y/z)
    #sortData = (int(round(3*math.pi/8+theta*8/math.pi)))
    sortData = int(float(-y/8)*10)
    return (brick, sortData)

bricks = map(addSortData, bricks)
bricks.sort(key=lambda brick: brick[1])

printBrick(*bricks[0][0])
h = bricks[0][1]
for b in bricks[1:]:
    nh = b[1]
    if nh != h:
        print '0 STEP'
        h = nh
    printBrick(*b[0])
