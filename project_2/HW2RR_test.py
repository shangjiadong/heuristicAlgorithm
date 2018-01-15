import os
import math
import random
from random import randint
#os.chdir("C:\Users\lenovo\Desktop\FE640HW")
os.chdir("C:/Research/FE640HW")
with open ('2001.txt') as f:
    initialVol = f.read().splitlines()
#print initialVol
vol0 = [0] * 2001
vol1 = [int(item) for item in initialVol]
vol2 = [item * 1.3 for item in vol1]
vol3 = [item * 1.3 for item in vol2]
vol4 = [item * 1.3 for item in vol3]
vol5 = [item * 1.3 for item in vol4]

hStd = 100
loop = 0
harVol = []
harAvg = []
harStd = []
harSch = []

while hStd > 25:

    soln = [0] * 2001
    h = [0] * 6
    bestsoln = [0] * 2001
    vol = []

    T = 440000
    deviation = 9999
    nrep = 200000
    decay = 0

    loop = loop + 1
    steps = 0

    for i in range(0,2001):
        temp = []
        temp.append(vol0[i])
        temp.append(vol1[i])
        temp.append(vol2[i])
        temp.append(vol3[i])
        temp.append(vol4[i])
        temp.append(vol5[i])
        vol.append(temp)

    for i in range(1,2001):
        soln[i] = randint(1,5)
        bestsoln[i] = soln[i]

    h = [0] * 6
    for i in range(1,2001):
        h[soln[i]] = h[soln[i]] + vol[i][soln[i]]

    objnow = 0
    for i in range(1,6):
        objnow = objnow + (T - h[i]) ** 2

    globalbest = objnow

    for rep in range(0,nrep):
        steps = steps + 1
        while True:
            x = randint(1,2000)
            per = randint(1,5)
            if soln[x] != per:
                break
        oldsoln = soln[x]
        soln[x] = per

        hold1 = h[oldsoln]
        hold2 = h[per]
        new_devs = (T - (hold1 - vol[x][oldsoln])) ** 2 + (T - (h[per] + vol[x][per])) ** 2
        old_devs = (T - hold1) ** 2 + (T - hold2) ** 2
        tempobj = objnow + new_devs - old_devs

        if tempobj < objnow - deviation:
            objnow = tempobj
            h[per] = h[per] + vol[x][per]
            h[oldsoln] = h[oldsoln] - vol[x][oldsoln]
            if objnow < globalbest:
                globalbest = objnow
                for i in range(1,2001):
                    bestsoln[i] = soln[i]
        else:
            soln[x] = oldsoln

    h = [0] * 6
    for i in range(1, 2001):
        h[bestsoln[i]] = h[bestsoln[i]] + vol[x][bestsoln[i]]

    hAvg = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
    hStd = (((h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2 + (h[5] - hAvg) ** 2) / 5 ) ** 0.5

    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(bestsoln)

    print "loop", loop, "h", h, "hAvg", hAvg, "hStd", hStd

    if loop > 1000:
        break

with open('RRharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('RRharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('RRharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('RRharvSchedule.txt', "a") as f:
    for item in harSch:
        f.write(str(item) + '\n')
