
def calcobj(x):
    h = [0] * 6
    fitness = 0
    tot = 0
    for j in range(1, 6):
        for i in range(1, 101):
            if x[i] == j:
                h[j] = h[j] + v[i][j]
                tot = tot + v[i][j]
    ave = tot / 5
    for j in range(1, 6):
        fitness = fitness + (ave - h[j]) ** 2
    return fitness, h

def variance(obj, pop):
    mean = 0
    var = 0
    for n in range(1, pop+1):
        mean = mean + obj[n] / pop
    npop = pop - 1
    for n in range(1,pop+1):
        var = var + ((obj[n] - mean) ** 2) / npop
    std = math.sqrt(var)
    return std

def SWAP(a,b):
    c = a
    a = b
    b = c

import os
import math
import random
from random import randint
os.chdir("C:\Users\lenovo\Desktop\FE640HW")
#os.chdir("C:/Shangjia_File/FE640HW")
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


h = [0] * 6
#sol = [[0] * 101] * 51
opp = [0] * 51
prop = [0] * 51
rang = [0] * 51
x = [0] * 101
temp1 = [0] * 101
temp2 = [0] * 101
#nextgen = [[0] * 101] * 51
nextobj = [0] * 51
v = []
obj = [0] * 51
hStd = 100
objmax = 10
sol = []
nextgen = []
for i in range(51):
    sol.append([0]*101)
    nextgen.append([0]*101)


# rerun
while True:
    pop = 50
    for i in range(0,101):
        temp = []
        temp.append(vol0[i])
        temp.append(vol1[i])
        temp.append(vol2[i])
        temp.append(vol3[i])
        temp.append(vol4[i])
        temp.append(vol5[i])
        v.append(temp)
    for i in range(1, 101):
        for j in range(1, pop+1):
            sol[j][i] = 0

    for k in range(1, pop+1):
        for i in range(1,101):
            p = randint(1,5)
            sol[k][i] = p

    obj = [0] * 51
    objtot = 0

    for k in range(1, pop+1):
        for i in range(1, 101):
            x[i] = sol[k][i]
        fitness = calcobj(x)[0]
        h = calcobj(x)[1]
        obj[k] = fitness
        objtot = objtot + fitness

    std = variance(obj, pop)
    while std > 1:
        opptot = 0
        rang = [0] * 51
        for k in range(1, pop+1):
            if obj[k] > objmax:
                objmax = obj[k]
        objmax = objmax * 1.1
        for k in range(1, pop+1):
            opp[k] = objmax - obj[k]
            opptot = opptot + opp[k]

        for k in range(1, pop+1):
            prop[k] = opp[k] / opptot
            rang[k] = rang[k-1] + prop[k]
        # find offspring for next generation
        for n in range(1,pop+1):
            xx = random.random()
            for k in range(1, pop+1):
                if (xx >= (rang[k] - prop[k])) and (xx <= rang[k]):
                    break # potential error
            p1 = k

            while True:
                xx = random.random()
                for k in range(1, pop+1):
                    if (xx >= (rang[k] - prop[k])) and (xx <= rang[k]):
                        break # potential error
                p2 = k
                if p2 != p1:
                    break
            # make offspring
            xx = randint(1,100)
            for i in range(1, xx+1):
                temp1[i] = sol[p1][i]
                temp2[i] = sol[p2][i]

            for i in range(xx+1, 101):
                temp1[i] = sol[p2][i]
                temp2[i] = sol[p1][i]
            # introduce change of mutation for each offspring
            for i in range(1,101):
                xx = random.random()
                if xx < 0.02:
                    if i < 100:
                        SWAP(temp1[i], temp1[i+1])
                    else:
                        SWAP(temp1[i], temp1[i-1])
                xx = random.random()
                if xx < 0.02:
                    if i < 100:
                        SWAP(temp2[i], temp2[i+1])
                    else:
                        SWAP(temp2[i], temp2[i-1])
            # evaluate fitness of each offspring
            fit1 = calcobj(temp1)[0]
            fit2 = calcobj(temp2)[0]

            if fit1 < fit2:
                mostfit = fit1
            else:
                mostfit = fit2

            if mostfit < obj[p1] and mostfit < obj[p2]:
                if fit1 <= fit2:
                    j = 1
                    nextobj[n] = fit1
                else:
                    j = 2
                    nextobj[n] = fit2
                for i in range(1, 101):
                    if j == 1:
                        nextgen[n][i] = temp1[i]
                    else:
                        nextgen[n][i] = temp2[i]
            else:
                if obj[p1] < obj[p2]:
                    j = 1
                    nextobj[n] = obj[p1]
                else:
                    j = 2
                    nextobj[n] = obj[p2]
                for i in range(1,101):
                    if j == 1:
                        nextgen[n][i] = sol[p1][i]
                    else:
                        nextgen[n][i] = sol[p2][i]
        # update popolation array
        for k in range(1,pop+1):
            obj[k] = nextobj[k]
            for i in range(1, 101):
                sol[k][i] = nextgen[k][i]

        for i in range(51):
            nextgen.append([0]*101)

        nextobj = [0] * 51
        std = variance(obj, pop)
        # display solution for best fitness
    objmin = 10 ** 10
    for k in range(1, pop+1):
        if obj[k] < objmin:
            objmin = obj[k]
            bestk = k
    for i in range(1, 101):
        x[i] = sol[bestk][i]
    harSch.append(x)
    fitness = calcobj(x)[0]
    h = calcobj(x)[1]
    hAve = (h[1] + h[2] + h[3] + h[4] + h[5]) / 5
    hStd = math.sqrt(fitness)
    harVol.append(h)
    harSch.append(x)
    harAvg.append(hAve)
    harStd.append(hStd)
    print "hStd ", hStd
    for i in range(1,6):
        print "period ", i, "volume ", h[i]


    if hStd < 10:
        break

with open('GAharvestVol.txt', "a") as f:
    for item in harVol:
        f.write(str(item) + '\n')

with open('GAharvestAvg.txt', "a") as f:
    for item in harAvg:
        f.write(str(item) + '\n')

with open('GAharvestStd.txt', "a") as f:
    for item in harStd:
        f.write(str(item) + '\n')

with open('GAharvSchedule.txt', "a") as f:
    for item in harSch:
        f.write(str(item) + '\n')
