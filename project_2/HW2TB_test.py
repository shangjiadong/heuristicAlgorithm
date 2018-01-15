import os
import math
import random
from random import randint
#os.chdir("C:\Users\lenovo\Desktop\FE640HW")
os.chdir("C:/Research/FE640HW")
with open ('100.txt') as f:
    initialVol = f.read().splitlines()
#print initialVol
vol0 = [0] * 101
vol1 = [int(item) for item in initialVol]
vol2 = [item * 1.3 for item in vol1]
vol3 = [item * 1.3 for item in vol2]
vol4 = [item * 1.3 for item in vol3]
vol5 = [item * 1.3 for item in vol4]

loop = 0
harVol = []
harAvg = []
harStd = []
harSch = []

soln = [0] * 101
h = [0] * 6
bestsoln = [0] * 101
vol = []

tabu = []
obj = []

for i in range(101):
    tabu.append([0] * 6)
    obj.append([0] * 6)

T = 24000
Big = 999999999999
neigoborhoods = 160
taboo = 52
Nmod = 10
bests = randint(1,5)
bestp = randint(1,5)

for i in range(0,101):
    temp = []
    temp.append(vol0[i])
    temp.append(vol1[i])
    temp.append(vol2[i])
    temp.append(vol3[i])
    temp.append(vol4[i])
    temp.append(vol5[i])
    vol.append(temp)

for i in range(1,101):
    soln[i] = 0
    bestsoln[i] = soln[i]

h = [0] * 6
for i in range(1,101):
    h[soln[i]] = h[soln[i]] + vol[i][soln[i]]

objnow = 0
for i in range(1,6):
    objnow = objnow + (T - h[i]) ** 2

globalbest = objnow

for N in range(1,neigoborhoods+1):
    obj = []
    for i in range(101):
        obj.append([0] * 6)
    for p in range(1,101):
        for s in range(1,6):
            if s == soln[p]:
                obj[p][s] = Big
            else:

                old = soln[p]
                soln[p] = s
                h = [0] * 6
                for i in range(1, 101):
                    h[soln[i]] = h[soln[i]] + vol[i][soln[i]]
                for i in range(1,6):
                    obj[p][s] = obj[p][s] + (T - h[i]) ** 2

                soln[p] = old
    #print h
    bestobj = Big
    for p in range(1,101):
        for s in range(1,6):
            if obj[p][s] < bestobj:
                bestobj = obj[p][s]
                bestp = p
                bests = s
    if bestobj < globalbest:
        globalbest = bestobj
        soln[bestp] = bests
        for i in range(1,101):
            bestsoln[i] = soln[i]
        # tabulist
        for p in range(1,101):
            for s in range(1,6):
                if tabu[p][s] > 0:
                    tabu[p][s] = tabu[p][s] - 1
        for s in range(1,6):
            tabu[bestp][s] = taboo

    else:
        bestobj = Big
        for p in range(1,101):
            for s in range(1,6):
                if (obj[p][s] < bestobj) and (tabu[p][s] == 0):
                    bestobj = obj[p][s]
                    bestp = p
                    bests = s
        soln[bestp] = bests
        for p in range(1,101):
            for s in range(1,6):
                if tabu[p][s] > 0:
                    tabu[p][s] = tabu[p][s] - 1
        for s in range(1,6):
            tabu[bestp][s] = taboo
    #print bestsoln
    #if N % Nmod == 0:
    #    print "N ", N, "globalbest ", globalbest, "bestobj ", bestobj

    h = [0] * 6
    for i in range(1,101):
        h[bestsoln[i]] = h[bestsoln[i]] + vol[i][bestsoln[i]]

    bestobj = 0
    for i in range(1,6):
        bestobj = bestobj + (T - h[i]) ** 2

    hAvg = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
    hStd = (((h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2 + (h[5] - hAvg) ** 2) / 4 ) ** 0.5
    print "h", h, "hAvg", hAvg, "hStd", hStd
    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(bestsoln)

with open('TBharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('TBharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('TBharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('TBharvSchedule.txt', "a") as f:
    for item in harSch:
        f.write(str(item) + '\n')
