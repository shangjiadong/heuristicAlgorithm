def calcobj(x):
    h = [0] * 6
    obj = [0] * 201
    for i in range(1, 201):
        for j in range(1,101):
            h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
        for k in range(1,6):
            obj[i] = obj[i] + (target - h[k]) * (target - h[k])

    return h, obj

import os
import math
import random
from random import randint
import numpy as np
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

harVol = []
harAvg = []
harStd = []
harSch = []

for rep in range(0, 5000):
    niter = 400
    npop = 100

    w = 0.7
    c1 = 2
    c2 = 1

    x = []
    v = []
    obj = [0] * 201
    pbest = [0] * 201
    pxbest = []
    gxbest = [0] * 101
    vol = []
    h = [0] * 6

    for i in range(201):
        x.append([0]*101)
        v.append([0]*101)
        pxbest.append([0]*101)

    target = 24000

    for i in range(0,101):
        temp = []
        temp.append(vol0[i])
        temp.append(vol1[i])
        temp.append(vol2[i])
        temp.append(vol3[i])
        temp.append(vol4[i])
        temp.append(vol5[i])
        vol.append(temp)

    gbest = 1000000000000

    """
    xArray = np.random.randint(1,5, size = (201, 101))
    x = [list(item) for item in xArray]
    j = 0
    for i in range(1,201):
        x[i][j] = 0
    """

    for i in range(1, 201):
        for j in range(1,101):
            x[i][j] = randint(1,5)
            v[i][j] = 0


    for i in range(1, 201):
        #i = 1
        h = [0] * 6
        obj = [0] * 201
        for j in range(1,101):
            h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
        for k in range(1,6):
            obj[i] = obj[i] + (target - h[k]) ** 2
        #print obj[i]

        pbest[i] = obj[i]
        for j in range(1, 101):
            pxbest[i][j] = x[i][j]

        if obj[i] < gbest:
            gbest = obj[i]
            #print i
            for j in range(1, 101):
                gxbest[j] = x[i][j]
        #print obj[i], gbest
        #print i, obj[i], gbest

    for iter in range(1, niter+1):

        for i in range(1,npop+1):
            for j in range(1, 101):

                v[i][j] = w * v[i][j] + c1 * random.random() * (gxbest[j] - x[i][j]) + c2 * random.random() * (pxbest[i][j] - x[i][j])
                x[i][j] = x[i][j] + v[i][j]
                #x[i][j] = int(round(x[i][j]))

                x[i][j] = int(math.floor(x[i][j]))
                prob = 1 / (1 + math.exp(-1 * v[i][j]))
                if random.random() < prob:
                    x[i][j] = int(x[i][j]) + 1

                if x[i][j] > 5:
                    x[i][j] = 5
                if x[i][j] < 1:
                    x[i][j] = 1
            #print v[i]
            #print x[i]
            #print x
        for i in range(1,npop+1):
            h = [0] * 6
            obj = [0] * 201
            for j in range(1,101):
                h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
            for k in range(1, 6):
                obj[i] = obj[i] + (target - h[k]) ** 2

            if obj[i] < pbest[i]:
                pbest[i] = obj[i]
                for j in range(1, 101):
                    pxbest[i][j] = x[i][j]
            if obj[i] < gbest:
                gbest = obj[i]
                bestsoln = i
                for j in range(1, 101):
                    gxbest[j] = x[i][j]
                #print gbest

        h = [0] * 6
        for j in range(1, 101):
            h[gxbest[j]] = h[gxbest[j]] + vol[j][gxbest[j]]
        #print gxbest
        hAvg = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
        hStd = (((h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2 + (h[5] - hAvg) ** 2 ) / 5 ) ** 0.5



    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(gxbest)

    print "rep ", rep, "hStd ", hStd, "hAvg ", hAvg
    for i in range(1,6):
        print "period ", i, "volume ", h[i]

with open('PSharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('PSharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('PSharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('PSharvSchedule.txt', "a") as f:
    for item in harSch:
        f.write(str(item) + '\n')
