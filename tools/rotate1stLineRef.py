import numpy
from numpy.linalg import inv
import sys

def rounded(f):
    i = round(f)
    if abs(f - i) <= abs(f)/100:
        return "%d" % i
    return '%.2f' % f

def parseLine(line):
    items = line.split()
    if len(items) == 0:
        print line[:-1]
        return
    if items[0] != "1":
        print line[:-1]
        return
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
    return k, col, x, y, z, numpy.matrix([[a,b,c], [d,e,f], [g,h,i]]), fileName

def applyTransform(piece, t):
    k, col, x, y, z, mat, name = piece
    nmat = t*mat
    mat2 = t.tolist()
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
    return k, col, nx, ny, nz, na, nb,nc,nd,ne,nf,ng,nh,ni, name

def printBrick(b):
    print '%1s %2s %8.2f %8.2f %8.2f %5g %5g %5g %5g %5g %5g %5g %5g %5g %s' % tuple(b)

f = open(sys.argv[1])
opiece = parseLine(f.readline())
ok, ocol, ox, oy, oz, omat, oname = opiece
t = inv(omat)
k, col, nx, ny, nz, na, nb,nc,nd,ne,nf,ng,nh,ni, name = applyTransform(opiece, t)
#print " ".join([k, col]+map(rounded, (0, 0, 0, na, nb,nc,nd,ne,nf,ng,nh,ni))+[name])   
print ('%1s %2s %8s %8s %8s %5s %5s %5s %5s %5s %5s %5s %5s %5s %s' % tuple([k, col]+map(rounded, (nx, ny, nz, na, nb,nc,nd,ne,nf,ng,nh,ni))+[name]))

for line in f.readlines():
    piece = parseLine(line)
    if piece:
        k, col, x, y, z, na, nb,nc,nd,ne,nf,ng,nh,ni, name = applyTransform(piece, t)
        #print " ".join([k, col]+map(rounded, (x-nx, y-ny, z-nz, na, nb,nc,nd,ne,nf,ng,nh,ni))+[name])
        print ('%1s %2s %8s %8s %8s %5s %5s %5s %5s %5s %5s %5s %5s %5s %s' % tuple([k, col]+map(rounded, (x, y, z, na, nb,nc,nd,ne,nf,ng,nh,ni))+[name]))

