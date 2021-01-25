import sys
from math import cos, sin, pi

def produceRotationMatrix(angle):
    return 1, 0, 0, 0, cos(angle), -sin(angle), 0, sin(angle), cos(angle)

for n in (2,6,10,14,4,8,12):
    print "%d %d %d %d %4.2f %4.2f %d %4.2f %4.2f" % produceRotationMatrix(n*pi/8)

a,b,c,d,e,f,g,h,i,x,y,z,tx,ty,tz = map(float, sys.argv[1:])

nx = a*x + b*y + c*z
ny = d*x + e*y + f*z
nz = g*x + h*y + i*z

print tx-nx, ty-ny, tz-nz

