import numpy
from numpy.linalg import inv
import sys

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

def getLines(f):
  doTransforms = True
  pieces = []
  transforms = []
  for line in open(sys.argv[1]).readlines():
    if len(line.strip()) == 0:
        doTransforms = False
        continue
    k, col, x, y, z, a, b, c, d, e, f, g, h, i, fileName = line.split()
    x = float(x)
    y = float(y)
    z = float(z)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    g = float(g)
    h = float(h)
    i = float(i)
    item = (k,col,x,y,z,a,b,c,d,e,f,g,h,i,fileName)
    if doTransforms:
      transforms.append(item)
    else:
      pieces.append(item)
  return pieces, transforms

pieces, transforms = getLines(open(sys.argv[1]))

for transform in transforms:
    k,col,x,y,z,a,b,c,d,e,f,g,h,i,ignFileName = transform
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    for line in pieces:
        kp, colp, xp, yp, zp, ap,bp,cp,dp,ep,fp,gp,hp,ip,fileName = line
        mat2 = numpy.matrix([[ap,bp,cp], [dp,ep,fp], [gp,hp,ip]])
        nmat = mat*mat2
        nmat = nmat.tolist()
        na,nb,nc = nmat[0]
        nd,ne,nf = nmat[1]
        ng,nh,ni = nmat[2]
        nx,ny,nz = (mat.dot(numpy.array([xp,yp,zp])) + numpy.array([x,y,z]))[0].tolist()[0]
        printBrick(kp, colp, roundedh(nx), roundedh(ny), roundedh(nz),
                   rounded(na), rounded(nb), rounded(nc), rounded(nd),
                   rounded(ne), rounded(nf), rounded(ng), rounded(nh),
                   rounded(ni), fileName)
