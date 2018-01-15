import os
import math
import random
from random import randint
import numpy as np
#os.chdir("C:\Users\lenovo\Desktop\FE640HW")
os.chdir("C:/Shangjia_File/FE640HW")
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
stdDev = 100

maxreps = 3000
numruns = 0

niter = 2000
npop = 30
hmcr = 0.69
par = 0.09
x = []
#x = [[0] * 101] * 31
for i in range(31):
    x.append([0] * 101)

obj = [0] * 31
vol = []
h = [0] * 6

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

while stdDev > 60:
    numruns = numruns + 1
    objworst = 0
    for i in range(1, 31):
        for j in range(1, 101):
            x[i][j] = randint(1,5)

    for i in range(1,31):
        h = [0] * 6
        obj = [0] * 31
        for j in range(1, 101):
            h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
        for k in range(1,5):
            obj[i] = obj[i] + (target - h[k]) ** 2
        if obj[i] > objworst:
            objworst = obj[i]
            solworst = i

    for ite in range(1, niter+1):
        for j in range(1,101):
            if random.random() < hmcr:
                harmony_memory = randint(1, 30)
                x[0][j] = x[harmony_memory][j]
                if random.random() < par:
                    if random.random() < 0.5:
                        x[0][j] = x[0][j] + 1
                        if x[0][j] > 5:
                            x[0][j] = x[0][j] - 4
                    else:
                        x[0][j] = x[0][j] - 1
                        if x[0][j] < 1:
                            x[0][j] = x[0][j] + 4
            else:
                x[0][j] = randint(1,5)
        i = 0
        h = [0] * 6
        obj = [0] * 31
        for j in range(1, 101):
            h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
        for k in range(1,5):
            obj[i] = obj[i] + (target - h[k]) ** 2

        if obj[0] < objworst:
            obj[solworst] = obj[0]
            for j in range(1,101):
                x[solworst][j] = x[0][j]

        objworst = 0
        for i in range(1, 31):
            h = [0] * 6
            obj = [0] * 31
            for j in range(1, 101):
                h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
            for k in range(1,5):
                obj[i] = obj[i] + (target - h[k]) ** 2

            if obj[i] > objworst:
                objworst = obj[i]
                solworst = i

    objbest = 99999999999999
    for i in range(1,31):
        h = [0] * 6
        obj = [0] * 31
        for j in range(1, 101):
            h[x[i][j]] = h[x[i][j]] + vol[j][x[i][j]]
        for k in range(1,5):
            obj[i] = obj[i] + (target - h[k]) ** 2
        if obj[i] < objbest:
            objbest = obj[i]
            solbest = i
    h = [0] * 6
    for j in range(1,101):
        cutper = x[solbest][j]
        h[cutper] = h[cutper] + vol[j][cutper]

    hAvg = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
    hStd = (((h[1] - hAvg) ** 2 + (h[2] - hAvg) ** 2 + (h[3] - hAvg) ** 2 + (h[4] - hAvg) ** 2 + (h[5] - hAvg) ** 2 ) / 5 ) ** 0.5

    print "hAvg ", hAvg, "stdDev ", hStd, "h ", h
    harVol.append(h)
    harAvg.append(hAvg)
    harStd.append(hStd)
    harSch.append(x[solbest])

    if numruns > 8000:
        break
with open('HSharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('HSharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('HSharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('HSharvSchedule.txt', "a") as f:
    for item in harSch:
        f.write(str(item) + '\n')
