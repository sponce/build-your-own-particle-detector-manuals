import sys

inputFile = sys.argv[1]
outputFile = inputFile.replace('ldr', 'mpd')

filesDone = []
filesToDo = [inputFile]

def parseFile(filename):
    bricks = {}
    for line in open(filename).readlines():
        items = line.split()
        if len(items) == 0:
            continue
        if items[0] != "1":
            continue
        k, col, x, y, z, a, b, c, d, e, f, g, h, i, name = items
        if name [-3:] == 'ldr' and name not in filesDone and name not in filesToDo:
            filesToDo.append(name)
            print 'needing', name

f = open(outputFile, 'w')

while len(filesToDo) > 0:
    name = filesToDo[0]
    parseFile(name)
    f.write('0 FILE %s\n' % name)
    f.write(open(name).read())
    f.write('0 NOFILE\n\n')
    filesToDo = filesToDo[1:]
    filesDone.append(name)

f.close()

