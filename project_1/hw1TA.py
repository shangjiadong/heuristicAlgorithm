import numpy as np
import os
import random
import math
os.chdir("C:/Research/FE640HW")

k = [0] * 6
k[0] = 1.09
k[1] = 1 + (math.exp(-0.5 * 0.9)) / 10
k[2] = 1 + (math.exp(-0.5 * 5.1)) / 10
k[3] = 1 + (math.exp(-0.5 * 12.0)) / 10
k[4] = 1 + (math.exp(-0.5 * 18.0)) / 10
k[5] = 1

with open ('hw1.txt') as f:
    initialVol = f.read().splitlines()
#print initialVol
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

while hStd > 14:

    soln = [0] * 2000
    h = [0, 0, 0, 0, 0]
    bestsoln = [0] * 2000
    vol = []
    loop = loop + 1
    nRep = 1500
    T = 439610

    for i in range(0,2000):
        temp = []
        temp.append(vol1[i])
        temp.append(vol2[i])
        temp.append(vol3[i])
        temp.append(vol4[i])
        temp.append(vol5[i])
        vol.append(temp)

    for i in range(0,2000):
        h[soln[i]] = h[soln[i]] + vol[i][soln[i]]

    objNow = 0
    for i in range(0,5):
        objNow = objNow + (T - h[i]) ** 2

    globalbest = objNow
    for n in range(0,6):
        for rep in range(0, nRep):
            x = int(random.random() * 2000)
            per = int(random.random() * 5)
            oldsoln = soln[x]
            soln[x] = per
            h = [0, 0, 0, 0, 0]
            for i in range(0, 2000):
                h[soln[i]] = h[soln[i]] + vol[i][soln[i]]
            tempObj = 0
            for i in range(0, 5):
                tempObj = tempObj + (T - h[i]) ** 2
            if tempObj < k[n] * objNow:
                objNow = tempObj
                if objNow < globalbest:
                    globalbest = objNow
                    for i in range(0,2000):
                        bestsoln[i] = soln[i]
            else:
                soln[x] = oldsoln
    h = [0, 0, 0, 0, 0]
    for i in range(0, 2000):
        h[bestsoln[i]] = h[bestsoln[i]] + vol[i][soln[i]]

    hAvg = (h[0] + h[1] + h[2] + h[3] + h[4]) / 5
    hStd = (((h[0] - hAvg) ** 2 + (h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2) / 4 ) ** 0.5

    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(bestsoln)

    print "loop", loop, "h", h, "hAvg", hAvg, "hStd", hStd
    if loop > 8000:
        break



with open('TAharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('TAharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('TAharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('TAharvSchedule.txt', "a") as f:
    for i in range(0, len(harSch[-1])):
        f.write(str(i + 1) + ' ')
        f.write(str(harSch[-1][i]) + '\n')
