import numpy
from numpy.linalg import inv
import sys

def rounded(f):
    i = round(f)
    if abs(f - i) <= abs(f)/100:
        return "%d" % i
    return '%.2f' % f

for line in open(sys.argv[1]).readlines():
    items = line.split()
    if len(items) == 0:
        continue
    if items[0] != "1":
        continue
    k, col, x, y, z, a, b, c, d, e, f, g, h, i, fileName = items
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
    mat = numpy.matrix([[a,b,c], [d,e,f], [g,h,i]])
    mat2 = numpy.matrix([[ 0, 0.38, 0.92], [-1, 0, 0], [0,-0.92,0.38]])
    nmat = mat2*mat
    mat2 = mat2.tolist()
    na,nb,nc = mat2[0]
    nd,ne,nf = mat2[1]
    ng,nh,ni = mat2[2]
    #print mat, inv(mat)
    nx = na*x + nb*y + nc*z
    ny = nd*x + ne*y + nf*z
    nz = ng*x + nh*y + ni*z
    nmat = nmat.tolist()
    na,nb,nc = nmat[0]
    nd,ne,nf = nmat[1]
    ng,nh,ni = nmat[2]
    print " ".join([k, col]+map(rounded, (nx, ny, nz, na, nb,nc,nd,ne,nf,ng,nh,ni))+[fileName])

