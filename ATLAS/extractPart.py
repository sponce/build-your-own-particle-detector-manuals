import sys
import numpy
from numpy.linalg import inv

def applyRotation(pInPiece, t):
    xp, yp, zp, ap, bp, cp, dp, ep, fp, gp, hp, ip = pInPiece
    x, y, z, a, b, c, d, e, f, g, h, i = t
    matp = numpy.matrix([[ap,bp,cp], [dp,ep,fp], [gp,hp,ip]])
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    matr = mat*matp
    matr = matr.tolist()
    ar,br,cr = matr[0]
    dr,er,fr = matr[1]
    gr,hr,ir = matr[2]
    return (xp, yp, zp, ar, br, cr, dr, er, fr, gr, hr, ir)

rotate90X = (0,0,0, 1,0,0,  0,0,-1, 0,1,0)
rotate90Y = (0,0,0, 0,0,-1, 0,1,0,  1,0,0)
rotate90Z = (0,0,0, 0,-1,0, 1,0,0,  0,0,1)

rotate180X = (0,0,0,1,0,0,0,-1,0,0,0,-1)
rotate180Y = (0,0,0,-1,0,0,0,1,0,0,0,-1)
rotate180Z = (0,0,0,-1,0,0,0,-1,0,0,0,1)

rotate270X = (0,0,0, 1,0,0, 0,0,1,  0,-1,0)
rotate270Y = (0,0,0, 0,0,1, 0,1,0, -1,0,0)
rotate270Z = (0,0,0, 0,1,0, -1,0,0, 0,0,1)

all180Rotations = [rotate180X, rotate180Y, rotate180Z]
allRotations = [rotate90X, rotate90Y, rotate90Z,
                rotate180X, rotate180Y, rotate180Z,
                rotate270X, rotate270Y, rotate270Z,
                    applyRotation(rotate180X, rotate90Y), applyRotation(rotate180X, rotate270Y),
                    applyRotation(rotate180X, rotate90Z), applyRotation(rotate180X, rotate270Z),
                    applyRotation(rotate180Y, rotate90X), applyRotation(rotate180Y, rotate270X),
                    applyRotation(rotate180Y, rotate90Z), applyRotation(rotate180Y, rotate270Z),
                    applyRotation(rotate180Z, rotate90X), applyRotation(rotate180Z, rotate270X),
                    applyRotation(rotate180Z, rotate90Y), applyRotation(rotate180Z, rotate270Y)]
#allRotations= []

def rounded(s):
    f = float(s)
    i = round(f)
    if abs(f - i) <= abs(f)/100 or abs(f) < 0.01:
        return i
    return round(f,2)

def printBrick(b):
    print '%1s %2s %8.2f %8.2f %8.2f %5g %5g %5g %5g %5g %5g %5g %5g %5g %s' % tuple(b)

def parseFile(filename):
    bricks = {}
    for line in open(filename).readlines():
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
        if name not in bricks:
            bricks[name] = []
        bricks[name].append((col, (x, y, z, a, b, c, d, e, f, g, h, i)))
    return bricks

def computeTransform(pInPiece, pInModel):
    xp, yp, zp, ap, bp, cp, dp, ep, fp, gp, hp, ip = pInPiece
    matp = numpy.matrix([[ap,bp,cp], [dp,ep,fp], [gp,hp,ip]])
    x, y, z, a, b, c, d, e, f, g, h, i = pInModel
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    matr = mat*inv(matp)
    matr = matr.tolist()
    ar,br,cr = matr[0]
    dr,er,fr = matr[1]
    gr,hr,ir = matr[2]
    xr = x - ar*xp - br*yp - cr*zp
    yr = y - dr*xp - er*yp - fr*zp
    zr = z - gr*xp - hr*yp - ir*zp
    return map(lambda x:round(x,2), (xr, yr, zr, ar, br, cr, dr, er, fr, gr, hr, ir))

def applyTransform(pInPiece, t):
    xp, yp, zp, ap, bp, cp, dp, ep, fp, gp, hp, ip = pInPiece
    x, y, z, a, b, c, d, e, f, g, h, i = t
    xr = a*xp + b*yp + c*zp + x
    yr = d*xp + e*yp + f*zp + y
    zr = g*xp + h*yp + i*zp + z
    matp = numpy.matrix([[ap,bp,cp], [dp,ep,fp], [gp,hp,ip]])
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    matr = mat*matp
    matr = matr.tolist()
    ar,br,cr = matr[0]
    dr,er,fr = matr[1]
    gr,hr,ir = matr[2]
    return (xr, yr, zr, ar, br, cr, dr, er, fr, gr, hr, ir)

def applyRotation(pInPiece, t):
    xp, yp, zp, ap, bp, cp, dp, ep, fp, gp, hp, ip = pInPiece
    x, y, z, a, b, c, d, e, f, g, h, i = t
    matp = numpy.matrix([[ap,bp,cp], [dp,ep,fp], [gp,hp,ip]])
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    matr = mat*matp
    matr = matr.tolist()
    ar,br,cr = matr[0]
    dr,er,fr = matr[1]
    gr,hr,ir = matr[2]
    return (xp, yp, zp, ar, br, cr, dr, er, fr, gr, hr, ir)

# piece = (1,1,1, 1,0,0,0,1,0,0,0,1)
# model = (-1,-1,-1, -1,0,0,0,-1,0,0,0,1)
# print 'piece :', piece
# print 'model :', model
# t = computeTransform(piece, model)
# print 'tranform :', t
# r = applyTransform(piece, t)
#print 'inmodel :', r

def closeEnough(itema, itemb):
    for a,b in zip(itema[:3], itemb[:3]):
        if abs(a-b) > 5:
            return False
    for a,b in zip(itema[3:], itemb[3:]):
        if abs(a-b) > abs(0.02*max(a,b)) and abs(a-b) > 0.02:
            return False
    return True

def find(item, l):
    for a in l:
        if closeEnough(item[1], a[1]):
            return True
    return False

def simplifyModel(piecesToRemove, model):
    for b, pcol, placeInModel in piecesToRemove:
        for col, a in model[b]:
            if closeEnough(placeInModel, a):
                model[b].remove((col, a))
                break            

def findPieceInModel(pieceName, piece, model):
    # find the brick in piece that is the least common in the model
    bricksInPiece = piece.keys()
    nbInPiece = 9999999
    bestBrick = None
    for b in bricksInPiece:
        if b not in model:
            return None
        nbInModel = len(model[b])
        if nbInModel == 0:
            return None
        if nbInModel < nbInPiece:
            nbInPiece = nbInModel
            bestBrick = b
    print 'Using brick', bestBrick, 'as transformer. We have only', nbInPiece
    # find all possible transformation for putting that piece in the model
    transforms = []
    for col, placeInPiece in piece[bestBrick]:
        for col2, placeInModel in model[bestBrick]:
            transforms.append((computeTransform(placeInPiece, placeInModel), (bestBrick, col, placeInPiece)))
            for rot in all180Rotations:
                rotPiece = applyTransform(rot, placeInPiece)
                transforms.append((computeTransform(rotPiece, placeInModel), (bestBrick, col, rotPiece)))
    # For each transform, go through all bricks of the piece and
    # check we find the corresponding one in model
    res = []
    for t, pieceToRemove in transforms:
        #print 'Trying transform', t
        ok = True
        piecesToRemove = [pieceToRemove]
        for b in piece:
            if not ok: break
            for col, placeInPiece in piece[b]:
                placeInModel = applyTransform(placeInPiece, t)
                if find((col, placeInModel), model[b]):
                    piecesToRemove.append((b, col, placeInModel))
                else:
                    # try different rotation of the piece checked
                    found = False
                    for rot in allRotations:
                        nplaceInPiece = applyRotation(placeInPiece, rot)
                        placeInModel = applyTransform(nplaceInPiece, t)
                        if find((col, placeInModel), model[b]):
                            piecesToRemove.append((b, col, placeInModel))
                            found = True
                            break
                    if not found:
                        # we've tried everything...
                        ok = False
                        break
        if ok:
            simplifyModel(piecesToRemove, model)
            res.append(list(t) + [pieceName])
            print 'Found piece in model with transform %s' % (str(t))
    return res

model = parseFile(sys.argv[1])
nbBricksinModel = 0
print 'Working with model'
for b in model:
    print ' ', b, len(model[b]), 'times'
    nbBricksinModel += len(model[b])
    #for p in model[b]:
    #    print '   ', p
print "Initially, model had %d bricks" % nbBricksinModel

transforms = []
for n in range(2,len(sys.argv)):
    pieceName = sys.argv[n]
    piece = parseFile(pieceName)
    print 'Working with piece', pieceName
    #for b in piece:
    #    print ' ', b
    #    for p in piece[b]:
    #        print '   ', p
    nt = findPieceInModel(pieceName, piece, model)
    if nt:
        transforms = transforms + nt

nbRemBricksInModel = 0
for b in model:
    nbRemBricksInModel += len(model[b])
print "At the end, only %d raw bricks in model" % nbRemBricksInModel

for t in transforms:
    printBrick(['1', '0'] + list(t))

print
print "Remaining pieces"
print

for b in model:
    for col,t in model[b]:
        printBrick([1, col] + list(t) + [b])
