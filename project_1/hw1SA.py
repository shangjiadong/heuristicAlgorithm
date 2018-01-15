import numpy as np
import os
import random
import math
from random import randint
os.chdir("C:/Research/FE640HW")


with open ('hw1.txt') as f:
    initialVol = f.read().splitlines()
#print initialVol
vol0 = [int(item) for item in initialVol]
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

while hStd > 4.1:

    soln = [0] * 2001
    h = [0, 0, 0, 0, 0, 0]
    bestsoln = [0] * 2001
    vol = []
    loop = loop + 1
    jj = 0
    t0 = 10000
    tEnd = 0.1
    nRep = 100
    alpha = 0.995
    target = 440000
    currentTemp = t0
    bestObj = 0
    chkObj = 0
    objNow = 0

    for i in range(0,2001):
        temp = []
        temp.append(vol0[i])
        temp.append(vol1[i])
        temp.append(vol2[i])
        temp.append(vol3[i])
        temp.append(vol4[i])
        temp.append(vol5[i])
        vol.append(temp)

    for i in range(1, 6):
        objNow = objNow + (target - h[i]) ** 2

    globalbest = objNow

    while currentTemp > tEnd:
        for rep in range(0, nRep):
            jj = jj + 1
            x = randint(1, 2000)

            while True:
                per = randint(1, 5)
                if per != soln[x]:
                    break

            oldsoln = soln[x]
            soln[x] = per
            hold1 = h[oldsoln]
            hold2 = h[per]
            new_deviations = (target - (hold1 - vol[x][oldsoln])) ** 2 + (target - (h[per] + vol[x][per])) ** 2
            old_deviations = (target - hold1) ** 2 + (target - hold2) ** 2
            tempObj = objNow + new_deviations - old_deviations
            if tempObj < objNow:
                objNow = tempObj
                h[per] = h[per] + vol[x][per]
                h[oldsoln] = h[oldsoln] - vol[x][oldsoln]
                if objNow < globalbest:
                    globalbest = objNow
                    for i in range(1, 2001):
                        bestsoln[i] = soln[i]
            else:
                delta = tempObj - objNow
                k = 0.001 * delta / currentTemp
                if k < 10:
                    p = 1 / math.exp(k)
                else:
                    p = 0

                if random.random() < p:
                    objNow = tempObj
                    h[per] = h[per] + vol[x][per]
                    h[oldsoln] = h[oldsoln] - vol[x][oldsoln]
                else:
                    soln[x] = oldsoln

        currentTemp = currentTemp * alpha

    h = [0, 0, 0, 0, 0, 0]
    for i in range(1, 2001):
        h[bestsoln[i]] = h[bestsoln[i]] + vol[i][bestsoln[i]]

    for i in range(1, 6):
        chkObj = chkObj + (target - h[i]) ** 2

    hAvg = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
    hStd = (((h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2 + (h[5] - hAvg) ** 2 ) / 4 ) ** 0.5

    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(bestsoln)

    print "loop", loop, "h", h, "hAvg", hAvg, "hStd", hStd

    if loop > 8000:
        break

with open('SAharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('SAharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('SAharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('SAharvSchedule.txt', "a") as f:
    for i in range(0, len(harSch[-1])):
        f.write(str(i + 1) + ' ')
        f.write(str(harSch[-1][i]) + '\n')
